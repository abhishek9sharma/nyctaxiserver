import unittest
from app import APIServer
import json
import os

class TotaTripsByDateTestCase(unittest.TestCase):

    def setUp(self):
        self.testserver = APIServer('testing')
        self.client = self.testserver.app.test_client
        self.testdir = os.path.abspath(os.path.dirname(__file__))


   # tests for dates as integers
    def test_bad_request_start_number(self):
        
        """Test for invalid start date (integer) returns a  400 error response."""
        
        query_string_param1 = 'start=1'
        query_string_param2 = 'end=2017-01-01'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_end_number(self):
        
        """Test for invalid end date (integer) returns a  400 error response."""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
    
    def test_bad_request_both_numbers(self):
        
        """Test for invalid dates (both dates as integers) returns a  400 error response."""
        
        query_string_param1 = 'start=1'
        query_string_param2 = 'end=2'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    #tests for dates as invalid strings
    def test_bad_request_start_string(self):
        
        """Test for invalid start date (string) returns a  400 error response."""
        
        query_string_param1 = 'start=2017/01/01'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017/01/01, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_end_string(self):
        
        """Test for invalid end date (string) returns a  400 error response."""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017/01/31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017/01/31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
    
    def test_bad_request_both_string(self):
        
        """Test for invalid dates (both dates as ivaid strings) returns a  400 error response."""
        
        query_string_param1 = 'start=2017/01/01'
        query_string_param2 = 'end=2017/01/31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017/01/01, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
   
   # tests for dates as invalid dates
    def test_bad_request_start_date_format_A(self):
        
        """Test for invalid start date YYYY-MM-D returns a  400 error response."""
        
        query_string_param1 = 'start=2017-01-1'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017-01-1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
 
    def test_bad_request_start_date_format_B(self):
        
        """Test for invalid start date YYYY-M-DD returns a  400 error response"""
        
        query_string_param1 = 'start=2017-1-11'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017-1-11, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_start_date_format_C(self):
        
        """Test for invalid start date YYYY-MM-DD (DD>31) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-01-32'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017-01-32, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_start_date_format_D(self):
        
        """Test for invalid start date YYYY-MM-DD (MM>12) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-13-31'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017-13-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_start_date_format_E(self):
        
        """Test for invalid start date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-02-30'
        query_string_param2 = 'end=2017-01-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for start parameter having value --> 2017-02-30, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_end_date_Format_A(self):
        
        """Test for invalid end date YYYY-MM-D returns a  400 error response."""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-02-1'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017-02-1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
 
    def test_bad_request_end_date_Format_B(self):
        
        """Test for invalid end date YYYY-M-DD returns a  400 error response"""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-1-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017-1-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_end_date_Format_C(self):
        
        """Test for invalid end date YYYY-MM-DD (DD>31) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-01-32'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017-01-32, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_end_date_Format_D(self): 
        
        """Test for invalid end date YYYY-MM-DD (MM>12) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-13-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017-13-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
    
    def test_bad_request_end_date_format_E(self):
        
        """Test for invalid end date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-04-31'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for end parameter having value --> 2017-04-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    #tests for start dates greate than end date
    def test_bad_request_both_dates_end_less_than_start(self):
        
        """Test for invalid dates start date is greater than end date returns a  400 error response."""
        
        query_string_param1 = 'start=2017-01-02'
        query_string_param2 = 'end=2017-01-01'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid DATE RANGE, start date : 2017-01-02 should be less than end date: 2017-01-01"}
        assert response.status_code == 400

    #tests for start date equal to end date
    def test_valid_request_both_dates_equal(self):
        
        """Test for valid dates (both dates as are same) returns a  200 response."""
        
        query_string_param1 = 'start=2017-01-01'
        query_string_param2 = 'end=2017-01-01'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"data": [
                                                       {
                                                        "date": "2017-01-01",
                                                        "total_trips": 322201
                                                       }
                                                    ]
                                            }
        assert response.status_code == 200

   #tests for valid start and end date
    def test_valid_request_both_dates_2014_Jan_Feb(self):
        
        """est for valid dates for year 2014 Jan Feb returns a  200  response."""
        
        query_string_param1 = 'start=2014-01-30'
        query_string_param2 = 'end=2014-02-02'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2014_Jan_Feb.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200
 
    def test_valid_request_both_dates_2016_Feb_Mar(self):
        
        """Test for valid dates for year 2016 Feb Mar returns a  200  response."""
        
        query_string_param1 = 'start=2016-02-27'
        query_string_param2 = 'end=2016-03-03'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2016_Feb_Mar.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200
 
    def test_valid_request_both_dates_2015_March(self):
        
        """Test for valid dates for year 2015 March returns a  200  response."""
        
        query_string_param1 = 'start=2015-03-04'
        query_string_param2 = 'end=2015-03-10'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2015_March.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200
  
    
    def test_valid_request_both_dates_2017_Apr_May(self):
        
        """Test for valid dates for year 2017 Apr May returns a  200  response."""
        
        query_string_param1 = 'start=2017-04-26'
        query_string_param2 = 'end=2017-05-01'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2017_Apr_May.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200


    def test_valid_request_both_dates_2014_May(self):
        
        """Test for valid dates for year 2014 May start returns a  200  response."""
        
        query_string_param1 = 'start=2014-05-11'
        query_string_param2 = 'end=2014-05-15'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2014_May.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200


    def test_valid_request_both_dates_2015_June_Sep(self):
        
        """Test for valid dates for year 2015 June Sep start returns a  200  response."""
        
        query_string_param1 = 'start=2015-07-21'
        query_string_param2 = 'end=2015-09-26'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'total_trips'
        test_datafile = '2015_June_Sep.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200


    


        def test_valid_request_both_dates_2016_Oct_2017_Jan(self):
        
            """Test for valid dates for year 2014 June July start returns a  200  response."""
            
            query_string_param1 = 'start=2016-10-31'
            query_string_param2 = 'end=2017-01-01'
            test_data_dir_main = 'test_data'
            test_data_dir_api = 'total_trips'
            test_datafile = '2016_Oct_2017_Jan.json'
            test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
            test_json = json.load(test_data_file_resource)         
            test_data_file_resource.close()
            response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
            assert json.loads(response.data.decode('utf-8')) == test_json
            assert response.status_code == 200


   
    #tests for valid empty result
    def test_valid_request_both_dates__not_present(self):
        
        """Test for valid dates both dates not present in table returns a  200  response."""
        
        query_string_param1 = 'start=2019-04-01'
        query_string_param2 = 'end=2019-04-18'
        response = self.client().get('/total_trips/?' +  query_string_param1 + '&' + query_string_param2)
        assert json.loads(response.data.decode('utf-8')) == {"message": "No records found for the given date range : 2019-04-01 --> 2019-04-18"}
        assert response.status_code == 404

if __name__ == "__main__":
    unittest.main()
