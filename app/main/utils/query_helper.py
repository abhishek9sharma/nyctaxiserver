
# def legacy_query_formatter_from(dbconfig, datasetname, databases = [], tables = []):

#     """Helper method to load the dataset and tables to be queried """

#     tableliststr = ''
#     datasetinfo = dbconfig['datasets'][datasetname]

#     for dbname, dbinfo in datasetinfo['databases'].items():
#         if len(databases)==0 or (dbname in databases):
#             for tbl in dbinfo['tables']:
#                 if len(tables)==0 or (tbl in tables):
#                     tableliststr = tableliststr + ('[' + datasetname + '.' + dbname +'.' + tbl + '],')

#     return tableliststr