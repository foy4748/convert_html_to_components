import os, re
from replace_links import replace_links
from bs4 import BeautifulSoup as BS4
from caseconverter import pascalcase

#########################################
### Change this variable to switch
### between React and Vue
isReact = True
#########################################

file_extension = ''
if isReact:
    file_extension = '.jsx'
else:
    file_extension = '.vue'

# Importing empty template 

## React Empty Component template
from rfc import rfc

## Vue Empty Component template
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

        # Replacing Links to NavLink or router-link
        replace_links(soup, isReact)

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


        ## Mouse Cursor
        for s in body.select(".mouseCursor"):
            s.extract()

        ## Footer
        body.select('.footer-area')[0].extract() 
        try:
            body.select('.footer-bottom')[0].extract() 
        except:
            pass
        
        ## Scroll to Top button
        try:
            body.select('.progress-wrap')[0].extract() 
        except:
            pass

        ## Canvas Overlay
        try:
            body.select('.offcanvas-overly')[0].extract()
        except:
            pass
        ## Off-canvas Extra Info
        try:
            body.select('.extra-info')[0].extract()
        except:
            pass

        try:
            body.select('.header-area')[1].extract()           
        except:
            pass

        ## Breadcrumb
        try:
            body.select(".breadcrumb-area")[0].extract()
        except:
            pass

        ###
        
        # Converting Soup ==> PlainText
        # So that Regular Expression can be applied
        body_txt = str(body)

        if isReact:
            # Converting class to className for JSX support
            #### You don't need this for Vue component conversion
            body_txt = re.sub(r'class=\"','className=\"', body_txt)

            # Converting Comments for JSX support
            #### You don't need this for Vue component conversion
            body_txt = re.sub(r"<!--", "{/*", body_txt)
            body_txt = re.sub(r"-->", "*/}", body_txt)

        # Removing excess body Tag
        body_txt = re.sub(r"</?body>","", body_txt)
        
        ### Creating Component File -----------------------

        ################## Tweak here for React or Vue ##################
        # Change the files extension --------------------------------------_V_
        component_file = os.path.join(component_folder, component_name + file_extension)
        with open(component_file,'w', encoding='utf-8') as f:

            # Switch 'comment out' between these two lines
            if isReact:
                f.write(rfc.format(a=component_name,b=body_txt)) # For React
            else:
                f.write(sfc.format(b=body_txt)) # For Vue

