import requests


def enviar_arquivo():
    caminho = 'C:/Users/Laura/Downloads/produtos_informatica.xlsx'

    try:
        with open(caminho, 'rb') as file:
            requisicao = requests.post('https://limewire.com/', files={'file': file})

        if requisicao.status_code == 200:
            saida_requisicao = requisicao.json()
            print(saida_requisicao)
            url = saida_requisicao['link']
            print("Arquivo enviado. Link para acesso:", url)
        else:
            print(f"Erro ao enviar arquivo: {requisicao.status_code}")
            print(f"Resposta do servidor: {requisicao.text}")  # Exibe mais detalhes do erro

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")


def enviar_arquivo_chave():
    caminho = 'C:/Users/Laura/Downloads/produtos_informatica.xlsx'
    chave_acesso = 'https://limewire.com/d/017a45b9-1498-4d49-92a2-36e61a2a6085#trvt4bcKF9Qr9CD0tzQpLNtYJF4upWHUVfY3AxLTOsk'

    try:
        with open(caminho, 'rb') as file:
            requisicao = requests.post(
                'https://limewire.com/',
                files={'file': file},
                headers={'Authorization': chave_acesso}  # Corrigido para 'Authorization'
            )

        if requisicao.status_code == 200:
            saida_requisicao = requisicao.json()
            print(saida_requisicao)
            url = saida_requisicao['link']
            print("Arquivo enviado com chave. Link para acesso:", url)
        else:
            print(f"Erro ao enviar arquivo com chave: {requisicao.status_code}")
            print(f"Resposta do servidor: {requisicao.text}")  # Exibe mais detalhes do erro

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")


def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.status_code == 200:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso")
    else:
        print("Erro ao baixar o arquivo:", requisicao.json())


# Testando as funções
enviar_arquivo()
receber_arquivo(
    'https://limewire.com/d/017a45b9-1498-4d49-92a2-36e61a2a6085#trvt4bcKF9Qr9CD0tzQpLNtYJF4upWHUVfY3AxLTOsk')


   
