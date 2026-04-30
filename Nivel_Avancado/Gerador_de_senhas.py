import string
import random

tamanho = int(input("Digite quantos caracteres dev ter sua senha: "))


carateres = string.ascii_letters + string.digits + string.punctuation

lista = list(carateres)

senha = ''
for i in range(tamanho):
    senha += random.choice(lista)

print(senha)
