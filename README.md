# HTML to React/Vue Converter / Cleaner Python Script


## Instructions
Run this command below once to use this script 
``` console
pip install -r requirements.txt
```
Then tweak the automate.py script to remove certain
parts of the htmls such as header, footer, scripts, 
breadcrumb sections, scroll to top, loading animations
etc. 

You need to look into the html files. Then note down the
classes and ids of the repeatative parts. Then write them 
in the automate.py

The rfc.py and sfc.py holds the empty React component and 
Vue component templates respectively.


## WARNING !
Don't copy the .gitignore file from the Components folder 
while copying the generated Component files to your project! 

## Finally
Put your html files in the html folder.
Make sure your terminal is at the same path as automate.py
Then, Run this command to execute the script

``` console
python automate.py
```
Then take a look at the Component folder. The generated 
components will be there.
