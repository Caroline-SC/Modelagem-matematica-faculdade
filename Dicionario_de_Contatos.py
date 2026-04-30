contatos = []

def adicionarContato (nome, telefone,email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(contato)

def buscarContato (nome):
    for contato in contatos:
        if contato["nome"] == nome:
            print(contato)
            break
    print("Contato não encontrado")
    
def listarContatos():
    for contato in contatos:
        print(contato)

while True:
    print("O que deseja fazer:")
    print("1 - Adicionar contato")
    print("2 - Buscar contatos")
    print("3 - Listar contatos")
    print("4 - Parar aplicacao")

    acao = int(input("Resposta: "))


    match acao:
        case 1:
            nome = input("Digite o nome do contato: ")
            tel = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")

            adicionarContato(nome,tel,email)

        case 2:
            buscarContato(input("Digite o nome do contato: "))
        case 3:
            listarContatos()
        case 4:
            break