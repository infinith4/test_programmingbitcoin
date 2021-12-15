
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
