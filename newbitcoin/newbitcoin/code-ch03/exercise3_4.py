
#ex3-4
from ecc import FieldElement, Point
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)

p1 = Point(x1, y1, a, b)

print(p1+p1)

#Point(49,71)_0_7 FieldElement(223)

x2 = FieldElement(num=143, prime=prime)
y2 = FieldElement(num=98, prime=prime)

p2 = Point(x2, y2, a, b)

print(p2+p2)

#Point(64,168)_0_7 FieldElement(223)

x3 = FieldElement(num=47, prime=prime)
y3 = FieldElement(num=71, prime=prime)

p3 = Point(x3, y3, a, b)

print(p3+p3) #Point(36,111)_0_7 FieldElement(223)

print(p3+p3+p3+p3) #Point(194,51)_0_7 FieldElement(223)

print(p3+p3+p3+p3+p3+p3+p3+p3) #Point(116,55)_0_7 FieldElement(223)

print(p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3+p3) #Point(infinity)
