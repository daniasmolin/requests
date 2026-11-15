import requests

response = requests.get("http://books.toscrape.com/")
response.encoding = 'utf-8'
html_text = response.text

book_prices = []

parts = html_text.split('class="price_color">')

for part in parts[1:]:
    price = part.split('<')[0]
    book_prices.append(price)

print(f"Знайдено цін: {len(book_prices)}\n")
for i, price in enumerate(book_prices, 1):
    print(f"{i}. {price}")