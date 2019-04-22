import os
configdir = os.path.abspath(os.path.dirname(__file__))





# Below dictionary stores the following configuration keys
    ## big_query_keys: Name of .json file containing the google service account key and information. 
    ## SVC_ACCNT_PROJECT_NAME: Name of the project realted to the google service account
    ## datasets: Name of various projects+datasets+tables that will be used by various API endpoints
DATABASE_CONFIG = {
    
                    'big_query_keys':{
                        'bqconfig':os.path.join (configdir,'bqconfig.json'),
                        'yourkey':os.path.join (configdir,'enteryourkey.json'),
                        
                    },
                    'SVC_ACCNT_PROJECT_NAME' : "premium-carving-90315",

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

# Below dictionary stores in dictinary the information related to various end points. 
    ## The main key (e.g. total_trips )is the API name referred inside classes.
        ### bq_key : The value is a reference to key 'big_query_keys' in DATABASE_CONFIG, specifies which service account to use for this API endpoint
        ### datetimeformat : Format of datetime the API endpoint suports
        ### main_data_project : The value is a reference to key 'datasets' in DATABASE_CONFIG, specified which dataset to query
        ### table_filter : The years corresponding to the dataset used in main_data_project. Only tables containing the year in their name are queried
        ### caching_enabled : Specifies if caching needs to be enables for some of the queries for the given dataset
        ### cache_info : Specified the project_name + dataset_name +table_name to be used for a cache

API_CONFIG = {
               
               'total_trips' : {
                                'bq_key':'bqconfig', 
                                'datetimeformat' : "%Y-%m-%d",
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014','2015', '2016', '2017'],
                                'caching_enabled' : False,
                                'cache_info':{
                                               'all_trips_by_date':{ 
                                                                     'projectname': DATABASE_CONFIG['SVC_ACCNT_PROJECT_NAME'], 
                                                                     'dataset' : 'nyctaxicache' ,
                                                                     'table' : 'total_trips_by_date_cache'}
                                                                    }
                                            },
               'avg_speed24h' : {
                                'bq_key':'bqconfig', 
                                'main_data_project': 'bigquery-public-data',
                                'datetimeformat' : "%Y-%m-%d",
                                'table_filter' : ['2014','2015', '2016'],
                                'caching_enabled' : False,
                                'cache_info':{
                                               'total_distance_time_by_ts':{ 
                                                                            
                                                                            'projectname': DATABASE_CONFIG['SVC_ACCNT_PROJECT_NAME'], 
                                                                            'dataset' : 'nyctaxicache' ,
                                                                            'table' : 'total_distance_time_cache'}
                                                                           }
                                },
 
               'avg_fare_S2ID' : {
                                'bq_key':'bqconfig',
                                'main_data_project': 'bigquery-public-data',
                                'table_filter' : ['2014','2015', '2016', '2017'],
                                'datetimeformat' : "%Y-%m-%d",
                                }
 

             }

# Dictionay to store date formats that may be used by varous APIs
datetime_formats = {
                     'date_only' : "%Y-%m-%d"
                   }
