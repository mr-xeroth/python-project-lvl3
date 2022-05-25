import os
import requests
import re
import html
from urllib.parse import urljoin
from bs4 import BeautifulSoup


def download(url, folder):
    #url = url.rstrip('/')
    r = requests.get(url)
    
    print('\nurl:', url)
        
    soup = BeautifulSoup(r.text, 'html.parser')

    img_tags = soup.find_all('img')

    print('tag_num:', len(img_tags))
    print('url:', url)
    host_url = re.search('(?<=\://)(.*)(?=/|\Z)', url).group(1)
    
    #n = re.sub('(html?)$', '', url)
    #print('\n^htm:', n)
    #file_name = re.sub('\W+', '-', n)
    #print('\nfname:', file_name)
    file_path = os.path.join(folder, f'{host_url}.html')
    print('file_path:', file_path)
    #with open(file_path, "w") as f:
    #    f.write(r.text)
    

    print('host_url:', host_url)
    for tag in img_tags:
        print(tag['src'])
        f_name, f_ext = os.path.splitext(tag['src'])
        d = requests.get(urljoin(url, tag['src']))
        f_content = d.content
        print('cont:', len(f_content))
        print('orig:', f_name)
        #f_name_new = os.path.join(, f_name)
        
        file = f_name.lstrip('/')
        #print('fnn:', f_name_new)
        
        subst = re.sub('\W+', '-', host_url)
        pure_path = f'{subst}_files'

        subst = re.sub('\W+', '-', file)
        pure_file = f'{subst}{f_ext}'

        f_path = f'{pure_path}/{pure_file}'
        print('path_new:', f_path)
        
        # re.sub('\W+', '-',

        #new_image_url = os.path.join(host_url)
        #with open(file_path, "w") as f:
        #    f.write(r.text)

    return file_path
