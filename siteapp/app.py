from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

# Trecho HTML que você compartilhou
html = """
# Coloque aqui o trecho HTML dos filmes que você compartilhou
"""

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Rota para a página inicial
@app.route('/')
def index():
    # Encontra todos os links de filmes dentro do trecho HTML
    links_filmes = soup.find_all('a', href=True)

    # Crie uma lista de dicionários com informações de filmes
    filmes = []
    for link in links_filmes:
        filme_nome = link.text.strip()
        filme_link = link['href']
        filmes.append({'Nome do Filme': filme_nome, 'Link do Filme': filme_link})

    return render_template('pagina_inicial.html', filmes=filmes)

if __name__ == '__main__':
    app.run(debug=True)
