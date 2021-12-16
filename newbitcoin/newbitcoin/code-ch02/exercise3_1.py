
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
run(ecc.PointTest('test_add2'))

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


x = FieldElement(num=47, prime=prime)
y = FieldElement(num=71, prime=prime)

p = Point(x, y, a, b)

for s in range(1,21):
    result = s*p
    print('{}*(47,71)=({},{})'.format(s, result.x.num, result.y.num))

# 1*(47,71)=(47,71)
# 2*(47,71)=(36,111)
# 3*(47,71)=(15,137)
# 4*(47,71)=(194,51)
# 5*(47,71)=(126,96)
# 6*(47,71)=(139,137)
# 7*(47,71)=(92,47)
# 8*(47,71)=(116,55)
# 9*(47,71)=(69,86)
# 10*(47,71)=(154,150)
# 11*(47,71)=(154,73)
# 12*(47,71)=(69,137)
# 13*(47,71)=(116,168)
# 14*(47,71)=(92,176)
# 15*(47,71)=(139,86)
# 16*(47,71)=(126,127)
# 17*(47,71)=(194,172)
# 18*(47,71)=(15,86)
# 19*(47,71)=(36,112)
# 20*(47,71)=(47,152)

a = FieldElement(0, prime)
b = FieldElement(7, prime)

x = FieldElement(num=15, prime=prime)
y = FieldElement(num=86, prime=prime)

p = Point(x, y, a, b)

inf = Point(None, None, a, b)

product = p

count=1
while product != inf:
    product += p
    count+=1

print(count) #7


print(7*p) #Point(infinity)

gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
print(gy**2 % p == (gx**3 + 7) % p)

n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

x = FieldElement(gx, p)
y = FieldElement(gy, p)
seven = FieldElement(7, p)
zero = FieldElement(0, p)

G = Point(x, y, seven, zero)
print(n*G)


