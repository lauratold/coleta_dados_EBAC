import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text,'html.parser')

#exibir texto
print(extracao.text.strip())

#filtrar exibicao pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.name
    print('Titulo ', titulo)

#contar qtd de linhas e paragrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 #contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('total de titulos', contar_titulos)
print('total_de_paragrafos', contar_paragrafos)

#exibir tag aninhada
for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
      for a in link.find_all('a', href=True):
          print('Texto Link: ', a.text.strip(), '| URL: ', a['href'])
