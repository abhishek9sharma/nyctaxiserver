from datetime import datetime,date


def isvaliddate(valtobevalidated):
    
    """ this method checks if the argument provided is in the format YYYY-MM--DD """
    try:
        if valtobevalidated == datetime.strptime(valtobevalidated, "%Y-%m-%d").strftime('%Y-%m-%d'):
                return True
        else:
            return  False
    except:
        return False
