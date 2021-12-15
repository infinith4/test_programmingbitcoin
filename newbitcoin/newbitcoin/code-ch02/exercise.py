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

# tag::exercise6[]
#==== Exercise 6

# end::exercise6[]
# tag::answer6[]
a, x1, y1 = 5, -1, -1
s = (3 * x1**2 + a) / (2 * y1)
x3 = s**2 - 2*x1
y3 = s*(x1-x3)-y1
print(x3,y3)  ##18.0 77.0

# end::answer6[]

from ecc import FieldElement
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
def on_curve(x,y):
    return y**2 == x**3 + a*x + b

print(on_curve(FieldElement(192, prime), FieldElement(105, prime)))

print(on_curve(FieldElement(17, prime), FieldElement(56, prime)))

print(on_curve(FieldElement(200, prime), FieldElement(119, prime)))

print(on_curve(FieldElement(1, prime), FieldElement(193, prime)))

print(on_curve(FieldElement(42, prime), FieldElement(99, prime)))
