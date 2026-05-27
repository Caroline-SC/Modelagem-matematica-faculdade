import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'Nivel_Desafio\arquivos\dados_clientes.csv')
rotulos = ['18-25','26-30','31-35','36-40','41-45','46-50']

limites = [17, 25, 30, 35, 40, 45, 50]
rotulos = ['18-25', '26-30', '31-35', '36-40', '41-45', '46-50']

df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=limites, labels=rotulos)

contagem_faixas = df['Faixa_Etaria'].value_counts().reindex(rotulos)

plt.figure(figsize=(8, 5))
contagem_faixas.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Distribuição de Clientes por Faixa Etária', fontsize=14, fontweight='bold')
plt.xlabel('Faixa Etária', fontsize=12)
plt.ylabel('Quantidade de Clientes', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7) # 
plt.tight_layout()
plt.show()