def find_lattice_intercept(origin, radius):
    x = origin[0]
    y = origin[1]
    r_2 = pow(radius,2)
    xy_2 = pow(x,2) + pow(y,2)
    lattice_intercepts = []
    i = 0
    while i <= xy_2:
        j = 0
        while j <= xy_2:
            if (pow((i - x),2) + pow((j - y),2) == r_2):
                lattice_intercepts.append((i,j))
            j = j + 1
        i = i + 1
    return lattice_intercepts


print(find_lattice_intercept((7,7), 2))
print(find_lattice_intercept((0,10), 10))



# center: (7.5,7.5)
# radius: 2

# (x-7.5)^2 + (y-7.5)^2 = 4

# try: (7.5,9.5)

# 0 + 4