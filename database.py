import sqlite3

DB_NAME = 'products.db'

# データベース接続の取得
def get_connection():
    return sqlite3.connect(DB_NAME)

# 初期化（テーブルの作成）
def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    # 商品テーブルの作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    # 売上記録テーブルの作成（任意の拡張）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    connection.commit()
    connection.close()

# 商品の追加
def add_product(title, price, stock):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO products (title, price, stock)
            VALUES (?, ?, ?)
        ''', (title, price, stock))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        connection.close()

# 商品一覧の取得
def get_products():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, title, price, stock FROM products')
        products = cursor.fetchall()
        return products
    except sqlite3.Error as e:
        print(f"Error fetching products: {e}")
        return []
    finally:
        connection.close()

# 在庫の更新
def update_stock(product_id, quantity):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE products
            SET stock = stock + ?
            WHERE id = ?
        ''', (quantity, product_id))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error updating stock: {e}")
    finally:
        connection.close()

# 販売レポートの生成
def generate_sales_report():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT title, price, stock FROM products')
        products = cursor.fetchall()
        
        # レポート生成
        report = [{"title": product[0], "price": product[1], "stock": product[2]} for product in products]
        return report
    except sqlite3.Error as e:
        print(f"Error generating sales report: {e}")
        return []
    finally:
        connection.close()

# テスト用（例：初期化とデータ挿入）
if __name__ == "__main__":
    initialize_database()
    add_product("Dog Toy", 9.99, 100)
    add_product("Cat Food", 19.99, 50)
    print("Products:", get_products())
    print("Sales Report:", generate_sales_report())
