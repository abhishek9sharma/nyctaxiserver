import os
configdir = os.path.abspath(os.path.dirname(__file__))

SVC_ACCNT_PROJECT_NAME = "premium-carving-90315"


datetime_formats = {
                     'date_only' : "%Y-%m-%d"
                   }


DATABASE_CONFIG = {
    
                    'big_query_keys':{
                        'bqconfig':os.path.join (configdir,'bqconfig.json'),
                        'yourkey':os.path.join (configdir,'enteryourkey.json'),
                        
                    },

                    'datasets':{

                        'bigquery-public-data':{
                            'datasets':{
                                'new_york_taxi_trips':{
                                    'tables':[
                                        'tlc_green_trips_2014',
                                        'tlc_green_trips_2015',
                                         'tlc_green_trips_2016',
                                         'tlc_green_trips_2017',
                                         'tlc_yellow_trips_2015',
                                         'tlc_yellow_trips_2016',
                                         'tlc_yellow_trips_2017',
                                    ]
                                }
                            }
                        },

                        'yourproject': {
                            'datasets': {
                                'yourdatabase': {
                                    'tables': [
                                        'yourtable1',
                                        'yourtable2'

                                    ]
                                }
                            }
                        }

                    }

                }


API_CONFIG = {
               
               'total_trips' : {
                                'bq_key':'bqconfig', 
                                'datetimeformat' : "%Y-%m-%d",
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014', '2015', '2016', '2017'],
                                'caching_enabled' : True,
                                'cache_info':{
                                               'all_trips_by_date':{ 
                                                                     'projectname': SVC_ACCNT_PROJECT_NAME, 
                                                                     'dataset' : 'nyctaxicache' ,
                                                                     'table' : 'total_trips_by_date_cache'}
                                                                    }
                                            },
               'avg_speed24h' : {
                                'bq_key':'bqconfig', 
                                'main_data_project': 'bigquery-public-data',
                                'datetimeformat' : "%Y-%m-%d",
                                'table_filter' : ['2014','2015', '2016'],
                                'caching_enabled' : True,
                                'cache_info':{
                                               'total_distance_time_by_ts':{ 
                                                                            
                                                                            'projectname': SVC_ACCNT_PROJECT_NAME, 
                                                                            'dataset' : 'nyctaxicache' ,
                                                                            'table' : 'total_distance_time_cache'}
                                                                           }
                                },
 
               'avg_fare_S2ID' : {
                                'bq_key':'bqconfig', 
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014'],
                                'datetimeformat' : "%Y-%m-%d",
                                }
 

             }
