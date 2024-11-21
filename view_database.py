import sqlite3

DB_NAME = 'products.db'

def view_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # テーブル一覧を確認
    print("Tables in the database:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"- {table[0]}")

    # productsテーブルの内容を表示
    print("\nContents of 'products' table:")
    cursor.execute("SELECT * FROM products;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

if __name__ == "__main__":
    view_database()
