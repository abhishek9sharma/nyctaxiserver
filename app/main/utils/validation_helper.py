from datetime import datetime,date, timedelta



def isvalid_datetime_format(valtobevalidated, format):
    """ this method checks if the argument provided is in the format YYYY-MM--DD """
    
    try:
        if valtobevalidated == datetime.strptime(valtobevalidated, format).strftime(format):
                return True
        else:
            return  False
    except:
        return False


def get_datetime_in_specified_format(date_txt, format):
    """ this method tries to conver the provided argument to a date time object in the format YYYY-MM--DD """
    try:
        return datetime.strptime(date_txt, format)
    except:
        raise ValueError(" the date " + str(date_txt + "is not a valid date expected format is ") + format)


def get_datetime_string_in_specified_format(date_obj, format):
    """ this method tries to conver the provided argument to a date time object in the format YYYY-MM--DD """
    try:
        return date_obj.strftime(format)
    except:
        raise ValueError(" the date " + str(date_txt + "is not a valid date"))

            
def get_previous_datetime(input_dateobj, hours_behind = 0):
        prev_dateobj = input_dateobj - timedelta(hours = hours_behind)
        return prev_dateobj

