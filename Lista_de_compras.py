lista = []

def add(item):
    lista.append(item)
def remove(item):
    lista.remove(item)
def show():
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
    print()

while True:
    print("O que deseja fazer:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Parar aplicacao")

    acao = int(input("Resposta: "))


    match acao:
        case 1:
            add(input("Digite o item que quer adicionar: "))
        case 2:
            remove(input("Digite o item que quer remover: "))
        case 3:
            show()
        case 4:
            break