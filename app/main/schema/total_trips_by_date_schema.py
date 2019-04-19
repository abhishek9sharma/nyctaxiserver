from flask_restplus import Namespace, fields, reqparse

class TotalTripsByDate:
    """ Schema for Total Trips in a given date range """
    ns = Namespace('totaltrips_by_date', 'Number of trips per date in a given date range')
    model = ns.model('totaltrips_by_date', {
                                                           'date': fields.Date(required = True, description = 'date'),
                                                           'total_trips': fields.Integer(required= True, description = 'number of trips on the given date')
                                                          
                                                          })
    parser = reqparse.RequestParser(bundle_errors= True)
    parser.add_argument('start', type = str, required= True, help = 'Example:  2017-01-01 (DDDD-MM-YY)', location = 'args')
    parser.add_argument('end',   type = str, required= True, help = 'Example: 2017-01-02 (DDDD-MM-YY)', location = 'args')

