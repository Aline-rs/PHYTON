# 29 - Faça um programa para resolver equações do 2º grau.
#a2+bx+c=0 

#Onde x é uma variável, sendo a, b e c constantes, com a ≠ 0

#Δ=b2−4ac 

#Δ<0→nãoexisteraizreal 

#Δ=0→existeraizreal 

#x=−b2a 

#Δ>0→existemduasraizesreais 

#x1=−b+Δ−−√2a 

#x2=−b−Δ−−√2a

print("defina os valores de A, B e C")
a=int(input())
b=int(input())
c=int(input())
delta = b**2-4*a*c

if delta == 0 :
  x= (b*-1)/2*a
  print("o valor de x é:", x)

elif delta < 0 :
  print("não existe raiz da equação")

else:
  xi = ((b*-1)+ delta)/2*a
  xii = ((b*-1)- delta)/2*a
  print ("os valores da raiz são" , xi , xii)