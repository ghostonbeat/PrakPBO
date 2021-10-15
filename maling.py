from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://sentracomputer.com/product.php?category=21&subcat=1")

ambil = BeautifulSoup(page.content, 'html.parser')

inti = ambil.find_all('span', class_='bigtitle')

laptop = []

for q in inti:
    laptop.append({
        'judul':q.find('b').text,
        'spek':q.find('small').text
    })

transfer = pd.DataFrame(laptop)
transfer.to_csv('anjay.csv', index=False, encoding="utf-8")