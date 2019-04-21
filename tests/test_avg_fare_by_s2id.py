import unittest
from app import APIServer
import json
import  os

class AvgFareByS2IDTestCase(unittest.TestCase):

    def setUp(self):
        self.testserver = APIServer('testing')
        self.client = self.testserver.app.test_client
        self.testdir = os.path.abspath(os.path.dirname(__file__))


   # tests for dates as invalid dates
    def test_bad_request_date_number(self):

        """Test for invalid date (integer) returns a  400 error response."""

        query_string_param1 = 'date=1'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400


    def test_bad_request_date_string(self):

        """Test for invalid date (string) returns a  400 error response."""

        query_string_param1 = 'date=2017/01/01'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017/01/01, expected format is YYYY-MM-DD"}
        assert response.status_code == 400


    def test_bad_request_date_date_format_A(self):

        """Test for invalid date YYYY-MM-D returns a  400 error response."""

        query_string_param1 = 'date=2017-01-1'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-01-1, expected format is YYYY-MM-DD"}
        assert response.status_code == 400


    def test_bad_request_date_date_format_B(self):

        """Test for invalid date YYYY-M-DD returns a  400 error response"""

        query_string_param1 = 'date=2017-1-11'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-1-11, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_C(self):

        """Test for invalid date YYYY-MM-DD (DD>31) returns a  400 error response"""

        query_string_param1 = 'date=2017-01-32'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-01-32, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_D(self):

        """Test for invalid date YYYY-MM-DD (MM>12) returns a  400 error response"""

        query_string_param1 = 'date=2017-13-31'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-13-31, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

    def test_bad_request_date_date_format_E(self):

        """Test for invalid date YYYY-MM-DD (wrong date month combination) returns a  400 error response"""

        query_string_param1 = 'date=2017-02-30'
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == {"message": "Invalid format for date parameter having value --> 2017-02-30, expected format is YYYY-MM-DD"}
        assert response.status_code == 400

      # tests for valid date

    def test_valid_request_2014(self):

        """Test for valid dates year  2014  response."""

        query_string_param1 = 'date=2014-01-01'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'avg_fare_bys2id'
        test_datafile = '2014_Jan_01.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200

    def test_valid_request_2015(self):

        """Test for valid dates year  2015  response."""

        query_string_param1 = 'date=2015-12-25'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'avg_fare_bys2id'
        test_datafile = '2015_Dec_25.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200

    def test_valid_request_2016(self):

        """Test for valid dates year  2016  response."""

        query_string_param1 = 'date=2016-02-29'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'avg_fare_bys2id'
        test_datafile = '2016_Feb_29.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))         
        test_json = json.load(test_data_file_resource)         
        test_data_file_resource.close()
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200


    def test_valid_request_2015(self):

        """Test for valid dates year  2016  response."""

        query_string_param1 = 'date=2015-12-31'
        test_data_dir_main = 'test_data'
        test_data_dir_api = 'avg_fare_bys2id'
        test_datafile = '2015_Dec_31.json'
        test_data_file_resource = open(os.path.join(self.testdir,test_data_dir_main, test_data_dir_api, test_datafile))
        test_json = json.load(test_data_file_resource)
        test_data_file_resource.close()
        response = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(response.data.decode('utf-8')) == test_json
        assert response.status_code == 200


    def test_valid_request_2017_New(self):

        """Test for valid dates year  2017  response."""

        query_string_param1 = 'date=2017-12-31'
        responsemsg = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(responsemsg.data.decode('utf-8')) == {"message": "No records found for the given date  : 2017-12-31"}
        assert responsemsg.status_code == 404


    #tests for valid empty result
    def test_valid_request_date_not_present_s2id(self):
        
        """Test for valid dates both dates not present in table returns a  200  response."""
        
        query_string_param1 = 'date=2019-04-01'
        responsemsg = self.client().get('/average_fare_heatmap/?' +  query_string_param1)
        assert json.loads(responsemsg.data.decode('utf-8')) == {"message": "No records found for the given date  : 2019-04-01"}
        assert responsemsg.status_code == 404

if __name__ == "__main__":
    unittest.main()
