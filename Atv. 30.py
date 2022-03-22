# 30 - Faça um programa que receba vários números, calcule e mostre:

#A soma dos números digitados;
#A quantidade de números digitados;
#A média dos números digitados;
#O maior número digitado;
#O menor número digitado;
#A média dos números pares;
#A porcentagem dos números ímpares entre todos os números digitados.
#Finalize a entrada de dados com a digitação do número 0.

qtdNum = 0

somaNum = 0

maior = 0

menor = 0

somaPar = 0

qtdPar = 0

qtdImpar = 0

num = int(input('Digite um valor: '))

maior = num

menor = num

while(num != 0):

   qtdNum += 1

   somaNum += num

   

   if num > maior:

       maior = num

   elif num < menor:

       menor = num

   if num % 2 == 0:

       qtdPar += 1

       somaPar += num

   else:

       qtdImpar += 1

   num = int(input('Digite um valor'))

print('Quantidade de números digitados:', qtdNum)

print('Média dos números: ', somaNum / qtdNum)

print('O maior número digitado foi: ', maior)

print('O menor número digitado foi: ', menor)

print('Média dos números pares: ', somaPar / qtdPar)

print('Porcentagem de números ímpares: ', qtdImpar / qtdNum * 100)