from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avg_fare_by_s2id_schema import AvgFareByS2ID
from app.main.service.avg_fare_by_s2id_svc import AvgFareByS2IDServiceManager
#from app.main.service.baseservice import BaseServiceManager
from app.main.utils.validation_helper import *


avg_fare_by_s2id_ns = AvgFareByS2ID.ns
avg_fare_by_s2id_model = AvgFareByS2ID.model
avg_fare_by_s2id_parser = AvgFareByS2ID.parser
avg_fare_by_s2id_svc = AvgFareByS2IDServiceManager()
        

@avg_fare_by_s2id_ns.route('/')
class AvgFareByS2IDList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """ 

    @avg_fare_by_s2id_ns.expect(avg_fare_by_s2id_parser, validate = True)
    @avg_fare_by_s2id_ns.marshal_list_with(avg_fare_by_s2id_model, envelope = 'data')
    def get(self):
        
        query_string_data = avg_fare_by_s2id_parser.parse_args(request)
        input_date = query_string_data['date']
        
        if input_date and not(isvaliddate(input_date)):
            abort(400, 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD')
            #return {"message":"Invalid format for start parameter value : " + str(input_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
         
        avg_fare_by_s2id_list = avg_fare_by_s2id_svc.get_data(input_date, self.api.app.config.get('BQCONFIGFILE'))
        #print(avg_fare_by_s2id_list)
        if avg_fare_by_s2id_list:
            return avg_fare_by_s2id_list
        
        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date  : '  + str(input_date))
 
 