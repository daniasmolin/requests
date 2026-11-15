import requests
response = requests.get("http://books.toscrape.com/")
response.encoding = 'utf-8'
html_text = response.text

book_titles = []

products = html_text.split('<article class="product_pod">')

for product in products[1:]:
    if 'title="' in product:
        title_part = product.split('title="')[1]
        title = title_part.split('"')[0]
        book_titles.append(title)
print(f"Знайдено назв книг: {len(book_titles)}\n")
for i, title in enumerate(book_titles, 1):
    print(f"{i}. {title}")