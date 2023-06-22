import os, re
from bs4 import BeautifulSoup as BS4
from caseconverter import pascalcase

# Import one of these empty template below

# React Empty Component template
# from rfc import rfc

# Vue Empty Component template
from sfc import sfc


# Getting the path of html and Components folder
BASE_DIR = os.getcwd()

html_folder = os.path.join(BASE_DIR, "html")
component_folder = os.path.join(BASE_DIR, "Components")

# Getting the path of the html files
htmls = os.listdir(html_folder)

# Skipping .gitignore in the html folder
# in the html file list
htmls.pop(0)

# Iterating through html files
for html in htmls:
    html_path = os.path.join(html_folder,html)

    # Generataing file name for component in PascalCase
    component_name = pascalcase(os.path.splitext(os.path.basename(html))[0])

    # Reading a single html file
    with open(html_path,'r', encoding='utf-8') as file:
        contents = file.read()

        # Generating Soup
        # Soup means the object representing 
        # the DOM in your python code!
        soup = BS4(contents, 'html.parser')
        body = soup.body

        # Clearing Script Tags
        for s in body.select('script'):
            s.extract()

        # Clearing by querying using css classes and ids
        # You need to look into your html files for these.

        ## Preloader 
        body.select('.preloader')[0].extract()       

        ## Header
        # body.select('.header-top-area')[0].extract()           
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
        body.select('.go-top')[0].extract() 

        ###
        
        # Converting Soup ==> PlainText
        # So that Regular Expression can be applied
        body_txt = str(body)

        # Converting class to className for JSX support
        body_txt = re.sub(r'class=\"','className=\"', body_txt)

        # Converting Comments for JSX support
        #### You don't need this for Vue component conversion
        # body_txt = re.sub(r"<!--", "{/*", body_txt)
        # body_txt = re.sub(r"-->", "*/}", body_txt)

        # Removing excess body Tag
        body_txt = re.sub(r"</?body>","", body_txt)
        
        ### Creating Component File -----------------------

        ################## Tweak here for React or Vue ##################
        # Change the files extension --------------------------------------_V_
        component_file = os.path.join(component_folder, component_name + ".vue")
        with open(component_file,'w', encoding='utf-8') as f:

            # Switch 'comment out' between these two lines
            # f.write(rfc.format(a=component_name,b=body_txt)) # For React
            f.write(sfc.format(b=body_txt)) # For Vue

