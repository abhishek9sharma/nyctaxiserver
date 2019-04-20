import s2sphere 
import app.main.utils.S2Lib.pywraps2 as s2google




def compute_s2id_from_lat_long_s2sphere(latitude,longitude, required_level = 16):

    curr_point = s2sphere.LatLng.from_degrees(latitude, longitude)
    curr_cell = s2sphere.CellId.from_lat_lng(curr_point)
    
    curr_level_ptr = curr_cell.level()
    curr_cell_ptr = curr_cell

    while curr_level_ptr != required_level:
        curr_cell_ptr = curr_cell_ptr.parent()
        curr_level_ptr = curr_cell_ptr.level()


    return curr_cell_ptr.to_token()



def compute_s2id_from_lat_long_s2google(latitude, longitude, required_level=16):
    curr_point = s2google.S2LatLng.FromDegrees(latitude, longitude)
    curr_cell = s2google.S2CellId(curr_point)

    curr_level_ptr = curr_cell.level()
    curr_cell_ptr = curr_cell

    while curr_level_ptr != required_level:
        curr_cell_ptr = curr_cell_ptr.parent()
        curr_level_ptr = curr_cell_ptr.level()

    return curr_cell_ptr.ToToken()