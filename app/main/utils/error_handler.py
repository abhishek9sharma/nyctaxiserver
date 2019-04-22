


error_dict = {

                'ModelConnectionErrorDB': 'The service is currently facing some issues connecting to database please try again later',
                'ModelConnectionErrorConfig': 'The service is currently facing some issues please try again later',
                'ModelConnectionErrorGeneral': 'The service is currently DOWN please try again later',

             }




def isConfigException(exception):

    errorList = [ValueError, KeyError, FileNotFoundError]
    if type(exception) in errorList:
        return  True
    else:
        return  False


def isGoogleBigQueryException(exception):

    try:
        if 'google.api' in str(type(exception)) or 'https://www.googleapis.com/bigquery' in exception:
            return True

        else:
            return  False
    except:
        return  False


def model_exception_handler(model_exception):

    try:
        if isConfigException(model_exception):
           return 400,error_dict['ModelConnectionErrorConfig']
        elif isGoogleBigQueryException(model_exception):
        
            try:
                error_code_from_msg = str(model_exception).split(' ')[0]
                #if 'Not found: Project' in str(model_exception):
                return int(error_code_from_msg), error_dict['ModelConnectionErrorDB']
            except:
                return 400, error_dict['ModelConnectionErrorConfigDB']
    except:
            return 400, error_dict['ModelConnectionErrorGeneral']






