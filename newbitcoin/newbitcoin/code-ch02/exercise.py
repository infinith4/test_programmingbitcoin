# tag::exercise4[]
#==== Exercise 4


# end::exercise4[]
# tag::answer4[]
x1, y1 = 2, 5
x2, y2 = -1, -1
s = (y2 - y1) / (x2 - x1)
x3 = s**2 - x1 - x2
y3 = s * (x1 - x3) - y1
print(x3, y3) ##3.0 -7.0

# end::answer4[]