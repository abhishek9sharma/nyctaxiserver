import unittest
from app import APIServer
import json
import os

class AvgSpeed24HForDateTestCase(unittest.TestCase):

    def setUp(self):
        self.testserver = APIServer('testing')
        self.client = self.testserver.app.test_client
        self.testdir = os.path.abspath(os.path.dirname(__file__))


   #tests for dates as invalid dates
    def test_bad_request_date_number(self):
        
        """Test for invalid date (integer) returns a  400 error response."""
        
        query_string_param1 = 'date=1'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

   
    def test_bad_request_date_string(self):
        
        """Test for invalid date (string) returns a  400 error response."""
        
        query_string_param1 = 'date=2017/01/01'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017/01/01, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

     
    def test_bad_request_date_date_format_A(self):
        
        """Test for invalid date YYYY-MM-D returns a  400 error response."""
     
        query_string_param1 = 'date=2017-01-1'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-01-1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400
 

    def test_bad_request_date_date_format_B(self):
        
        """Test for invalid date YYYY-M-DD returns a  400 error response"""
        
        query_string_param1 = 'date=2017-1-11'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-1-11, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_C(self):
        
        """Test for invalid date YYYY-MM-DD (DD>31) returns a  400 error response"""
        
        query_string_param1 = 'date=2017-01-32'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-01-32, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_D(self):
        
        """Test for invalid date YYYY-MM-DD (MM>12) returns a  400 error response"""
        
        query_string_param1 = 'date=2017-13-31'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-13-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_E(self):
        
        """Test for invalid date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""
        
        query_string_param1 = 'date=2017-02-30'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-02-30, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

   
   # tests for valid date 
    def test_valid_request_date_2017_Jan(self):
        
        """Test for valid dates returns a  200  response."""
        
        query_string_param1 = 'date=2017-01-01'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {
                                                "data": [
                                                    {
                                                    "average_speed": 0.7017676092
                                                    }
                                                ]
                                            }
        assert response.status_code == 200


    def test_valid_request_date_2016_Feb(self):
        
        """Test for valid dates returns a  200  response."""
        
        query_string_param1 = 'date=2016-02-29'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {
                                                "data": [
                                                    {
                                                    "average_speed": 11.7515114652
                                                    }
                                                ]
                                            }
        assert response.status_code == 200



    def test_valid_request_date_2015_Aug(self):
        
        """Test for valid dates returns a  200  response."""
        
        query_string_param1 = 'date=2015-08-12'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {
                                                "data": [
                                                    {
                                                    "average_speed": 27.0399171853
                                                    }
                                                ]
                                            }
        assert response.status_code == 200


    def test_valid_request_date_2015_Jan(self):
        
        """Test for valid dates returns a  200  response."""
        
        query_string_param1 = 'date=2015-01-15'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {
                                                "data": [
                                                    {
                                                    "average_speed": 12.0676661674
                                                    }
                                                ]
                                            }
        assert response.status_code == 200



    #tests for valid empty result
    def test_valid_request_date__not_present(self):
        
        """Test for valid dates both dates not present in table returns a  200  response."""
        
        query_string_param1 = 'date=2019-04-01'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "No records found for the given date  : 2019-04-01"}
        assert response.status_code == 404

    def test_valid_request_date__not_present_2017(self):
        
        """Test for valid dates both dates not present in table returns a  200  response."""
        
        query_string_param1 = 'date=2017-09-02'
        response = self.client().get('/average_speed_24hrs/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "No records found for the given date  : 2017-09-02"}
        assert response.status_code == 404

if __name__ == "__main__":
    unittest.main()
