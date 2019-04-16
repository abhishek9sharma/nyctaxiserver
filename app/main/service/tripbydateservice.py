from app.main.service.baseservice import BaseServiceManager

class TotalTripsServiceManager(BaseServiceManager):

    def __init__(self):
        self.trips_by_dates = []

    
    def get_data(self, start_date, end_date, dbconfig):
        
        """Gets the counts of trips grouped by date based on the provided date range """


        temp_locals = locals().copy()
        queryparams = {}
        for pargkey in temp_locals.keys():
            if pargkey not in ['self', 'dbconfig']:
                queryparams[pargkey] = temp_locals[pargkey]

        #queryparams = [ parg for parg in locals()  if parg not in ['self', 'dbconfig']]
        query = """
                SELECT  date,sum(total_trips) as total_trips
                FROM `gh2nu-904.taxiinfo.total_trips_per_day`
                where date >=@start_date and date <=@end_date
                group by date
                order by date
                """

        results_dataframe = self.fetch_records_from_BQ(query, dbconfig, queryparams)
        return eval(results_dataframe.to_json(orient ='records'))


