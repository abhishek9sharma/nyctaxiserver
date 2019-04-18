from app.main.service.base_svc import BaseServiceManager

class TotalTripsByDateServiceManager(BaseServiceManager):

    def __init__(self):
        self.total_trips_by_date_for_query = None
        #self.DBCONFIG, self.APICONFIG  = self.load_config()

    
    def get_data(self, start_date, end_date):
        
        """Gets the counts of trips grouped by date based on the provided date range """

        #populate query params for running queries in standard SQL format (COMMENT/DELETE/ not used in current flow)
        # temp_locals = locals().copy()
        # queryparams = {}
        # for pargkey in temp_locals.keys():
        #     if pargkey not in ['self']:
        #         queryparams[pargkey] = temp_locals[pargkey]


        api_name = 'total_trips'
        query = """
                         SELECT  
                               DATE(pickup_datetime) as date , 
                               count(*) as total_trips
                         FROM {0}
                         group by date
                         order by date
                     """
        
        #default mode is legacy 
        totaltrips_by_date_df = self.query_BQ(query, api_name, create_table_in_BQ= True)
        
        total_trips_by_date_for_query_df = self.filter_by_date_range(totaltrips_by_date_df, start_date, end_date)
        self.total_trips_by_date_for_query = eval(total_trips_by_date_for_query_df.to_json(orient ='records'))
        return self.total_trips_by_date_for_query


    def filter_by_date_range(self, total_trips, start_date, end_date):

        greater_than_mask = total_trips['date'] >= start_date
        less_than_mask = total_trips['date'] <= end_date
        query_df =total_trips[greater_than_mask & less_than_mask]
        return query_df

