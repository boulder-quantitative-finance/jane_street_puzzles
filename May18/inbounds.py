import math

def inbounds(origin, distance, slope):

    x = origin[0]
    y = origin[1]
    inbounds = True

    if slope == "vertical_pos":
        if distance + y > 20:
            inbounds = False
    elif slope == "vertical_neg":
        if distance - y < 0:
            inbounds = False
    elif slope == "horizontal_pos":
        if distance + x > 20:
            inbounds = False
    elif slope == "horizontal_neg":
        if distance - x < 0:
            inbounds = False
    else:
        c = 1/math.sqrt(1+pow(slope,2))
        s = slope/math.sqrt(1+pow(slope,2))

        x1 = x+distance*c
        y1 = y+distance*s

        if x1 < 0 or x1 > 20 or y1 < 0 or y1 > 20:
            inbounds = False

    return inbounds




# toss: (0.0,0.0) => (14.0,1.0) | d:14.0357 | s:0.0714
#     g_pos_swing: (14.0,1.0) => (5.0,0.0) | d:4.9803 | g:2.2546° | s:0.1111
#     g_neg_swing: (14.0,1.0) => (7.0,1.0) | d:7.0357 | g:-4.0856° | s:horizontal_neg
#     lps: []
# ___________
# >>> p (x2,y2): (14.0, 1.0)
# >>> p distance: 14.0357
# >>> p slope: 0.1111
# >>> n (x2,y2): (14.0, 1.0)
# >>> n distance: 14.0357
# >>> n slope: horizontal_neg


print(inbounds((14.0, 1.0), 14.0357, 0.1111))
print(inbounds((14.0, 1.0), 14.0357, "horizontal_neg"))