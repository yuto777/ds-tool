import sqlite3

DB_NAME = 'products.db'

# 商品の追加
def add_product(title, price, stock):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, title TEXT, price TEXT, stock INTEGER)''')
    cursor.execute('''INSERT INTO products (title, price, stock) VALUES (?, ?, ?)''',
                   (title, price, stock))
    connection.commit()
    connection.close()

# 商品一覧の取得
def get_products():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    connection.close()
    return products

# 販売レポートの生成
def generate_sales_report():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT title, price, stock FROM products')
    products = cursor.fetchall()
    connection.close()
    
    # 簡単な売上レポートを生成（ここでは在庫数を単純に表示）
    report = [{"title": product[0], "price": product[1], "stock": product[2]} for product in products]
    return report
