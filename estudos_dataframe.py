import pandas as pd

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo: números, textos...
dados = [
    {'nome': 'Ana', 'idade': 20, 'cidade': 'São Paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'São José dos Campos'},
    {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio de Janeiro'},
]

#dicionário: estrutura composta de pares chave_valor
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 20,
    'Cidade': 'São Paulo'
}
print('Dicionário de uma pessoa: \n', dicionario_pessoa)
print('Atributo de Dicionario: \n', dicionario_pessoa.get('nome'))

# Criando o DataFrame
df = pd.DataFrame(dados)
print('DataFrame \n', df)

# Adicionando nova coluna 'salario'
df['salario'] = [4100, 3600, 1200]

# Adicionando um novo registro
df.loc[len(df)] = {
    'nome': 'João',
    'idade': '30',
    'cidade': 'Taubaté',
    'salario': 4800
}

print('DataFrame Atual \n', df)

# Corrigindo o erro: Convertendo a coluna 'idade' para numérica
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')

# Agora podemos aplicar o filtro sem erro
filtro_idade = df[df['idade'] >= 30]
print('Filtro \n', filtro_idade)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados_CSV.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados_CSV.csv')
print('\n Leitura do csv \n', df_lido)