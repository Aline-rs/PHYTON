# 18 - Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.

print ("Digite a nota 1: ")
x= int(input())
print ("Digite seu peso: ")
xp= int(input())
print ("Digite a nota 2: ")
y= int(input())
print ("Digite seu peso: ")
yp= int(input())
print ("Digite a nota 3: ")
z= int(input())
print ("Digite seu peso: ")
zp= int(input())

media=(x*xp + y*yp + z*zp)/(xp+yp+zp)

print("sua nota é", media)