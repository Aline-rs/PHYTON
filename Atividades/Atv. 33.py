# 33 - Uma empresa quer transmitir dados pelo telefone, mas está preocupada com a interceptação telefônica. Todos os seus dados são transmitidos como inteiros de quatro dígitos. Ela pediu para que você escreva um programa que criptografe seus dados, para que eles possam ser transmitidos com mais segurança. Implemente a função criptogra(numero) que receba como parâmetro um número inteiro de quatro dígitos e criptografe-o da seguinte forma:

#Substitua cada um dos dígitos do número usando a seguinte fórmula: (digito + 7) módulo 10;
#Após a substituição, troque o primeiro dígito pelo terceiro e troque o segundo dígito pelo quarto;
#Retorne o número inteiro criptografado.