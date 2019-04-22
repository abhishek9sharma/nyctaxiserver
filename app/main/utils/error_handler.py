from werkzeug.exceptions import  default_exceptions

error_dict = {

                'ModelConnectionErrorDB': 'The service is currently facing some issues connecting to database please try again later',
                'ModelConnectionErrorConfig': 'The service is currently facing some issues please try again later',
                'ModelConnectionErrorGeneral': 'The service is currently DOWN please try again later',

             }




def isConfigException(exception):
    """This method tries to check if the Exception was raised by the local API code (mostly while reading configuration)"""

    errorList = [ValueError, KeyError, FileNotFoundError]
    if type(exception) in errorList:
        return  True
    else:
        return  False


def isGoogleBigQueryException(exception):
    """This method tries to check if the Exception was raised while doing an operation using big query API"""

    try:
        if 'google.api' in str(type(exception)) or 'https://www.googleapis.com/bigquery' in exception:
            return True

        else:
            return  False
    except:
        return  False


def isFlaskException(exception):

    if type(exception) in default_exceptions.values():
        return True
    else:
        return False

def endpoint_exception_handler(exception_passed):
    """This method handles the exception raised  while processing a request at the endpoints"""

    try:
        if isFlaskException(exception_passed):
            try:
                return  exception_passed.code, exception_passed.data['message']
            except:
                return exception_passed.code, "Invalid request please check the request format/paramaeters"

        elif isConfigException(exception_passed):
           return 400,error_dict['ModelConnectionErrorConfig']
        elif isGoogleBigQueryException(exception_passed):
        
            try:
                error_code_from_msg = str(exception_passed).split(' ')[0]
                #if 'Not found: Project' in str(model_exception):
                return int(error_code_from_msg), error_dict['ModelConnectionErrorDB']
            except:
                return 400, error_dict['ModelConnectionErrorConfigDB']
    except:
            return 400, error_dict['ModelConnectionErrorGeneral']






