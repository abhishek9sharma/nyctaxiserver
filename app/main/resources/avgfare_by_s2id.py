from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avgfare_by_s2id_schema import AvgFareByS2ID
from app.main.service.avgfare_by_s2id_svc import AvgFareByS2IDServiceManager
#from app.main.service.baseservice import BaseServiceManager
from app.main.utils.validation_helper import *


avgfare_by_s2id_ns = AvgFareByS2ID.ns
avgfare_by_s2id_model = AvgFareByS2ID.model
avgfare_by_s2id_parser = AvgFareByS2ID.parser
avgfare_by_s2id_svc = AvgFareByS2IDServiceManager()
        

@avgfare_by_s2id_ns.route('/')
class AvgFareByS2IDList(Resource):
    """
    Returns the total number of trips per day in a given date range (dates inclusive)
       start: start date for the provided date range
       end: end date for the provided date range
    """ 

    @avgfare_by_s2id_ns.expect(avgfare_by_s2id_parser, validate = True)
    @avgfare_by_s2id_ns.marshal_list_with(avgfare_by_s2id_model, envelope = 'data')
    def get(self):
        
        query_string_data = avgfare_by_s2id_parser.parse_args(request)
        input_date = query_string_data['date']
        
        if input_date and not(isvaliddate(input_date)):
            abort(400, 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD')
            #return {"message":"Invalid format for start parameter value : " + str(input_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
         
        avgfare_by_s2id_list = avgfare_by_s2id_svc.get_data(input_date, self.api.app.config.get('BQCONFIGFILE'))
        #print(avgfare_by_s2id_list)
        if avgfare_by_s2id_list:
            return avgfare_by_s2id_list
        
        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date  : '  + str(input_date))
 
 