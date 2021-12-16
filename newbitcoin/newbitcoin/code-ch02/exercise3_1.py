
from ecc import FieldElement, Point
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

import ecc
from helper import run
run(ecc.ECCTest('test_on_curve'))
run(ecc.ECCTest('test_add'))

x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)

x2 = FieldElement(num=17, prime=prime)
y2 = FieldElement(num=56, prime=prime)

a = FieldElement(0, prime)
b = FieldElement(7, prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)

#print(p1)
print(p1+p2)  #Point(FieldElement_223(170),FieldElement_223(142))_FieldElement_223(0)_FieldElement_223(7)

## ex3-2

a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(num=170, prime=prime)
y1 = FieldElement(num=142, prime=prime)

x2 = FieldElement(num=60, prime=prime)
y2 = FieldElement(num=139, prime=prime)

p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)

print(p1+p2) # Point(FieldElement_223(220),FieldElement_223(181))_FieldElement_223(0)_FieldElement_223(7)

x3 = FieldElement(num=47, prime=prime)
y3 = FieldElement(num=71, prime=prime)

x4 = FieldElement(num=17, prime=prime)
y4 = FieldElement(num=56, prime=prime)

p3 = Point(x3, y3, a, b)
p4 = Point(x4, y4, a, b)

print(p3+p4)
# Point(FieldElement_223(215),FieldElement_223(68))_FieldElement_223(0)_FieldElement_223(7)


x5 = FieldElement(num=143, prime=prime)
y5 = FieldElement(num=98, prime=prime)

x6 = FieldElement(num=76, prime=prime)
y6 = FieldElement(num=66, prime=prime)

p5 = Point(x5, y5, a, b)
p6 = Point(x6, y6, a, b)

print(p5+p6)
# Point(FieldElement_223(47),FieldElement_223(71))_FieldElement_223(0)_FieldElement_223(7)

#ex3-4

x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)

p1 = Point(x1, y1, a, b)

print(p1+p1)

x2 = FieldElement(num=143, prime=prime)
y2 = FieldElement(num=98, prime=prime)

p2 = Point(x2, y2, a, b)

print(p2+p2)


x3 = FieldElement(num=47, prime=prime)
y3 = FieldElement(num=71, prime=prime)

p3 = Point(x3, y3, a, b)

print(p3+p3)

print(p3+p3+p3+p3)
print(p3+p3+p3+p3+p3+p3+p3+p3)
print(p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3)

