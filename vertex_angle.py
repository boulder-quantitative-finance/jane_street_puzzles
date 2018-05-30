def calc_angle(p0, p1, p2):
    ''' 
    calculate the angle (in degrees) for vertex p0 p1 p2 
    '''
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)
    angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
    return np.degrees(angle)
