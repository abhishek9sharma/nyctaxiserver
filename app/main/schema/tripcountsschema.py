from flask_restplus import Namespace, fields, reqparse

class TripCountsPerDay:
    """ Schema for Trips per date """
    ns = Namespace('total_trips', 'Number of trips in a given date range')
    total_trips = ns.model('total_trips', {
                                                           'date': fields.Date(required = True, description = 'date'),
                                                           'total_trips': fields.Integer(reuired= True, description = 'number of trips on a given date')
                                                          
                                                          })
    parser = reqparse.RequestParser(bundle_errors= True)
    parser.add_argument('start', type = str, required= True, help = 'Expected format DDDD-MM-YY', location = 'args')
    parser.add_argument('end',   type = str, required= True, help = 'Expected format DDDD-MM-YY', location = 'args')

