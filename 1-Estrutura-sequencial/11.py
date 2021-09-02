# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A- o produto do dobro do primeiro com metade do segundo .
# B- a soma do triplo do primeiro com o terceiro.
# C- o terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro numero inteiro: '))
num2 = int(input('Digite o segundo numero inteiro: '))
num3 = float(input('Digite o numero real: '))

prod = (num1 * num1) + (num2 / 2)
print('A - O produto do dobro do primeiro com metade do segundo', prod)

som = (num1 * 3) + num3
print('B- a soma do triplo do primeiro com o terceiro.', som)

cube = pow(num3, 3)
print('C- o terceiro elevado ao cubo.', cube)
