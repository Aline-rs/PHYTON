# 27 - A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:
#Nota	Peso
#Trabalho de Laboratório	2
#Avaliação Semestral	3
#Exame Final	5
#aça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a #tabela:

#Média Ponderada	Conceito
#8,00 <= Média <= 10,00	A
#7,00 <= Média < 8,00	B
#6,00 <= Média < 7,00	C
#5,00 <= Média < 6,00	D
#0,00 <= Média < 5,00	E

print("digite a nota de trabalho")
x=int(input())
tl=x*2
print("digite a nota da avaliação")
y=int(input())
av=y*3
print("digite a nota do exame final")
z=int(input())
ex=z*5

media=(tl+av+ex)/10

if  media >= 8:
  print("sua média foi de ", media, "e conceito A")

elif media < 8 and media >= 7:
  print("sua média foi de ", media, "e conceito B")

elif media < 7 and media >= 6:
  print("sua média foi de ", media, "e conceito C")

elif media < 6 and media >= 5:
  print("sua média foi de ", media, "e conceito D")

else:
  print("sua média foi de ", media, "e conceito E")