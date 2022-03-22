#Escreva um programa que receba como entrada um número de 5 dígitos, separe o número em dígitos individuais e os imprima separados por 3 espaços cada um. Por exemplo, se o usuário digitar 42339, o programa deverá imprimir: 4 2 3 3. Dica: utilize as operações de divisão e módulo para extrair cada dígito do número.
print("Digite um número de 5 casas: ")
num = input()
x = [int(a) for a in str(num)]
print(x)