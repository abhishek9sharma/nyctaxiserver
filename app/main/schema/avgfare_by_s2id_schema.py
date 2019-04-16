from flask_restplus import Namespace, fields, reqparse

class AvgFareByS2ID:
   
    """ Schema for Average Fare for a S2ID """
   
    ns = Namespace('avg_fare_by_s2id', 'Average Fare Per Pick Up Location (S2ID) for Level 16')
    model = ns.model('avg_fare_by_s2id', {
                                                           's2id': fields.String(required = True, description = 's2id of location at level 16'),
                                                           'fare': fields.Float(required= True, description = 'average fare for the given S2ID location')
                                                          
                                                          })
    parser = reqparse.RequestParser(bundle_errors= True)
    parser.add_argument('date', type = str, required= True, help = 'Example: 2017-01-01 (DDDD-MM-YY)', location = 'args')
    
