# 28 - Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir.
#Média	Situação
#7,00 <= Média <= 10,00	Aprovado
#3,00 <= Média < 7,00	Exame Especial
#0,00 <= Média < 3,00	Reprovado

print ("Digite as notas: ")
x= int(input())
y= int(input())
z= int(input())
media =(x+y+z)/3
print("sua média foi de " , media)

if  media >= 7:
  print("APROVADO")
elif media < 7 and media >= 3:
   print("exame especial")
else:
  print("REPORVADO")