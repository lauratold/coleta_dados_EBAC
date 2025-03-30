import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []
for artigo in extracao.find_all('article', class_='product_pod'): # Encontrar cada
   livro = {}
   for h3 in artigo.find_all('h3'):
       titulo_tag = h3.find('a')
       if titulo_tag:
           titulo = titulo_tag.text.strip()
           livro['Título'] = titulo
   for p in artigo.find('p', class_='price_color'):
       preco = p.text.strip()
       livro['Preço'] = preco
   # Adicionando o livro ao catálogo
   catalogo.append(livro)
   contar_livros += 1

# Exibindo o total de livros e o catálogo
print('Total de livros:', contar_livros)
print(catalogo)