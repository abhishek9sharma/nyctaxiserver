from flask_restplus import Resource, abort
from flask import request
from app.main.schema.total_trips_by_date_schema import TotalTripsByDate
from app.main.service.total_trips_by_date_svc import TotalTripsByDateServiceManager
#from app.main.service.baseservice import BaseServiceManager
from app.main.utils.validation_helper import *


total_trips_by_date_ns = TotalTripsByDate.ns
total_trips_by_date_model = TotalTripsByDate.model
total_trips_by_date_parser = TotalTripsByDate.parser
total_trips_by_date_svc = TotalTripsByDateServiceManager()
        

@total_trips_by_date_ns.route('/')
class TotaltripsByDateList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """ 

    @total_trips_by_date_ns.expect(total_trips_by_date_parser, validate = True)
    @total_trips_by_date_ns.marshal_list_with(total_trips_by_date_model, envelope = 'data')
    def get(self):
        
        query_string_data = total_trips_by_date_parser.parse_args(request)
        start_date = query_string_data['start']
        end_date = query_string_data['end']

        if start_date and not(isvaliddate(start_date)):
            abort(400, 'Invalid format for start parameter having value --> ' + str(start_date) + ', expected format is YYYY-MM-DD')
            #return {"message":"Invalid format for start parameter value : " + str(start_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
        
        if end_date and not(isvaliddate(end_date)):
            abort(400, 'Invalid format for end parameter having value --> ' + str(end_date) + ', expected format is YYYY-MM-DD')

        if getdate(start_date)>getdate(end_date):
            abort(400, 'Invalid DATE RANGE, start date : ' + str(start_date) + ' should be less than end date: ' + str(end_date))
        
        total_trips_by_date_list = total_trips_by_date_svc.get_data(start_date, end_date)
        #print(total_trips_by_date_list)
        if total_trips_by_date_list:
            return total_trips_by_date_list
        
        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date range : '  + str(start_date) + " --> " + str(end_date))
 
 