#Exercise2
## F 57 のもとで解いてください（すべての + は + f 、 − は − f とします）。
## 44 + 33
## 77 % 57 = 20
## 9 − 29
## -20 % 57 = 37
## 17 + 42 + 49
## (59 + 49) % 57 = 108 % 57 = 51
## 52 − 30 − 38
# (22 - 38) % 57 = -16 % 57 = 41

from ecc import FieldElement
# a = FieldElement(7, 13)
# b = FieldElement(12, 13)
# c = FieldElement(6, 13)
# print(a+b==c)

a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a*b==c)

prime = 31
# 3/24
print(3*pow(24, prime-2, prime) % prime)
# 17**(-3)
print(pow(17, prime-4, prime) % prime)
# (4**(-4)) * 11 
print(pow(4, prime-5, prime)*11 % prime)



a = FieldElement(3, 31)
b = FieldElement(24, 31)
print(a / b == FieldElement(4, 31))