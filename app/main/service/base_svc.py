from app.main.utils.big_query_helper import BQConnector
from app.configuration.dbconfig import  API_CONFIG, DATABASE_CONFIG as DBCONFIG
from abc import abstractmethod, ABC



class BaseSvc(ABC):
    """ Base class for Data Access  service to fetch data from data tables """

    APICONFIG = API_CONFIG
    cached_tables_dict = {}

    def create_BQ_connection(self, api_name):
        """ Method which creates a connection for a service class related to an end point """
        
        self.bq_svc_accnt_file = DBCONFIG['big_query_keys'][API_CONFIG[api_name]['bq_key']]
        self.connection = BQConnector(self.bq_svc_accnt_file)
        

    def query_BQ(self, query, cache_query_in_BQ = False, cache_info = {}, query_from_cache = False, legacy = True, typedict = {}, query_params = None):
        """ Method which runs various kinds queries by a service class related to an end point"""
        
        if legacy:
            records = self.connection.execute_legacy_query(query, cache_query_in_BQ, cache_info)
        else:
            raise ValueError(" standard queries are not supported yet")
            #records = connection.execute_standard_query(query, api_name, create_table_in_BQ, query_params, typedict)

        return records

    def query_and_cache_if_required(self, query_create_cache, api_name, cache_id):
        """ Method which executes a query and caches it invoked by a service class related to an end point"""
      
        cache_info = API_CONFIG[api_name]['cache_info'][cache_id]
        cache_info = self.resolve_cache_table_name(cache_info)  

        try:
            if cache_info['cache_table_key'] not in self.get_cached_tables():
                cached_table_status = self.query_BQ(query_create_cache, cache_query_in_BQ = True, cache_info = cache_info)
                if cached_table_status:
                    self.update_cached_tables(cache_info['cache_table_key'], '['+cache_info['cache_table_key']+'],')
        except:
            return self.get_cached_tables()

        return self.get_cached_tables()[cache_info['cache_table_key']]

    def get_cached_tables(self):
        """ Method which returns the dictionary containing all the tables which have been cached by varous service classes related to endpoints """
        return self.cached_tables_dict

    def update_cached_tables(self, table_key, table_val):
        """ Method which upadetd the dictionary containing all the tables which have been cached by varous service classes related to endpoints """
        self.cached_tables_dict[table_key] = table_val

    def resolve_cache_table_name(self, cache_info):
        #""" Method which resolve the full keyname and big query table name for a table to be cached """"
        class_name = self.__class__.__name__
        project_name = cache_info['projectname']
        dataset_name = cache_info['dataset']
        table_name =  cache_info['table']
        cache_info['cache_table_key'] = ".".join([project_name, dataset_name, table_name])+'_' +class_name
        cache_info['cache_table_id'] = table_name + '_' + class_name
        return cache_info
        
        
    def legacy_query_formatter_from(self, api_name, project_name, datasets =[], tables = []):
        
        """Helper method to load the dataset and tables to be queried """
        
        try:
            tableliststr = ''

            apidataset = API_CONFIG[api_name][project_name]
            datasetinfo = DBCONFIG['datasets'][apidataset]

            for dbname, dbinfo in datasetinfo['datasets'].items():
                if len(datasets)==0 or (dbname in datasets):
                    for tbl in dbinfo['tables']:
                        tbl_year = tbl.split('_')[-1]
                        if len(tables)==0 or (tbl in tables) or (tbl_year in tables):
                            tableliststr = tableliststr + ('[' + apidataset + '.' + dbname +'.' + tbl + '],')
            return tableliststr      
        except:
            raise ValueError('Exception Occured while formating legacy quuery for attaching tables for dataset ', apidataset)
   
    @abstractmethod
    def get_data(self):
        pass
