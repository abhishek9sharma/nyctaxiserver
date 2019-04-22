from flask_restplus import Resource, abort
from flask import request
from app.main.schema.total_trips_by_date_schema import TotalTripsByDate
from app.main.service.total_trips_by_date_svc import TotalTripsByDateSvc
from app.main.utils.validation_helper import *
from app.main.utils.error_handler import endpoint_exception_handler
from app.configuration.dbconfig import API_CONFIG
from app.main.utils.logging_helper import *

total_trips_by_date_ns = TotalTripsByDate.ns
total_trips_by_date_model = TotalTripsByDate.model
total_trips_by_date_parser = TotalTripsByDate.parser
        

@total_trips_by_date_ns.route('/')
class TotaltripsByDateList(Resource):
    """
       Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """

    logger_local = None

    @total_trips_by_date_ns.expect(total_trips_by_date_parser, validate = True)
    @total_trips_by_date_ns.marshal_list_with(total_trips_by_date_model, envelope = 'data')
    def get(self):

        #Intialize Logger 
        if self.logger_local is None:
            self.logger_local = set_logger(self.__class__.__name__)
            
        try:
            #Get query parameters
            self.logger_local.info("Recieved request : " + str(request))      
            query_string_data = total_trips_by_date_parser.parse_args(request)
            start_date = query_string_data['start']
            end_date = query_string_data['end']
            
            #Load config values
            api_name = 'total_trips'
            datetime_format = API_CONFIG[api_name]['datetimeformat']

            #Validate query parameters
            if start_date and not(isvalid_datetime_format(start_date, datetime_format)):
                msg = 'Invalid format for start parameter having value --> ' + str(start_date) + ', expected format is YYYY-MM-DD'
                abort(400, msg)
    
            if end_date and not(isvalid_datetime_format(end_date, datetime_format)):
                msg = 'Invalid format for end parameter having value --> ' + str(end_date) + ', expected format is YYYY-MM-DD'
                abort(400, msg)

            if get_datetime_in_specified_format(start_date, datetime_format)>get_datetime_in_specified_format(end_date, datetime_format):
                msg = 'Invalid DATE RANGE, start date : ' + str(start_date) + ' should be less than end date: ' + str(end_date)
                abort(400, msg)   

            #Fetch data using service
            self.logger_local.info("For request :" + str(request) + " querying big query for data" )
            total_trips_by_date_svc = TotalTripsByDateSvc()
            total_trips_by_date_list = total_trips_by_date_svc.get_data(start_date, end_date)
            if total_trips_by_date_list:
                self.logger_local.info("Data for request :" + str(request) + " successfully fetched sending back to client" )
                return total_trips_by_date_list
                   
            msg = 'No records found for the given date range : '  + str(start_date) + " --> " + str(end_date)
            abort(404, msg)
    

        except Exception as e:
            self.logger_local.info("For request :" + str(request) + " following exception occured ::" + str(e))
            error_status, error_message = endpoint_exception_handler(e)
            abort(int(error_status), error_message)

 
 