from app.main.service.base_svc import BaseSvc

class TotalTripsByDateSvc(BaseSvc):

    def __init__(self):
        self.total_trips_by_date_for_range = None
        #self.DBCONFIG, self.APICONFIG  = self.load_config()

    
    def get_data(self, start_date, end_date):
        
        """Gets the counts of trips grouped by date based on the provided date range """

        api_name = 'total_trips'
        self.create_BQ_connection(api_name)
        main_table_names = self.legacy_query_formatter_from(api_name, 'main_data_project')
        usecaching = self.APICONFIG[api_name]['caching_enabled']
        total_trips_by_date_for_range_df ={'message :': 'Error Occured while quering google big query'}

        if usecaching:
            #query data and cache 
            query_all_trips = """
                                SELECT  
                                    DATE(pickup_datetime) as date , 
                                    count(*) as total_trips
                                FROM {0}
                                group by date
                                order by date
                            """.format(main_table_names)
            query_all_trips_cache_table_id = self.query_and_cache_if_required(query_all_trips, api_name, 'all_trips_by_date')
            
            #query data from Cache 
            query_all_trips_cache  = """
                                        SELECT 
                                            *                                                 
                                        FROM {0}
                                        where date>='{1}' and date<='{2}'
                                        order by date
                                    """.format(query_all_trips_cache_table_id, start_date, end_date)
            total_trips_by_date_for_range_df = self.query_BQ(query_all_trips_cache)
        
        else:
            #query data without caching
            query_all_trips_normal = """
                                        SELECT  
                                            DATE(pickup_datetime) as date , 
                                            count(*) as total_trips
                                        FROM {0}
                                        where DATE(pickup_datetime)>='{1}' and DATE(pickup_datetime)<='{2}'
                                        group by date
                                        order by date
                                    """.format(main_table_names, start_date, end_date)

            total_trips_by_date_for_range_df = self.query_BQ(query_all_trips_normal)

        #default mode is legacy 
        self.total_trips_by_date_for_range = eval(total_trips_by_date_for_range_df.to_json(orient ='records'))
        return  self.total_trips_by_date_for_range

        #total_trips_by_date_for_query_df = self.filter_by_date_range(totaltrips_by_date_df, start_date, end_date)
        #self.total_trips_by_date_for_query = eval(total_trips_by_date_for_query_df.to_json(orient ='records'))
        #return self.total_trips_by_date_for_query


    # def filter_by_date_range(self, total_trips, start_date, end_date):

    #     greater_than_mask = total_trips['date'] >= start_date
    #     less_than_mask = total_trips['date'] <= end_date
    #     query_df =total_trips[greater_than_mask & less_than_mask]
    #     return query_df

