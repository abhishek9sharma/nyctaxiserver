from app.main.service.base_svc import BaseSvc

class TotalTripsByDateSvc(BaseSvc):

    def __init__(self):
        self.total_trips_by_date_for_range = None
        #self.DBCONFIG, self.APICONFIG  = self.load_config()

    
    def get_data(self, start_date, end_date):
        
        """Gets the counts of trips grouped by date based on the provided date range """

        api_name = 'total_trips'
        table_filter = self.APICONFIG[api_name]['table_filter']
        datetime_format = self.APICONFIG[api_name]['datetimeformat']

        #create connection
        self.create_BQ_connection(api_name)
        main_table_names = self.legacy_query_formatter_from(api_name, 'main_data_project', tables= table_filter)
        usecaching = self.APICONFIG[api_name]['caching_enabled']
        total_trips_by_date_for_range_df ={'message :': 'Error Occured while quering google big query'}

        #IF date format changes from date to something else the DATE function in below query needs to be update accordingly
        if usecaching:
            #query data and cache 
            query_all_trips = """
                                SELECT  
                                    DATETIME(DATE(pickup_datetime)) as pickup_DATE , 
                                    count(*) as total_trips
                                FROM {0}
                                WHERE pickup_datetime  is not  null
                                GROUP BY pickup_DATE
                                --ORDER BY pickup_DATE
                            """.format(main_table_names)
            query_all_trips_cache_table_id = self.query_and_cache_if_required(query_all_trips, api_name, 'all_trips_by_date')
            
            #query data from Cache 
            query_all_trips_cache  = """
                                        SELECT 
                                            DATE(pickup_DATE) as date,
                                            total_trips                                              
                                        FROM {0}
                                        WHERE pickup_DATE>=datetime('{1}') and pickup_DATE<=datetime('{2}')
                                        ORDER BY pickup_DATE
                                    """.format(query_all_trips_cache_table_id, start_date, end_date)
            total_trips_by_date_for_range_df = self.query_BQ(query_all_trips_cache)
        
        else:
            #query data without caching
            query_all_trips_normal = """
                                        SELECT  
                                            DATE(pickup_datetime) as date, 
                                            count(*) as total_trips
                                        FROM {0}
                                        WHERE pickup_datetime  is not  null and 
                                              DATE(pickup_datetime)>='{1}' and DATE(pickup_datetime)<='{2}'
                                        GROUP by date
                                        ORDER by date
                                    """.format(main_table_names, start_date, end_date)

            total_trips_by_date_for_range_df = self.query_BQ(query_all_trips_normal)

        self.total_trips_by_date_for_range = eval(total_trips_by_date_for_range_df.to_json(orient ='records'))
        return  self.total_trips_by_date_for_range



