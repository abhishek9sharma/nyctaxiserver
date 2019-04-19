from flask_restplus import Resource, abort
from flask import request
from app.main.schema.avg_fare_by_s2id_schema import AvgFareByS2ID
from app.main.service.avg_fare_by_s2id_svc import AvgFareByS2IDSvc
from app.main.utils.validation_helper import *
from app.configuration.dbconfig import API_CONFIG

avg_fare_by_s2id_ns = AvgFareByS2ID.ns
avg_fare_by_s2id_model = AvgFareByS2ID.model
avg_fare_by_s2id_parser = AvgFareByS2ID.parser
avg_fare_by_s2id_svc = AvgFareByS2IDSvc()
        

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
        
        api_name = 'avg_fare_S2ID'
        datetime_format = API_CONFIG[api_name]['datetimeformat'] 

        try:
            if input_date and not(isvalid_datetime_format(input_date, datetime_format)):
                abort(400, 'Invalid format for date parameter having value --> ' + str(input_date) + ', expected format is YYYY-MM-DD')
                #return {"message":"Invalid format for start parameter value : " + str(input_date) + ", expected format is YYYY-MM-DD","code":400}, 400 
        except Exception as e:
            abort(400, 'Invalid format for one of the input parameters')

            
        avg_fare_by_s2id_list = avg_fare_by_s2id_svc.get_data(input_date)
        #print(avg_fare_by_s2id_list)
        if avg_fare_by_s2id_list:
            return avg_fare_by_s2id_list
        
        #return {'NotFOund': 'No trips found for the given date range'}, 404 
        abort(404, 'No records found for the given date  : '  + str(input_date))
 
 