from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avgspeed_24h_for_date_schema import AvgFare24HForDate
from app.main.service.avgspeed24h_for_date_svc import AvgFare24HForDateServiceManager
#from app.main.service.baseservice import BaseServiceManager
from app.main.utils.validation_helper import *


avgspeed_24h_for_date_ns = AvgFare24HForDate.ns
avgspeed_24h_for_date_model = AvgFare24HForDate.model
avgspeed_24h_for_date_parser = AvgFare24HForDate.parser
avgspeed_24h_for_date_svc = AvgFare24HForDateServiceManager()
        

@avgspeed_24h_for_date_ns.route('/')
class AvgFare24HForDateList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """ 

    @avgspeed_24h_for_date_ns.expect(avgspeed_24h_for_date_parser, validate = True)
    @avgspeed_24h_for_date_ns.marshal_with(avgspeed_24h_for_date_model, envelope = 'data')
    def get(self):
        
        query_string_data = avgspeed_24h_for_date_parser.parse_args(request)
        input_date = query_string_data['date']
        
        if input_date and not(isvaliddate(input_date)):
            abort(400, 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD')
            #return {"message":"Invalid format for start parameter value : " + str(input_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
         
        avgspeed_24h_for_date = avgspeed_24h_for_date_svc.get_data(input_date, self.api.app.config.get('BQCONFIGFILE'))
        #print(avgspeed_24h_for_date_list)
        if avgspeed_24h_for_date:
            return avgspeed_24h_for_date
        
        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date  : '  + str(input_date))
 
 