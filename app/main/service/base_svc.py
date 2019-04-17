from app.main.utils.big_query_helper import BQConnector
from app.configuration.dbconfig import DATABASE_CONFIG, API_CONFIG



class BaseServiceManager:

    """ Data Access  service to fetch data from data tables """
    
    def fetch_records_from_BQ(self, query, dbconfig,  legacy = True, query_params = None,):
        
        typedict = {'str':'STRING', 'int':'INTEGER'}
        
        connection = BQConnector(dbconfig)
        if legacy:
            records = connection.execute_legacy_query(query)
        else:
            query_param_dict = {}

            if query_params:
                for pkey in query_params.keys():
                    paramvalue = query_params[pkey]
                    paramtype = type(pkey).__name__
                    query_param_dict[pkey] = {'dtype': typedict[paramtype], 'val': paramvalue}
            else:
                query_param_dict = None

            records = connection.execute_standard_query(query, query_param_dict)
        return records
        
        
    def load_config(self):
         return DATABASE_CONFIG, API_CONFIG

