import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TRATAMENTO SIMPLES DOS DADOS
dados = pd.read_csv('ecommerce_preparados.csv')
dados.drop(dados[['Review1', 'Review2', 'Review3']], axis = 1, inplace = True)
dados['Desconto'] = dados['Desconto'].fillna(0)
print(dados.head(10).to_string())

# GRÁFICO DE HISTOGRAMA - DISTRIBUIÇÃO DA QUANTIDADE VENDIDA
plt.figure(figsize = (16, 9))
plt.hist(dados['Qtd_Vendidos_Cod'], bins = 8, color = '#3E0156', alpha = 0.8)
plt.xticks(ticks = range(0, int(dados['Qtd_Vendidos_Cod'].max()) + 5000, 5000))
plt.xlabel('Quantidade Vendida')
plt.ylabel('Produtos')
plt.title('DISTRIBUIÇÃO DA QUANTIDADE VENDIDA POR PRODUTO')
plt.show()

plt.savefig('Graficos_Gerados/Histograma_Qtd_Vendida.png')

# GRÁFICO DE DISPERSÃO - CORRELAÇÃO ENTRE QUANTIDADE VENDIDA E PREÇO
plt.figure(figsize = (16, 9))
sns.scatterplot(x = 'Qtd_Vendidos_Cod', y = 'Preço', data = dados, color = '#8101B4')
plt.xticks(ticks = range(0, int(dados['Qtd_Vendidos_Cod'].max()) + 2500, 2500))
plt.title('CORRELAÇÃO ENTRE PREÇO E QUANTIDADE VENDIDA')
plt.ylabel('Quantidade Vendida')
plt.show()

plt.savefig('Graficos_Gerados/Dispersao_Qtd_Vendida_e_Preco.png')

# MAPA DE CALOR DE CORRELAÇÃO DE VARIÁVEIS
plt.figure(figsize = (16, 9))
dados_corr = dados[['Preço_MinMax', 'Desconto_MinMax', 'N_Avaliações_MinMax', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(dados_corr, annot = True, fmt = '.2f')
plt.title('HEATMAP DE CORRELAÇÃO DE VARIÁVEIS')
plt.show()

plt.savefig('Graficos_Gerados/Heatmap_Variaveis.png')

# GRÁFICO DE BARRAS - MARCAS MAIS VENDIDAS NA LOJA
# Descobrindo as marcas com as maiores quantidades vendidas
top_marcas = dados.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values(ascending = False).head(5)

# Criando o gráfico
plt.figure(figsize = (16, 9))
plt.bar(top_marcas.index, top_marcas.values, color = '#76409C')
plt.title('TOP 5 MARCAS MAIS VENDIDAS')
plt.xlabel('Marca')
plt.ylabel('Quantidade Vendida')
plt.show()

plt.savefig('Graficos_Gerados/Barras_Marcas_Mais_Vendidas.png')

# GRÁFICO DE SETORES (PIZZA)
# Agrupamento das categorias de gêneros | Tratamento da coluna
substituicoes_Feminino = {'Mulher': 'Feminino', 'short menina verao look mulher': 'Feminino', 'Meninas': 'Feminino', 'roupa para gordinha pluss P ao 52': 'Feminino', 'bermuda feminina brilho Blogueira': 'Feminino'}
substituicoes_Masculino = {'Meninos': 'Masculino', 'menino': 'Masculino'}
substituicoes_Infantil = {'Sem gênero infantil': 'Sem gênero', 'Unissex': 'Sem gênero', 'Bebês': 'Feminino'}
dados['Gênero'] = dados['Gênero'].replace(substituicoes_Feminino)
dados['Gênero'] = dados['Gênero'].replace(substituicoes_Masculino)
dados['Gênero'] = dados['Gênero'].replace(substituicoes_Infantil)

# Criando o gráfico
plt.figure(figsize = (16, 9))
x = dados['Gênero'].value_counts().index # Categorias
y = dados['Gênero'].value_counts().values # Quantidades
plt.pie(y, labels = x, autopct = '%.1f%%', startangle = 90, colors = ['#4b3f7f', '#367082', '#72debf'], textprops = {'color': 'white'})
plt.title('GÊNERO DOS PRODUTOS')
plt.show()

plt.savefig('Graficos_Gerados/Pizza_Tipo_Genero_Produtos.png')

# GRÁFICO DE DENSIDADE - DENSIDADE DAS AVALIAÇÕES
plt.figure(figsize = (16, 9))
sns.kdeplot(dados['Nota'], fill = True, color = '#863e9c')
plt.xlabel('Nota do Produto')
plt.ylabel('Quantidade de Avaliações')
plt.title('DENSIDADE DAS AVALIAÇÕES DOS PRODUTOS')
plt.show()

plt.savefig('Graficos_Gerados/Densidade_Avaliacoes.png')

# GRÁFICO DE REGRESSÃO
plt.figure(figsize = (16, 9))
sns.regplot(x = 'Nota', y = 'Preço', data = dados, color = '#278f65', scatter_kws = {'alpha': 0.5, 'color': '#34c289'})
plt.title('REGRESSÃO DE NOTA POR PREÇO')
plt.xlabel('Nota do Produto')
plt.ylabel('Preço do Produto')
plt.show()

plt.savefig('Graficos_Gerados/Regressao_Nota_e_Preco.png')
