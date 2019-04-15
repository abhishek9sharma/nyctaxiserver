from flask_restplus import Resource
from app.main.schema.tripcountsschema import TripCountsPerDay
from flask import abort, jsonify, request

from app.main.utils.validation_helper import isvaliddate
from app.main.service.tripbydateservice import TotalTripsServiceManager
from app.main.service.baseservice import BaseServiceManager


tripcounts_ns = TripCountsPerDay.ns
tripcounts_model = TripCountsPerDay.total_trips
tripcounts_parser = TripCountsPerDay.parser

@tripcounts_ns.route('/')
class TripCountsPerDayList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """ 

    
    @tripcounts_ns.expect(tripcounts_parser, validate = True)
    @tripcounts_ns.response(400,  'Validation Error ')
    @tripcounts_ns.marshal_list_with(tripcounts_model, envelope = 'data')
    def get(self):
        query_string_data = tripcounts_parser.parse_args(request)
        
        start_date = query_string_data['start']
        end_date = query_string_data['end']

        if start_date and not(isvaliddate(start_date)):
            abort(400, 'ValueError: Invalid Date Format Expected format is YYYY-MM-DD')
            
        if end_date and not(isvaliddate(end_date)):
            abort(400, 'ValueError: Invalid Date Format Expected format is YYYY-MM-DD')

        tripdataservice = TotalTripsServiceManager()
        tripcounts_list = tripdataservice.get_data(start_date, end_date)
        #tripcounts_list =[]
        if tripcounts_list:
            return tripcounts_list
        return {'NotFOund': 'No trips found for the given date range'}, 404 
        #abort(400, 'NotFound : No trips found for the given date range')
 
 