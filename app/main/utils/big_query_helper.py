
from google.cloud import bigquery
from google.oauth2 import service_account

class BQConnector:
    """ A Class used to represent connection with Biq Query DataBase """

    def __init__(self, svcacntfile):

        
        self.svcacntfile = svcacntfile
        self.credentials = service_account.Credentials.from_service_account_file(self.svcacntfile)
        self.client = bigquery.Client(credentials = self.credentials, project= self.credentials.project_id)
        #self.client = bigquery.Client(credentials = self.credentials, project = self.project_id)

    def set_queryparams(self, paramdict):
        """
        Class method which creates a list of parameters in the format required for big query 
        interaction (which are dynamically pased as paramdict) to be passed to the query 
        """

        paramlist =[]
        for param_name, param_info in paramdict.items():
            param_dtype = param_info['dtype']
            param_value= param_info['val']
            currparam = bigquery.ScalarQueryParameter(param_name, param_dtype, param_value)
            paramlist.append(currparam)
        return paramlist



    def executequery(self, query, paramdict = None):
        """Class Method to execute a parameterized query"""

        if paramdict:
            query_params =self.set_queryparams(paramdict)     
            job_config = bigquery.QueryJobConfig()
            job_config.query_parameters = query_params
            query_results_df = self.client.query(query, job_config=job_config).to_dataframe()
        
        else:
            query_results_df = self.client.query(query).to_dataframe()
        
        return query_results_df
