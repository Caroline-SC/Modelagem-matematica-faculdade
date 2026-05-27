class ContaBancaria:
    def __init__(self,numero_Conta,saldo,titular):
        self.numero_Conta = numero_Conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self,quantia):
        self.saldo = self.saldo + quantia

    def sacar(self,quantia):
        self.saldo = self.saldo - quantia

    def verificar_saldo(self):
        return self.saldo

class Cliente:
    def __init__(self,nome,cpf,contasBancarias):
        self.nome = nome
        self.cpf = cpf
        self.contasBancarias = contasBancarias
    
class Banco:
    def __init__(self, nome, listaClientes):
        self.nome = nome
        self.listaClientes = listaClientes

    def adicionarCliente (self,cliente):
        self.listaClientes.append(cliente)
    def removerCliente (self,cpf):
        for cliente in self.listaClientes:
            if cliente.cpf == cpf:
                self.listaClientes.remove(cliente)
                break
    def buscarContas(self, numero_Conta):
        for cliente in self.listaClientes:
           for conta in cliente.contasBancarias:
            if conta.numero_Conta == numero_Conta:
                return {
                    "cliente": cliente,
                    "conta":   conta
                }


conta_carlos_1 = ContaBancaria(numero_Conta=101, saldo=500.0, titular="Carlos Silva")
conta_carlos_2 = ContaBancaria(numero_Conta=102, saldo=1500.0, titular="Carlos Silva")

conta_ana = ContaBancaria(numero_Conta=201, saldo=3000.50, titular="Ana Souza")

cliente1 = Cliente(nome="Carlos Silva", cpf="123.456.789-00", contasBancarias=[conta_carlos_1, conta_carlos_2])

cliente2 = Cliente(nome="Ana Souza", cpf="987.654.321-11", contasBancarias=[conta_ana])

meu_banco = Banco(nome="Banco Nacional", listaClientes=[cliente1])
print(f"1. Clientes no banco: {[c.nome for c in meu_banco.listaClientes]}")

conta_carlos_1.depositar(200.0)
conta_ana.sacar(20.0)
print(f"Saldo de carlos: {conta_carlos_1.verificar_saldo()}")
print(f"Saldo de ana: {conta_ana.verificar_saldo()}")

meu_banco.adicionarCliente(cliente2)
print(f"\n1. Clientes no banco: {[c.nome for c in meu_banco.listaClientes]}")

resultado_busca = meu_banco.buscarContas(102)
if resultado_busca:
    print(f"4. Conta 102 encontrada! Titular: {resultado_busca['cliente'].nome} | Saldo: {resultado_busca['conta'].saldo}€")
else:
    print("4. Erro: Conta não encontrada.")

meu_banco.removerCliente("123.456.789-00")  
print(f"5. Clientes no banco após remover CPF '123.456.789-00': {[c.nome for c in meu_banco.listaClientes]}")

