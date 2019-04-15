from flask_restplus import Api, fields
from app.main.resources.tripcounts import tripcounts_ns as total_trips
from app.configuration.config import config_by_envkey
from flask import Flask, Blueprint

class APIServer:
    """ Class used to initiate the API server based on the environment whose configuration key has been passed"""

    def __init__(self, env_selected):
        self.app = Flask(__name__)
        self.app.config.from_object(config_by_envkey[env_selected])
        #self.blueprint = Blueprint('api', __name__)
        self.api= Api (
                        app = self.app,          
                        #self.blueprint,
                        title='NYC TAXI TRIPS INFO',
                        version='0.1',
                        description= "A Web API for returning statistics related to trips made by new york taxis"
                      )
        #self.app.register_blueprint(self.blueprint)        
        self.api.add_namespace(total_trips,'/total_trips')


    def run(self):
       self.app.run()