import  os

configdir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """A class used to store coniguration properties common across all environments"""
    DEBUG = True
    TESTING = False
    BQCONFIGFILE = os.path.join(configdir, 'bqconfig.json', )
    ERROR_404_HELP = False
    #BQCONNECTION = BQConnector(BQCONFIGFILE)


class DevelopmentConfig(BaseConfig):
    """A class used to store coniguration properties related to development environment"""
    TESTING = True
    PORT = '5001'
    SERVER_NAME="localhost:" + PORT 
    

class TestingConfig(BaseConfig):
    """A class used to store coniguration properties related to staging environment"""
    DEBUG = True
    TESTING = True
    SERVER_NAME="localhost:5000"

class ProductionConfig(BaseConfig):
    """A class used to store coniguration properties related to production environment"""
    DEBUG = False

config_by_envkey = dict(
    dev     = DevelopmentConfig,
    testing = TestingConfig,
    prod    = ProductionConfig
)

