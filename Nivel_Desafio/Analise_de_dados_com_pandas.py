import pandas as pd

df = pd.read_csv(r'Nivel_Desafio\arquivos\dados_clientes.csv')
renda = float(input('Qual vai ser a renda dos clientes para filtrar? '))

m_idade = df['Idade'].mean()
m_renda = df['Renda'].mean()
cidade_m = df['Cidade'].value_counts().index[0]
clientes_renda = df[df['Renda'] > renda][['Nome', 'Renda']]

print(f"\nMedia de idade: {m_idade:.2f}\n")
print(f"Media de renda: {m_renda:.2f}\n")
print("Cidade com mais clientes:")
print(cidade_m)
print(f"\nClientes com renda acima de {renda}: ")
print(clientes_renda)

