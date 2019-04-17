from flask_restplus import Api, fields
from app.main.resources.total_trips_by_date import total_trips_by_date_ns
from app.main.resources.avg_fare_by_s2id import avg_fare_by_s2id_ns
from app.main.resources.avg_speed_24h_for_date import avg_speed_24h_for_date_ns

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
        self.api.add_namespace(total_trips_by_date_ns,'/total_trips')
        self.api.add_namespace(avg_fare_by_s2id_ns,'/average_fare_heatmap')
        self.api.add_namespace(avg_speed_24h_for_date_ns,'/average_speed_24hrs')

    def run(self):
       self.app.run()