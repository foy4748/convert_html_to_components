import os, re
from bs4 import BeautifulSoup as BS4

from rfc import rfc
from caseconverter import pascalcase

BASE_DIR = os.getcwd()

html_folder = os.path.join(BASE_DIR, "html")
react_folder = os.path.join(BASE_DIR, "Components")

htmls = os.listdir(html_folder)

# Skipping .gitignore
htmls.pop(0)

for html in htmls:
    html_path = os.path.join(html_folder,html)
    component_name = pascalcase(os.path.splitext(os.path.basename(html))[0])

    with open(html_path,'r') as file:
        contents = file.read()
        soup = BS4(contents, 'html.parser')
        body = soup.body

        # Clearing Script Tags
        for s in body.select('script'):
            s.extract()

        # Clearing 

        ## Preloader 
        body.select('.preloader')[0].extract()       

        ## Header
        body.select('.header-top-area')[0].extract()           
        body.select('.header-area')[0].extract()           

        ## BreadCrumb
        try:
            body.select('.breadcrumb-area')[0].extract() 
        except:
            pass



        ## Footer
        body.select('.footer-area')[0].extract() 
        try:
            body.select('.footer-bottom')[0].extract() 
        except:
            pass
        
        ## Scroll to Top button
        body.select('.progress-wrap')[0].extract() 

        ###
        
        # Converting Soup ==> PlainText
        body_txt = str(body)

        # Converting class to className
        body_txt = re.sub(r'class=\"','className=\"', body_txt)

        # Converting Comments
        body_txt = re.sub(r"<!--", "{/*", body_txt)
        body_txt = re.sub(r"-->", "*/}", body_txt)

        # Removing body Tag
        body_txt = re.sub(r"</?body>","", body_txt)
        
        # Creating React File
        react_file = os.path.join(react_folder, component_name + ".jsx")
        with open(react_file,'w', encoding='utf-8') as f:
            f.write(rfc.format(a=component_name,b=body_txt))

