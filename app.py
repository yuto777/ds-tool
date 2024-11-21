from flask import Flask, render_template, request, redirect, url_for
from database import add_product, get_products, generate_sales_report
from scraper import scrape_products  # BeautifulSoupを使用したスクレイピング

app = Flask(__name__)

# 商品管理ページ
@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

# 商品追加ページ
@app.route('/add_product', methods=['POST'])
def add_new_product():
    title = request.form['title']
    price = request.form['price']
    stock = request.form['stock']
    
    add_product(title, price, stock)
    return redirect(url_for('index'))

# 販売レポートページ
@app.route('/sales_report')
def sales_report():
    report = generate_sales_report()
    return render_template('report.html', report=report)

# スクレイピングページ（例として商品情報を取得）
@app.route('/scrape')
def scrape():
    scraped_data = scrape_products()  # スクレイピング
    return f'Scraped {len(scraped_data)} products!'

@app.route("/debug/products")
def debug_products():
    from database import get_products
    products = get_products()
    return {"products": products}

if __name__ == "__main__":
    app.run(debug=True)
