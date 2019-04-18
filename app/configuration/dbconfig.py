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
                            'datasets':{
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
                                'main_data_project': 'bigquery-public-data',
                                'caching_enabled' : True,
                                'cache_info':{
                                               'all_trips_by_date':{ 
                                                                     'projectname': 'nyctaxiserver-237905', 
                                                                     'dataset' : 'nyctaxicache3' ,
                                                                     'table' : 'total_trips_by_date_cache'}
                                                                    }
                                            }
               
             }
