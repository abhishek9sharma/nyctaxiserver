from flask_restplus import Namespace, fields, reqparse

class AvgFare24HForDate:
   
    """ Schema for Average Speed for 24 hours preceding a given date """
   
    ns = Namespace('avg_speed_24hrs_for_date', 'Average Speed for 24 hours preceding a given date')
    model = ns.model('avg_speed_24hrs_for_date', {
                                                           'average_speed': fields.Float(required= True, description = 'average speed in miles per hour in the period 24 hours before the given date')
                                                          
                                                          })

    parser = reqparse.RequestParser(bundle_errors= True)
    parser.add_argument('date', type = str, required= True, help = 'Example: 2017-01-01 (DDDD-MM-YY)', location = 'args')
    
