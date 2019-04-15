from app.main.service.baseservice import BaseServiceManager

class TotalTripsServiceManager(BaseServiceManager):

    def __init__(self):
        self.trips_by_dates = []

    
    def get_data(self, start_date, end_date):
        
        """Gets the counts of trips grouped by date based on the provided date range """
        
        dummy_data = [
                        {"date":"2018-01-01","total_trips":"23294"},
                        {"date":"2018-01-02","total_trips":"23222"},
                        {"date":"2018-01-03","total_trips":"26417"},
                        {"date":"2018-01-04","total_trips":"6519"}
                    ]
        
        return dummy_data



