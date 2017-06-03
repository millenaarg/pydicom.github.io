#!/usr/bin/env python

'''
circle_urls.py will rename all url files to not have extension .html
'''

import sys
import os
from glob import glob

site_dir = os.path.abspath(sys.argv[1])
print("Using site directory %s" %(site_dir))

files = glob("%s/*.html" %(site_dir))

# For each file, we need to replace all links to have correct .html extension
search_names = [os.path.basename(f).replace('.html','') for f in files]
for html_file in files:
    with open(html_file,'r') as filey:
        content = filey.read()
    for search_name in search_names:
        content = content.replace('%s"' %(search_name),'%s.html"' %(search_name))
    content = content.replace('/images/logo/logo.png','https://pydicom.github.io/images/logo/logo.png')
    with open(html_file,'w') as filey:
        filey.write(content)
