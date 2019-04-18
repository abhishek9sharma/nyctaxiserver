from app.main.utils.big_query_helper import BQConnector
from app.configuration.dbconfig import  API_CONFIG
from abc import abstractmethod, ABC



class BaseServiceManager(ABC):

    """ Data Access  service to fetch data from data tables """

    APICONFIG = API_CONFIG
    cached_tables_dict = {}

    def query_BQ(self, query, api_name,  legacy = True, query_params = None, create_table_in_BQ = False, typedict = {}):
        
        connection = BQConnector(api_name)
        if legacy:
            records = connection.execute_legacy_query(query, api_name, create_table_in_BQ)
        else:
            raise ValueError(" standard queries are not supported yet")
            #records = connection.execute_standard_query(query, api_name, create_table_in_BQ, query_params, typedict)

        return records


    def get_cached_tables(self):
        return self.cached_tables_dict

    def update_cached_tables(self, table_key, table_val):
        self.cached_tables_dict[table_key] = table_val

        
    # def load_config(self):
    #      return DATABASE_CONFIG, API_CONFIG

    @abstractmethod
    def get_data(self):
        pass
