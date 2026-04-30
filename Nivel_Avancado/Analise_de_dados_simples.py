import csv 

with open(r'Nivel_Avancado\Arquivos\vendas.csv','r',encoding='utf-8') as arquivo:
    conteudo = csv.reader(arquivo)
    total_vendas = 0
    contagem_produtos = {}
    itens = set()
    for linha in conteudo:
        if not linha[0].isdigit():
            continue
        total_vendas += int(linha[3]) * float(linha[4])
        produto = linha[2]
        qtd = int(linha[3])
        if produto in contagem_produtos:
            contagem_produtos[produto] += qtd
        else:
            contagem_produtos[produto] = qtd
    
    print(f'Total de Vendas: R$: {total_vendas}')
    print(f'Produto mais vendido: {max(contagem_produtos,key=contagem_produtos.get)}')
