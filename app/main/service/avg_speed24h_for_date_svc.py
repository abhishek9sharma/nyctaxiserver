from app.main.service.base_svc import BaseSvc
from app.main.utils.validation_helper import  *
import os

class AvgFare24HForDateSvc(BaseSvc):

    def __init__(self):
        self.avg_speed_for_date = None
        self.testdir = os.path.abspath(os.path.dirname(__file__))



    
    def get_data(self, input_date):
        
        """ Gets the average speed for all the trips in the date range --> (input_date-24 hours) to (input_date)  """
        
        #Load values from configuration
        api_name = 'avg_speed24h'
        datetime_format = self.APICONFIG[api_name]['datetimeformat'] 
        table_filter = self.APICONFIG[api_name]['table_filter'] 
        usecaching = self.APICONFIG[api_name]['caching_enabled']
        if len(table_filter)==0 or datetime_format in [None, '']:
            raise ValueError("Could not find which tables to query for service and or datetime format to use " + self.__class__.__name__)

        
        #get timestamp 24 hours behind using utilty functions
        input_datetime_obj = get_datetime_in_specified_format(input_date, datetime_format)
        prev_datetime_obj = get_previous_datetime(input_datetime_obj, hours_behind = 24)
        prev_datetime_str = get_datetime_string_in_specified_format(prev_datetime_obj, datetime_format)

        #create connection with big query API
        self.create_BQ_connection(api_name)
        main_table_names = self.legacy_query_formatter_from(api_name, 'main_data_project', tables= table_filter)
        
        if usecaching:
            #create connection with big query API and also get table names to be queried
            query_total_dist_time = """
                                    SELECT  
                                        DATETIME(DATE(dropoff_datetime)) as dropoff_DATE, 
                                        SUM(float(trip_distance)) as total_distance,
                                        SUM(TIMESTAMP_TO_SEC(TIMESTAMP(dropoff_datetime)) - TIMESTAMP_TO_SEC(TIMESTAMP(pickup_datetime))) as total_trip_time_in_seconds,
                                        count(*) as no_of_trips
                                    FROM {0}
                                    WHERE
                                        trip_distance is not null AND 
                                        dropoff_datetime is not null AND
                                        pickup_datetime is not null AND
                                        string(trip_distance) <> 'INVALID'
                                    GROUP BY 
                                        dropoff_DATE
                                                                        
                                    """.format(main_table_names)         
            query_total_dist_time_table_id = self.query_and_cache_if_required(query_total_dist_time, api_name, 'total_distance_time_by_ts')
            
            #create query for getting final required information from cache and then run it
            query_total_dist_cache  = """
                                        SELECT 
                                            (3600 * total_distance/total_trip_time_in_seconds) as average_speed                                                
                                        FROM {0}
                                        where dropoff_DATE>datetime('{1}') and dropoff_DATE<=datetime('{2}')
                                    """.format(query_total_dist_time_table_id, prev_datetime_str, input_date)
            avg_speed_for_date_df = self.query_BQ(query_total_dist_cache)
        
        else:
            #create query for fetching data directly from big query witout caching, and run the query
            query_all_trips_normal = """
                                        SELECT
                                        (3600 * total_distance / total_trip_time_in_seconds) as average_speed 
                                        FROM
                                        (
                                            SELECT
                                                DATETIME(DATE(dropoff_datetime)) as dropoff_DATE,
                                                SUM(float(trip_distance)) as total_distance,
                                                SUM(TIMESTAMP_TO_SEC(TIMESTAMP(dropoff_datetime)) - TIMESTAMP_TO_SEC(TIMESTAMP(pickup_datetime))) as total_trip_time_in_seconds,
                                                count(*) as no_of_trips 
                                            FROM {0}
                                            WHERE
                                                trip_distance is not null AND 
                                                dropoff_datetime is not null AND
                                                pickup_datetime is not null AND
                                                string(trip_distance) <> 'INVALID'
                                            GROUP BY 
                                                dropoff_DATE
                                        )
                                        WHERE
                                        dropoff_DATE > datetime('{1}') 
                                        and dropoff_DATE <= datetime('{2}')
                                        """.format(main_table_names, prev_datetime_str, input_date)
            avg_speed_for_date_df = self.query_BQ(query_all_trips_normal)

        #case where no data found in big query table (CHECK)
        if avg_speed_for_date_df.size==0:
            return  self.avg_speed_for_date


        #reformat the data fetched as json and return it to the service handdler
        self.avg_speed_for_date = eval(avg_speed_for_date_df.to_json(orient ='records'))
        return  self.avg_speed_for_date

     
  