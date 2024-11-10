from bs4 import BeautifulSoup
import requests

while True:
    url = input("Introduza um link de perfil do Bluesky: ")

    if not "https://bsky.app/profile/" in url:
        print("Link inválido. Tente novamente.")
        continue
    break

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0" 
}

requisicao = requests.get(url, headers=headers)

bluesky_page = BeautifulSoup(requisicao.text, "html.parser")
rss_page = requests.get(bluesky_page.find("link", rel="alternate")["href"], headers=headers)
rss_elements = BeautifulSoup(rss_page.text, "html.parser")
file = open("postagens.txt", "w+", encoding="utf-8")

for post in rss_elements.find_all("description"):
    file.write(f"{post.get_text()}\n")

file.close()

print("Processo finalizado. Cheque o diretório do script por 'postagens.txt'.")