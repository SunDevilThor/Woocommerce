# Woocommerce
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTML, HTMLSession
import csv

url = 'http://barefootbuttons.com/product-category/version-1/'

s = HTMLSession()


#print(r.html.find('#header'))

def get_links(url):
    r = s.get(url)
    items = r.html.find('div.product-small.box')
    links = []
    for item in items: 
        links.append(item.find('a', first=True).attrs['href'])
    
    return links

def get_product(link):
    r = s.get(link)

    title = r.html.find('h1', first=True).full_text.strip()
    price = r.html.find('div.price-wrapper', first=True).full_text.strip().replace('$', '')
    sku = r.html.find('span.sku_wrapper', first=True).full_text
    category = r.html.find('span.posted_in', first=True).full_text
    print(sku)

    product = {
        'title': title, 
        'price': price, 
        'sku': sku, 
        'category': category, 
    }

    print(product)
    return product

links = get_links(url)

results = []

for link in links: 
    results.append(get_product(link))

with open('Results.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print('Finished writing to CSV file.')

