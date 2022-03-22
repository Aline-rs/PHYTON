# 20 - Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

print ("Digite seu salario: ")
x= int(input())
print ("Digite seu aumento percentual: ")
y= int(input())
z= (x*(y/100))+x
print ("seu novo salario é ", z)