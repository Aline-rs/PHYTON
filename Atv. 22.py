# 22 - Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².

import math

print("digite o raio:")
r= int(input())
d=r*2
c=2*math.pi*r
a=math.pi*(r**2)
print("o diametro é", d)
print("a circunferencia é", c)
print("a area é", a)