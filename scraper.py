import requests
from bs4 import BeautifulSoup

# サンプルのURLを指定（実際のURLに置き換えてください）
URL = "https://example.com/products"

def scrape_products():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = []
    # 商品情報が格納されているタグを探す（HTML構造に応じて修正する）
    for product_div in soup.find_all('div', class_='product'):
        title = product_div.find('h2').text.strip()
        price = product_div.find('span', class_='price').text.strip()
        stock = product_div.find('span', class_='stock').text.strip()
        
        products.append({"title": title, "price": price, "stock": stock})
    
    return products
