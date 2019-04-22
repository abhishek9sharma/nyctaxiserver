
from google.cloud import bigquery
from google.oauth2 import service_account
import  datetime, pytz
from app.configuration.dbconfig import API_CONFIG, DATABASE_CONFIG as DBCONFIG
import time

class BQConnector:
    """ A Class used to represent connection with Biq Query DataBase """

    def __init__(self, bq_svc_accnt_file):
        """Initializes a connection with big query database"""
        
        self.credentials = service_account.Credentials.from_service_account_file(bq_svc_accnt_file)
        self.client = bigquery.Client(credentials = self.credentials, project= self.credentials.project_id)



    def verify_dataset(self, dataset_id):
        """ This methofd checks if a dataset exists in current accounts project in google big query, else creates the dataset"""
        
        client_data_sets = [d.dataset_id for d in self.client.list_datasets()]
        if dataset_id in client_data_sets:
            return True
        else:
            status = self.client.create_dataset(dataset_id)
            if status.dataset_id==dataset_id:
                return True
            else:
                return False

    def check_if_recently_cached(self, table_id, dataset_id, table_fullid):
        """" This method checks if a query has been recently cached """

        table_exists = False
        recently_cached = False
        client_tables = [ t.table_id for t in list(self.client.list_tables(dataset_id))]
        if table_id in client_tables:
            table_exists = True
            table_info = self.client.get_table(table_fullid)
            last_cached = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - table_info.created
            if last_cached.days<2:
                recently_cached = True

        return table_exists, recently_cached
        
        

    def execute_legacy_query(self, query, cache_query_in_BQ_table = False, cache_info = {}):
        """This method executes a query in legacy SQL Format in google big query table"""
        
        try:
            
            # set big query job main parameters
            job_config = bigquery.QueryJobConfig()
            job_config.use_legacy_sql = True
            job_config.use_query_cache = True
          
            if cache_query_in_BQ_table:
                #caches the query if not already cached
                try:
                    cache_dataset_id = cache_info['dataset']
                    if self.verify_dataset(cache_dataset_id):
                        cache_table_name = cache_info['cache_table_id']
                        cache_table_key = cache_info['cache_table_key']
                        table_exists,recently_cached = self.check_if_recently_cached(cache_table_name, cache_dataset_id, cache_table_key)

                        # if query has been recently cached
                        if table_exists and recently_cached:
                            return True
                        else:
                            # delete the last cached table if it was cached 2 days ago
                            if table_exists:
                                self.client.delete_table(cache_table_key, not_found_ok=True)
                                print('Previous Cache deleted for table ' + cache_table_key)
                            
                            # run and cache the query
                            bq_cache_table_name = self.client.dataset(cache_dataset_id).table(cache_table_name)
                            job_config.destination = bq_cache_table_name
                            job_config.allow_large_results = True
                            query = self.client.query(query, job_config=job_config)
                           

                            # wait till the query cache job finishes
                            query_state = query.state
                            while query_state!='DONE':
                                query_state = self.client.get_job(query.job_id).state
                            print('New Cache created for table ' + cache_table_key)
                            
                            # return True if query cached finished
                            if query_state=='DONE':
                                return  True
                            else:
                                return  False
                    else:
                        raise ValueError("Isssue while creating or finding the dataset ", cache_dataset_id)
                except Exception as e:
                    raise ValueError("Message : Issue while creating cache for table {0} in dataset {1}", cache_table_name, cache_dataset_id)
                 
            else:
                # run query without caching
                query_results_df = self.client.query(query, job_config=job_config).to_dataframe()
                return query_results_df

        except Exception as e:
            raise e
            

