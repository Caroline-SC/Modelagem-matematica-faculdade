import string


def verificar_cpf(cpf):
    texto_limpo = []
    for caractere in cpf:
        if caractere in string.ascii_letters:
            return {
                'sucesso':False,
                'Mensagem': 'CPF não pode conter letras'
            }
        elif caractere not in string.punctuation:
            texto_limpo.append(int(caractere))
    if len(texto_limpo) != 11:
        return {
            'sucesso':False,
            'Mensagem': 'CPF deve conter 11 digitos'
        } 
    soma1 = sum(texto_limpo[i] * (10 - i) for i in range(9))
    
    if (soma1*10)%11 != texto_limpo[9]:
        return {
            'sucesso':False,
            'Mensagem': 'CPF é invalido'
        }
    soma2 = sum(texto_limpo[i] * (11 - i) for i in range(10))

    if (soma2*10)%11 == texto_limpo[10]:
        return{
        'sucess':True,
        'Mensagem':'CPF é válido'
        }
    else:
        return {
            'sucesso':False,
            'Mensagem': 'CPF é invalido'
        }

cpf = input('Digite o cpf: ')
res = verificar_cpf(cpf)

print(res["Mensagem"])