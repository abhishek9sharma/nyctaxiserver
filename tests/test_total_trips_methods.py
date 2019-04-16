# import json


# #tests for dates as integers
# def test_bad_request_start_number(client):
    
#     """Test for invalid start date (integer) returns a  400 error response."""
    
#     query_string_param1 = 'start=1'
#     query_string_param2 = 'end=2017-01-01'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 1, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_number(client):
    
#     """Test for invalid end date (integer) returns a  400 error response."""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_both_numbers(client):
    
#     """Test for invalid dates (both dates as integers) returns a  400 error response."""
    
#     query_string_param1 = 'start=1'
#     query_string_param2 = 'end=2'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 1, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# #tests for dates as invalid strings
# def test_bad_request_start_string(client):
    
#     """Test for invalid start date (string) returns a  400 error response."""
    
#     query_string_param1 = 'start=2017/01/01'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017/01/01, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_string(client):
    
#     """Test for invalid end date (string) returns a  400 error response."""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017/01/31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017/01/31, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_both_string(client):
    
#     """Test for invalid dates (both dates as ivaid strings) returns a  400 error response."""
    
#     query_string_param1 = 'start=2017/01/01'
#     query_string_param2 = 'end=2017/01/31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017/01/01, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# # tests for dates as invalid dates
# def test_bad_request_start_date_format_A(client):
    
#     """Test for invalid start date YYYY-MM-D returns a  400 error response."""
    
#     query_string_param1 = 'start=2017-01-1'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017-01-1, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_start_date_format_B(client):
    
#     """Test for invalid start date YYYY-M-DD returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-1-11'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017-1-11, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_start_date_format_C(client):
    
#     """Test for invalid start date YYYY-MM-DD (DD>31) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-01-32'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017-01-32, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_start_date_format_D(client):
    
#     """Test for invalid start date YYYY-MM-DD (MM>12) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-13-31'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017-13-31, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_start_date_format_E(client):
    
#     """Test for invalid start date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-02-30'
#     query_string_param2 = 'end=2017-01-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for start parameter value : 2017-02-30, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_date_Format_A(client):
    
#     """Test for invalid end date YYYY-MM-D returns a  400 error response."""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-02-1'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017-02-1, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_date_Format_B(client):
    
#     """Test for invalid end date YYYY-M-DD returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-1-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017-1-31, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_date_Format_C(client):
    
#     """Test for invalid end date YYYY-MM-DD (DD>31) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-01-32'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017-01-32, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_date_Format_D(client): 
    
#     """Test for invalid end date YYYY-MM-DD (MM>12) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-13-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017-13-31, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# def test_bad_request_end_date_format_E(client):
    
#     """Test for invalid end date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-04-31'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid format for end parameter value : 2017-04-31, expected format is YYYY-MM-DD"}
#     assert response.status_code == 400

# #tests for start dates greate than end date
# def test_bad_request_both_dates_end_less_than_start(client):
    
#     """Test for invalid dates start date is greater than end date returns a  400 error response."""
    
#     query_string_param1 = 'start=2017-01-02'
#     query_string_param2 = 'end=2017-01-01'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"message": "Invalid DATE RANGE, start date : 2017-01-02 should be less than end date: 2017-01-01"}
#     assert response.status_code == 400

# #tests for start date equal to end date
# def test_valid_request_both_dates_equal(client):
    
#     """Test for valid dates (both dates as are same) returns a  200 response."""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-01-01'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"data": [
#                                                     {
#                                                     "date": "2017-01-01",
#                                                     "total_trips": 322201
#                                                     }
#                                                 ]
#                                         }
#     assert response.status_code == 200

# #tests for valid start and end date
# def test_valid_request_both_dates(client):
    
#     """Test for valid dates returns a  200  response."""
    
#     query_string_param1 = 'start=2017-01-01'
#     query_string_param2 = 'end=2017-01-03'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {
#                                             "data": [
#                                                 {
#                                                 "date": "2017-01-01",
#                                                 "total_trips": 322201
#                                                 },
#                                                 {
#                                                 "date": "2017-01-02",
#                                                 "total_trips": 249419
#                                                 },
#                                                 {
#                                                 "date": "2017-01-03",
#                                                 "total_trips": 309032
#                                                 }
#                                             ]
#                                         }
#     assert response.status_code == 200

# #tests for valid start and end date
# def test_valid_request_both_dates_end_date_not_present(client):
    
#     """Test for valid dates end date not present in table returns a  200  response."""
    
#     query_string_param1 = 'start=2018-04-30'
#     query_string_param2 = 'end=2019-01-03'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"data":[
#                                                     {
#                                                         "date": "2018-04-30",
#                                                         "total_trips": 4
#                                                     },
#                                                     {
#                                                         "date": "2018-05-22",
#                                                         "total_trips": 4
#                                                     }
                                                    
#                                                 ]
#                                         }
#     assert response.status_code == 200

# #tests for valid empty result
# def test_valid_request_both_dates__not_present(client):
    
#     """Test for valid dates both dates not present in table returns a  200  response."""
    
#     query_string_param1 = 'start=2019-04-01'
#     query_string_param2 = 'end=2019-01-18'
#     response = client.get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
#     assert json.loads(response.data) == {"data":[]}
#     assert response.status_code == 200

