import Adams

def create_point(location,part_name,name):
    """
    Create a point on current model
    
    Parameters
    ----------
    location: list
        Location for point
    
    part_name: str
        Name of the part where the point will be located
    
    name: str
        Name of the point
    """
    model = Adams.getCurrentModel()
    point = model.Parts[part_name].DesignPoints.create(name=name, location=location)
    return point

def create_point_on_ground(location,name):
    model = Adams.getCurrentModel()
    point = model.ground_part.DesignPoints.create(name=name, location=location)
    return point
    
def create_points(name_location, part_name):
    # model = Adams.getCurrentModel()
    points = []
    for name, location in name_location.items():
        points.append( create_point(location,part_name,name) )
    return points

def create_marker(location,part_name,name):
    model = Adams.getCurrentModel()
    marker  = model.Parts[part_name].Markers.create(name= name, location=location, name_visibility="off")
    return marker
    
    