import os

import requests
import re


def download(url, folder):
    r = requests.get(url)
    
    print('\nurl:', url)
    n = re.sub('(html?)$', '', url)
    print('\n^htm:', n)
    file_name = re.sub('\W+', '-', n)
    print('\nfname:', file_name)
    
    file_path = os.path.join(folder, f'{file_name}.html')
    with open(file_path, "w") as f:
        f.write(r.text)
    
    return file_path
