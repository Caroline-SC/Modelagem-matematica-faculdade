import random
import os

class Jogo:
    def __init__(self):
        self.jogador = Jogador()
        self.palavra = Palavra()
        self.tentativas_restantes = 6
        self.desenho_forca = self.desenho_forca()
        
    def desenho_forca(self):
        return [
            """
               --------
               |      |
               |
               |
               |
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |
               |
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |      |
               |
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     /
               |
            ----------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |
            ----------
            """
        ]
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_tela_jogo(self):
        erros = 6 - self.tentativas_restantes
        print("_" * 50)
        print(f" JOGO DA FORCA - {self.jogador.nome}")
        print("_" * 50)
        print(self.desenho_forca[erros])
        print(f"Tentativas restantes: {self.tentativas_restantes}")
        print(f"\nPalavra: {self.palavra.obter_palavra_mascarada()}")
        print(f"Letras tentadas: {self.palavra.exibir_letras_tentadas()}")
    
    def obter_entrada_letra(self):
        while True:
            letra = input("\nDigite uma letra: ").upper().strip()
            
            if not letra.isalpha():
                print("Por favor, digite apenas uma letra")
                continue
            
            if len(letra) != 1:
                print("Por favor, digite apenas UMA letra")
                continue
                
            return letra
    
    def jogar(self):
        self.limpar_tela()
        self.jogador.definir_nome()
        self.palavra.randomizar_palavra()
        
        # Loop principal do jogo
        while self.tentativas_restantes > 0 and not self.palavra.palavra_completa():
            self.limpar_tela()
            self.exibir_tela_jogo()
            
            letra = self.obter_entrada_letra()
            acertou, mensagem , quantidade= self.palavra.verificar_letra(letra)
            
            if acertou:
                print(f"\n{mensagem}")
            else:
                if "já tentou" in mensagem:
                    print(f"\n{mensagem}")
                else:
                    self.tentativas_restantes -= 1
                    print(f"\n{mensagem}")
            
            input("\nPressione ENTER para continuar...")
        
        # Resultado final
        self.limpar_tela()
        print("_" * 50)
        
        if self.palavra.palavra_completa():
            print(" VOCÊ VENCEU! ")
            print("_" * 50)
            print(self.desenho_forca[6 - self.tentativas_restantes])
            print(f"\nA palavra era: {self.palavra.obter_palavra_secreta()}")
            print(f"Tentativas restantes: {self.tentativas_restantes}")
        else:
            print(" VOCÊ PERDEU! ")
            print("_" * 50)
            print(self.desenho_forca[6])
            print(f"\n📖 A palavra era: {self.palavra.obter_palavra_secreta()}")
        
        print("_" * 50)
        
        # Pergunta se quer jogar novamente
        
        print(f"\nObrigado por jogar, {self.jogador.nome}!")


class Palavra():

    def __init__(self):
        self.palavra_secreta = ""
        self.letras_descobertas = []
        self.letras_tentadas = []
        
    def randomizar_palavra(self):
        palavras = [
            'PYTHON', 'PROGRAMACAO', 'COMPUTADOR', 'DESENVOLVIMENTO',
            'ALGORITMO', 'BANCO', 'DADOS', 'INTELIGENCIA', 'ARTIFICIAL',
            'JAVA', 'JAVASCRIPT', 'HTML', 'CSS', 'REACT', 'ANGULAR',
            'ECLIPSE', 'VSCODE', 'GITHUB', 'LINUX', 'WINDOWS',
            'GAME', 'DESIGN', 'SOFTWARE', 'HARDWARE', 'REDE'
        ]
        self.palavra_secreta = random.choice(palavras).upper()
        self.letras_descobertas = ['_'] * len(self.palavra_secreta)
        self.letras_tentadas = []

    def verificar_letra(self, letra):
        letra = letra.upper()
        
        if letra in self.letras_tentadas:
            return False, f"Você já tentou a letra '{letra}'!", 0
        
        self.letras_tentadas.append(letra)
        
        if letra in self.palavra_secreta:
            acertos = 0
            for i, char in enumerate(self.palavra_secreta):
                if char == letra:
                    self.letras_descobertas[i] = letra
                    acertos += 1
            return True, f"A letra '{letra}' aparece {acertos} vez(es)!", acertos
        else:
            return False, f"A letra '{letra}' NÃO está na palavra!", 0
    
    def palavra_completa(self):
        return '_' not in self.letras_descobertas
    
    def obter_palavra_mascarada(self):
        return ' '.join(self.letras_descobertas)
    
    def obter_palavra_secreta(self):
        return self.palavra_secreta
    
    def obter_letras_tentadas(self):
        return self.letras_tentadas
    
    def exibir_letras_tentadas(self):
        if self.letras_tentadas:
            return ', '.join(sorted(self.letras_tentadas))
        return "Nenhuma letra tentada ainda"
    
class Jogador():
    def __init__(self):
        self.nome = ""    
        
    def definir_nome(self):
        nome = input("Digite seu nome: ").strip()
        if nome:
            self.nome = nome
        print(f"\nBem-vindo, {self.nome}!")

    
try:
    jogo = Jogo()
    jogo.jogar()
except KeyboardInterrupt:
    print("\n\n👋 Jogo interrompido. Até logo!")