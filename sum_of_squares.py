import math

def sum_of_squares(n):
	return sum([i**2 for i in range(1, math.floor(n) + 1)])


def calc_distance(x1,y1,x2,y2): 
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

d = calc_distance(0,0,15,10)
print("Distance: {}".format(d))
print("Sum of Squares: {}".format(sum_of_squares(d)))