from app.main.utils.big_query_helper import BQConnector

class BaseServiceManager:

    """ Data Access  service to fetch data from data tables """
    
    def fetch_records_from_BQ(self, query, dbconfig, query_params = None):
        
        typedict = {'str':'STRING', 'int':'INTEGER'}
        
        connection = BQConnector(dbconfig)
        query_param_dict = {}

        if query_params:
            for pkey in query_params.keys():
                paramvalue = query_params[pkey]
                paramtype = type(pkey).__name__
                query_param_dict[pkey] = {'dtype': typedict[paramtype], 'val': paramvalue}
        
        records = connection.executequery(query, query_param_dict)
        return records
        
        
