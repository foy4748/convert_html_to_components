import os
from bs4 import BeautifulSoup as BS4

from rfc import rfc

BASE_DIR = os.getcwd()

html_folder = os.path.join(BASE_DIR, "html")
react_folder = os.path.join(BASE_DIR, "Components")

htmls = os.listdir(html_folder)

for html in htmls:
    html_path = os.path.join(html_folder,html)
    with open(html_path,'r') as file:
        contents = file.read()
        soup = BS4(contents, 'html.parser')
        print(soup.body.find_all("script"))

print(rfc)
