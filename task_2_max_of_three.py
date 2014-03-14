def max_of_three(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > y and z > x:
        return z

print 9 == max_of_three(5, 3, 9)