# 23 - Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
# o número digitado ao quadrado;
# o número digitado ao cubo;
# a raiz quadrada do número digitado.

import math

print("digite o numero")
x= int(input())
y=x**2
z=x**3
w=math.sqrt(x)
print ("o valor ao quadrado é", y)
print ("o valor ao cubo é", z)
print ("a raiz do valor é", w)