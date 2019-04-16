from app.main.service.baseservice import BaseServiceManager

class TotalTripsByDateServiceManager(BaseServiceManager):

    def __init__(self):
        self.total_trips_by_date = None

    
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
                FROM `taxiinfo.total_trips_by_date`
                where date >=@start_date and date <=@end_date
                group by date
                order by date
                """

        totaltrips_by_date_df = self.fetch_records_from_BQ(query, dbconfig, queryparams)
        self.total_trips_by_date = eval(totaltrips_by_date_df.to_json(orient ='records'))
        return self.total_trips_by_date


