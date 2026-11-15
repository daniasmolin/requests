import requests

url = "http://books.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'
html_text = response.text

books_on_page = []

products = html_text.split('<article class="product_pod">')

for product in products[1:]:
    title = product.split('title="')[1].split('"')[0]

    price = product.split('class="price_color">')[1].split('<')[0]

    rating = product.split('star-rating ')[1].split('"')[0]

    availability_raw = product.split('class="instock availability">')[1].split('</p>')[0]
    availability = availability_raw.split('</i>')[1].strip()

    books_on_page.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability
    })
for i, book in enumerate(books_on_page, 1):
    print(f"{i}. Назва: {book['title']}")
    print(f"   Ціна: {book['price']} | Рейтинг: {book['rating']} | Статус: {book['availability']}")
    print("-" * 40)