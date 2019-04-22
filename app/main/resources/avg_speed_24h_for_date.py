from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avg_speed_24h_for_date_schema import AvgFare24HForDate
from app.main.service.avg_speed24h_for_date_svc import AvgFare24HForDateSvc
from app.main.utils.validation_helper import *
from app.configuration.dbconfig import API_CONFIG
from app.main.utils.error_handler import endpoint_exception_handler
from app.main.utils.logging_helper import *



avg_speed_24h_for_date_ns = AvgFare24HForDate.ns
avg_speed_24h_for_date_model = AvgFare24HForDate.model
avg_speed_24h_for_date_parser = AvgFare24HForDate.parser
        

@avg_speed_24h_for_date_ns.route('/')
class AvgFare24HForDateList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """
    logger_local = None
    
    @avg_speed_24h_for_date_ns.expect(avg_speed_24h_for_date_parser, validate = True)
    @avg_speed_24h_for_date_ns.marshal_with(avg_speed_24h_for_date_model, envelope = 'data')
    def get(self):
        
        #Intialize Logger 
        if self.logger_local is None:
            self.logger_local = set_logger(self.__class__.__name__)
            
        try:
            #Get query parameters
            self.logger_local.info("Recieved request : " + str(request))
            query_string_data = avg_speed_24h_for_date_parser.parse_args(request)
            input_date = query_string_data['date']
 
            #Load config values
            api_name = 'avg_speed24h'
            datetime_format = API_CONFIG[api_name]['datetimeformat'] 
 

            #Validate query parameters
            if input_date and not(isvalid_datetime_format(input_date, datetime_format)):
                msg = 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD'
                abort(400, msg)

            #Fetch data using service
            self.logger_local.info("For request :" + str(request) + " querying big query for data" )
            avg_speed_24h_for_date_svc = AvgFare24HForDateSvc()
            avg_speed_24h_for_date = avg_speed_24h_for_date_svc.get_data(input_date)
            if avg_speed_24h_for_date:
                self.logger_local.info("Data for request :" + str(request) + " successfully fetched sending back to client" )
                return avg_speed_24h_for_date
 
            msg =  'No records found for the given date  : '  + str(input_date)
            abort(404,msg)
    
        except Exception as e:
            self.logger_local.info("For request :" + str(request) + " following exception occured ::" + str(e))
            error_status, error_message = endpoint_exception_handler(e)
            abort(int(error_status), error_message)            
            
        
 
 