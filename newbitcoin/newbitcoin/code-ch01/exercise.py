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