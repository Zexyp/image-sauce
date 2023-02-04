import requests
from lxml import etree
import climage
import os
from PIL import Image
from io import BytesIO

URL_GET_SEARCH = "https://www.bing.com/images/search?q={q}"

query = input("query: ")

response = requests.get(URL_GET_SEARCH.format(q=query))

tree = etree.HTML(response.content)

os.system('')

for e in tree.xpath("//img"):
    src = e.get("src")

    if not src or not src.startswith("http") or src.endswith(".svg"):
        continue
    
    image_response = requests.get(src)

    if image_response.status_code != 200:
        continue

    buffer = BytesIO()
    buffer.write(image_response.content)
    buffer.seek(0)

    img = climage.convert(buffer,
                          is_256color=True,
                          is_truecolor=False, 
                          is_unicode=True)

    print(img)

input("dun")
