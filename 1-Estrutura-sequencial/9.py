# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
celcius = 5 * ((fahrenheit - 32) / 9)

print(fahrenheit, 'Graus Fahrenheit equivalem a', celcius, 'Graus celsius' )
