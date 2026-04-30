def cParaF (c):
    return c * 1.8 +32
def fParaC (f):
    return (f - 32)/1.8
 
print("O que deseja converter?")
print("1 - Celcius para Fahrenheit")
print("2 - Fahrenheit para Celcius")

acao = int(input("Resposta: "))


match acao:
    case 1:
        c = float(input("Digite a temperatura em celcius: "))
        f = cParaF(c)
        print(f'{c}° celcius em fahrenheit é: {f}°')
    case 2:
        f = float(input("Digite a temperatura em fahrenheit: "))
        c = fParaC(f)
        print(f'{f}° fahrenheit em celcius é: {c}°')