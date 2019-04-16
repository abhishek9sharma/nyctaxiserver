from flask_restplus import Namespace, fields

class HTTPStatus:
    """ Schema for showing messages related to various HTTP Statuses """
    ns = Namespace('httpstatus', 'Schema for displaying http status')
    statusschema = ns.model('httpstatus', {
                                                   'message': fields.String(required = True, description = 'description of failure'),
                                                   'code': fields.Integer(required= True, description = 'HTTP error code reated to message')
                                                          
                                                 })
    
