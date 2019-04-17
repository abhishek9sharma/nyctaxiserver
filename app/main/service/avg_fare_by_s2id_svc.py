from app.main.service.base_svc import BaseServiceManager

class AvgFareByS2IDServiceManager(BaseServiceManager):

    def __init__(self):
        self.avg_speed_24hours_for_date = None

    
    def get_data(self, input_date, dbconfig):
        
        """Gets the counts of trips grouped by date based on the provided date range """


        temp_locals = locals().copy()
        queryparams = {}
        for pargkey in temp_locals.keys():
            if pargkey not in ['self', 'dbconfig']:
                queryparams[pargkey] = temp_locals[pargkey]

        # query = """
        #         SELECT  * from
        #         FROM `taxiinfo.speed_table`
        #         where date = @input_date
        #         """
        #avg_fare_by_date_df = self.fetch_records_from_BQ(query, dbconfig, queryparams)
        #self.vg_fare_by_s2id = eval(totaltrips_by_date_df.to_json(orient ='records'))
        self.avg_speed_24hours_for_date = self.compute_avg_speed_24hours_for_date()
        return self.avg_speed_24hours_for_date


    def compute_avg_speed_24hours_for_date(self):
        return [{"average_speed": 24.7}]

