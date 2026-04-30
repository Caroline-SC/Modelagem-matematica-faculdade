vogais = ['a','e','i','o','u']

string = input('Digite a frase: ')
contador = 0

for letra in string:
    if letra in vogais:
        contador += 1
print(f'A frase: {string}. Tem {contador} vogais.')
