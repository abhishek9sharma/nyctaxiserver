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


def getdate(date_txt):
    
    """ this method tries to conver the provided argument to a date time object in the format YYYY-MM--DD """
   
    try:
        return datetime.strptime(date_txt, "%Y-%m-%d")
    except:
        raise ValueError(" the date " + str(date_txt + "is not a valid date"))

            

