from app.main.service.base_svc import BaseSvc

class AvgFare24HForDateServiceManager(BaseSvc):

    def __init__(self):
        self.avg_fare_by_s2id = None

    
    def get_data(self, input_date, dbconfig):
        
        """Gets the counts of trips grouped by date based on the provided date range """


        temp_locals = locals().copy()
        queryparams = {}
        for pargkey in temp_locals.keys():
            if pargkey not in ['self', 'dbconfig']:
                queryparams[pargkey] = temp_locals[pargkey]

        # query = """
        #         SELECT  * from
        #         FROM `taxiinfo.fare_table`
        #         where date = @input_date
        #         """
        #avg_fare_by_date_df = self.fetch_records_from_BQ(query, dbconfig, queryparams)
        #self.vg_fare_by_s2id = eval(totaltrips_by_date_df.to_json(orient ='records'))
        self.avg_fare_by_s2id = self.compute_avg_fare_by_s2id()
        return self.avg_fare_by_s2id


    def compute_avg_fare_by_s2id(self):
        return [{"s2id": "951977d37", "fare": 13.21}, {"s2id": "951977d40", "fare": 5.43}]

