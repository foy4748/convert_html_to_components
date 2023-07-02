import re
from bs4 import BeautifulSoup as BS4

def replace_links(soup, react):
    body = soup.body
    anchor = ''
    if react:
        anchor = 'NavLink'
    else:
        anchor = 'router-link'
    html_link_patterns = r'href=("|\')(.*).html("|\')'
    for link in body.findAll('a'):
        if re.search(html_link_patterns, str(link)) is not None:
            # Replacing anchor tags
            link.name = anchor

            # Replacing .html and _ 
            link['href'] = '/' + link['href'].replace('.html','').replace('index','').replace('_', '-').replace('-2','index-2')

            # Replacing href by to
            link.attrs['to'] = link.attrs.pop('href')
            print(link)

