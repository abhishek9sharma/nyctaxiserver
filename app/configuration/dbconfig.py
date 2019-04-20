import os
configdir = os.path.abspath(os.path.dirname(__file__))

datetime_formats = {
                     'date_only' : "%Y-%m-%d"
                   }
DATABASE_CONFIG = {
    
                    'big_query_keys':{
                        'gh':os.path.join (configdir,'nyctaxiserver-237905-b3c84f805ff7-gh.json'),
                        'org':os.path.join (configdir,'bqconfig.json'),
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

                        'nyctaxiserver-237905':{
                            'datasets':{
                                'nyctaxicached':{
                                    'tables':[
                                        'total_trips_by_date'
                                    ]
                                                },

                                'nyctaxicached_new':{
                                    'tables':[
                                        'total_trips_by_date'
                                    ]

                                }
                            }
                        },

                        'gh2nu-904': {
                            'datasets': {
                                'taxiinfo': {
                                    'tables': [
                                        'total_trips_by_date'
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
                                'bq_key':'gh', 
                                'datetimeformat' : "%Y-%m-%d",
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014', '2015', '2016', '2017'],
                                'caching_enabled' : True,
                                'cache_info':{
                                               'all_trips_by_date':{ 
                                                                     'projectname': 'nyctaxiserver-237905', 
                                                                     'dataset' : 'nyctaxicache3' ,
                                                                     'table' : 'total_trips_by_date_cache'}
                                                                    }
                                            },
               'avg_speed24h' : {
                                'bq_key':'gh', 
                                'main_data_project': 'bigquery-public-data',
                                'datetimeformat' : "%Y-%m-%d",
                                'table_filter' : ['2014','2015', '2016'],
                                'caching_enabled' : True,
                                'cache_info':{
                                               'total_distance_time_by_ts':{ 
                                                                     'projectname': 'nyctaxiserver-237905', 
                                                                     'dataset' : 'nyctaxicache3' ,
                                                                     'table' : 'total_distance_time_cache'}
                                                                    }
                                },
 
               'avg_fare_S2ID' : {
                                'bq_key':'gh', 
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014'],
                                'datetimeformat' : "%Y-%m-%d",
                                # 'caching_enabled' : False,
                                # 'cache_info':{
                                #                'tot_fare_by_date_location':{
                                #                                      'projectname': 'nyctaxiserver-237905', 
                                #                                      'dataset' : 'nyctaxicache3' ,
                                #                                      'table' : 'tot_fare_by_date_location_cache'}
                                #                                     }
                                            }
 

             }
