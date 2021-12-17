
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

G = Point(x, y, zero, seven)
print(n*G) #Point(infinity)

from ecc import G, N

print(N*G) #Point(infinity)

from ecc import S256Point, G, N
z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px, py)
s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)

#ex3-6
P = (0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c,
0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34)

point = S256Point(P[0], P[1])

# signature 1
z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60
r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395
s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4

s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r) #True

# signature 2
z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
r = 0xeff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c
s = 0xc7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6

s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r) #True


from ecc import S256Point, G, N
from helper import hash256
e = int.from_bytes(hash256(b'my secret'), 'big')
z = int.from_bytes(hash256(b'my message'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
point = e*G
print(point)
print(hex(z))
print(hex(r))
print(hex(s))