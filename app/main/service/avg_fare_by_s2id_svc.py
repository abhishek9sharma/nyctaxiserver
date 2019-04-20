from app.main.service.base_svc import BaseSvc
from app.main.utils.s2id_helper import *

class AvgFareByS2IDSvc(BaseSvc):

    def __init__(self):
        self.avg_fares_by_S2ID = None

    
    def get_data(self, input_date):
        
        """Gets the counts of trips grouped by date based on the provided date range """

        api_name = 'avg_fare_S2ID'
        date_year = input_date.split('-')[0]
        table_filter = self.APICONFIG[api_name]['table_filter'] 

        
        #creat BQ connection
        self.create_BQ_connection(api_name)
        main_table_names = self.legacy_query_formatter_from(api_name, 'main_data_project', tables = [date_year])
        usecaching = False
        avg_speed_for_date = {'message :': 'Error Occured while quering google big query'}

        if usecaching:
            raise ValueError ("Caching not enabled for this end points")
        else:
            #query data without caching
            query_total_fare = """
                                    SELECT * FROM (
                                    SELECT
                                        DATETIME(DATE(pickup_datetime)) as pickup_DATE,
                                        pickup_latitude, 
                                        pickup_longitude,
                                        SUM(fare_amount) as fare
                                    FROM {0}
                                    GROUP BY pickup_DATE, pickup_latitude, pickup_longitude)
                                    WHERE pickup_DATE = datetime('{1}')                                  
                                    """.format(main_table_names, input_date)         
            total_fares_by_date_df = self.query_BQ(query_total_fare)

        

        avg_fares_by_S2ID_df = self.get_avg_fare_by_s2id(total_fares_by_date_df)
        self.avg_fares_by_S2ID = eval(avg_fares_by_S2ID_df.to_json(orient ='records'))
        return self.avg_fares_by_S2ID




    def get_avg_fare_by_s2id(self, location_fares_df):
        
        location_fares_df['s2id'] = location_fares_df.apply(lambda x: compute_s2id_sphere_lat_long(x.pickup_latitude, x.pickup_longitude), axis=1)
        fares_df = location_fares_df[['fare','s2id']]
        avg_fares_df = fares_df.groupby('s2id').mean().reset_index()
        return avg_fares_df

