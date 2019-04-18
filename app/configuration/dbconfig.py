import os
configdir = os.path.abspath(os.path.dirname(__file__))

DATABASE_CONFIG = {
    
                    'big_query_keys':{
                        'gh':os.path.join (configdir,'nyctaxiserver-237905-b3c84f805ff7-gh.json'),
                        'org':os.path.join (configdir,'bqconfig.json'),
                        'yourkey':os.path.join (configdir,'enteryourkey.json'),
                        
                    },

                    'datasets':{
                        
                        'bigquery-public-data':{
                            'databases':{
                                'new_york_taxi_trips':{
                                    'tables':[
                                        'tlc_green_trips_2014',
                                        'tlc_green_trips_2015'
                                        #'tlc_green_trips_2016',
                                        #'tlc_green_trips_2017'
                                        #'tlc_yellow_trips_2014',
                                        #'tlc_yellow_trips_2015'
                                        #'tlc_yellow_trips_2016',                    
                                    ]
                                }
                            }
                        },
                        
                        'nyctaxiserver-237905':{
                            'databases':{
                                'nyctaxicached':{
                                    'tables':[
                                        'total_trips_by_date'
                                    ]
                                }
                            }
                        },

                        'gh2nu-904': {
                            'databases': {
                                'taxiinfo': {
                                    'tables': [
                                        'total_trips_by_date'
                                    ]
                                }
                            }
                        },
                        
                        'yourproject': {
                            'databases': {
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
               
               'total_trips'   : {'bq_key':'gh', 'dataset': 'bigquery-public-data','cache':{'dataset': 'nyctaxiserver-237905', 'tablename':'total_trips_by_date_cache', 'dbname' : 'nyctaxicached_A'}}
            #    'avg_fare'      : {'bq_key':'org', 'dataset': 'bigquery-public-data', 'cache':{'tablename':'total_fare_by_date_lat_long', 'dbname' : 'nyctaxicached'}},
            #    'avg_speed_24h' : {'bq_key':'org', 'dataset': 'bigquery-public-data', 'cache':{'tablename':'total_speed_by_date', 'dbname' : 'nyctaxicached   '}}
               
             }
