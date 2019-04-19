
import s2sphere 




def compute_s2id_sphere_lat_long(latitude,longitude, required_level = 16):

    curr_point = s2sphere.LatLng.from_degrees(latitude, longitude)
    curr_cell = s2sphere.CellId.from_lat_lng(curr_point)
    
    curr_level_ptr = curr_cell.level()
    curr_cell_ptr = curr_cell

    while curr_level_ptr != required_level:
        curr_cell_ptr = curr_cell_ptr.parent()
        curr_level_ptr = curr_cell_ptr.level()


    return curr_cell_ptr.to_token()



