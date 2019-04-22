from datetime import datetime,date, timedelta


def isvalid_datetime_format(valtobevalidated, date_format):
    """This method checks if the argument provided is in the date_format"""
    
    try:
        if valtobevalidated == datetime.strptime(valtobevalidated, date_format).strftime(date_format):
                return True
        else:
            return  False
    except:
        return False


def get_datetime_in_specified_format(date_txt, date_format):
    """This method tries to conver the provided argument to a date time object in the date_format"""
    
    try:
        return datetime.strptime(date_txt, date_format)
    except:
        raise ValueError(" the date " + str(date_txt + "is not a valid date expected date_format is ") + date_format)


def get_datetime_string_in_specified_format(date_obj, date_format):
    """This method tries to convert the provided argument to a date time object in the date_format"""
    
    try:
        return date_obj.strftime(date_format)
    except:
        raise ValueError(" the date " + str(date_obj + "is not a valid date"))

            
def get_previous_datetime(input_dateobj, hours_behind = 0):
    """This method computes a datetime object given number of hours behind the input datetime"""

    prev_dateobj = input_dateobj - timedelta(hours = hours_behind)
    return prev_dateobj

