from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avg_speed_24h_for_date_schema import AvgFare24HForDate
from app.main.service.avg_speed24h_for_date_svc import AvgFare24HForDateSvc
from app.main.utils.validation_helper import *
from app.configuration.dbconfig import API_CONFIG
from app.main.utils.error_handler import model_exception_handler


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

    @avg_speed_24h_for_date_ns.expect(avg_speed_24h_for_date_parser, validate = True)
    @avg_speed_24h_for_date_ns.marshal_with(avg_speed_24h_for_date_model, envelope = 'data')
    def get(self):
        
        query_string_data = avg_speed_24h_for_date_parser.parse_args(request)
        input_date = query_string_data['date']
        
        try:
            api_name = 'avg_speed24h'
            datetime_format = API_CONFIG[api_name]['datetimeformat'] 
        except Exception as e:
           error_status, error_message = model_exception_handler(e)
           abort(int(error_status), error_message)


        try:
            if input_date and not(isvalid_datetime_format(input_date, datetime_format)):
                abort(400, 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD')
                #return {"message":"Invalid format for start parameter value : " + str(input_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
        except Exception as e:
            abort(400, 'Invalid format for date parameter having value --> ' + str(
                input_date) + ', expected format is YYYY-MM-DD')

        try:
            avg_speed_24h_for_date_svc = AvgFare24HForDateSvc()
            avg_speed_24h_for_date = avg_speed_24h_for_date_svc.get_data(input_date)
            if avg_speed_24h_for_date:
                return avg_speed_24h_for_date
        except Exception as e:
           error_status, error_message = model_exception_handler(e)
           abort(int(error_status), error_message)

        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date  : '  + str(input_date))
 
 