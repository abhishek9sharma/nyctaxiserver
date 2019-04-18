
from google.cloud import bigquery
from google.oauth2 import service_account
from app.configuration.dbconfig import API_CONFIG, DATABASE_CONFIG as DBCONFIG

class BQConnector:
    """ A Class used to represent connection with Biq Query DataBase """

    def __init__(self, api_name):
        
        self.bq_svc_acnt_file = DBCONFIG['big_query_keys'][API_CONFIG[api_name]['bq_key']]
        self.credentials = service_account.Credentials.from_service_account_file(self.bq_svc_acnt_file)
        self.client = bigquery.Client(credentials = self.credentials, project= self.credentials.project_id)
        #self.client = bigquery.Client(credentials = self.credentials, project = self.project_id)

    def legacy_query_formatter_from(self, dbconfig, api_name, databases = [], tables = []):

        """Helper method to load the dataset and tables to be queried """
        try:
            
            tableliststr = ''
            apidataset = API_CONFIG[api_name]['dataset']
            datasetinfo = dbconfig['datasets'][apidataset]

            for dbname, dbinfo in datasetinfo['databases'].items():
                if len(databases)==0 or (dbname in databases):
                    for tbl in dbinfo['tables']:
                        if len(tables)==0 or (tbl in tables):
                            tableliststr = tableliststr + ('[' + apidataset + '.' + dbname +'.' + tbl + '],')

            return tableliststr
        
        except:
            raise ValueError('Exception Occured while formating legacy quuery for attaching tables for dataset ', apidataset)

    
    def execute_legacy_query(self, query, api_name, create_table = False):

        """Class Method to execute a parameterized query in legacy SQL Format"""
        try:
                formatted_query = query.format(self.legacy_query_formatter_from(DBCONFIG,api_name))
                job_config = bigquery.QueryJobConfig()
                job_config.use_legacy_sql = True
                job_config.use_query_cache = True
                if create_table:
                    #creat cache table
                    pass
                query_results_df = self.client.query(formatted_query, job_config=job_config).to_dataframe()
                return query_results_df
        except Exception as e:
            raise e
            
        return query_results_df


    # COMMENTED AS NOT BEIN USED IN CURRENT FLOW
    # def set_queryparams(self, query_params, typedict):
    #     """
    #     Class method which creates a list of parameters in the format required for big query 
    #     interaction (which are dynamically pased as paramdict) to be passed to the query 
    #     """ 
        
    #     paramlist =[]
    #     for pkey in query_params.keys():
    #             param_value = query_params[pkey]
    #             param_type = type(pkey).__name__
    #             currparam = bigquery.ScalarQueryParameter(pkey, typedict[param_type], param_value)
    #             paramlist.append(currparam)
    #     return paramlist
        
    #     # for param_name, param_info in paramdict.items():
    #     #     param_dtype = param_info['dtype']
    #     #     param_value= param_info['val']
    #     #     currparam = bigquery.ScalarQueryParameter(param_name, param_dtype, param_value)
    #     #     paramlist.append(currparam)
    #     # return paramlist
   
    # # COMMENTED AS NOT BEIN USED IN CURRENT FLOW
    # def execute_standard_query(self, query, api_name, create_table_in_BQ, query_params = None, typedict = None):
        
    #     """Class Method to execute a parameterized query in standard SQL Format."""
        
    #     try:
    #         formatted_query = 'to be implemented'
    #         job_config = bigquery.QueryJobConfig()
    #         if query_params:
    #             query_param_list =self.set_queryparams(query_params, typedict)
    #             job_config.query_parameters = query_params
    #             query_results_df = self.client.query(query, job_config=job_config).to_dataframe()

    #         else:
    #             query_results_df = self.client.query(query, job_config=job_config).to_dataframe()
        
    #     except Exception as e:
    #            raise e
        
    #     return query_results_df


    # COMMENTED AS NOT BEIN USED IN CURRENT FLOW
    # def create_param_dict(self, query_params):
            
        #     for pkey in query_params.keys():
        #             paramvalue = query_params[pkey]
        #             paramtype = type(pkey).__name__
        #             query_param_dict[pkey] = {'dtype': typedict[paramtype], 'val': paramvalue}
        #     # else:
        #     #     query_param_dict = None

        
