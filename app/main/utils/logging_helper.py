import logging
import os
from datetime import datetime
from pathlib import Path


def get_currtime_str():
    """ Gets the current time in a particular format  """

    timestampformat = '%Y%m%d__%H%M%S'
    currtime_str = str(datetime.now().strftime(timestampformat))
    return currtime_str

    
def set_logger(identifier, logfolder=None):
    """ Returns a logger object """
    
    if logfolder is None:
        uniqfilename = os.path.join(str(Path(__file__).parents[1]), 'Logs', get_currtime_str() + '_' + identifier)
    else:
        uniqfilename = os.path.join(logfolder, 'Logs', get_currtime_str() + '_' + identifier)

    logger = logging.getLogger(str(uniqfilename))
    logger.setLevel(logging.INFO)
    logfilepath = uniqfilename

    handler = logging.FileHandler(logfilepath)
    logformat = logging.Formatter('%(asctime)s:%(message)s')
    handler.setFormatter(logformat)
    logger.propagate = False
    logger.addHandler(handler)
    return logger



