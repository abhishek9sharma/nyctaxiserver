import s2sphere 

# The .so file build for S2Geometry does not load sometimes so have put it into a try catch block
try:
    import app.main.utils.S2Lib.pywraps2 as s2google
    print("Successfuly loaded google  will be using it for s2id computation")
except:
    print("Could not load google S2Geometry will be using s2sphere for s2id computation")
    pass


def compute_s2id_from_lat_long_s2sphere(latitude,longitude, required_level = 16):
    """This method computes the s2id for a latitude logitude pair at a provided level based on the the s2sphere library"""

    # get cell for current latittude longitude pair
    curr_point = s2sphere.LatLng.from_degrees(latitude, longitude)
    curr_cell = s2sphere.CellId.from_lat_lng(curr_point)

    # get cell id for the current cell
    curr_level_ptr = curr_cell.level()
    curr_cell_ptr = curr_cell

    # iterate till s2id for level 16 found
    while curr_level_ptr != required_level:
        curr_cell_ptr = curr_cell_ptr.parent()
        curr_level_ptr = curr_cell_ptr.level()


    return curr_cell_ptr.to_token()

    
def compute_s2id_from_lat_long_s2google(latitude, longitude, required_level=16):
    """This method computes the s2id  for a latitude logitude pair at a provided level based on the the S2Geometry library"""

    # get cell for current latittude longitude pair
    curr_point = s2google.S2LatLng.FromDegrees(latitude, longitude)
    curr_cell = s2google.S2CellId(curr_point)

    # get cell id for the current cell
    curr_level_ptr = curr_cell.level()
    curr_cell_ptr = curr_cell

   # iterate till s2id for level 16 found
    while curr_level_ptr != required_level:
        curr_cell_ptr = curr_cell_ptr.parent()
        curr_level_ptr = curr_cell_ptr.level()

    return curr_cell_ptr.ToToken()
