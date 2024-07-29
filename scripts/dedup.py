


# open all .html files in build/html/en and change "images/" to "../images/" and "_static/" to "../_static/"

import os

script_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath( f'{script_path}/../_build/html/en')
html_files = []
for root, dirs, files in list(os.walk(folder_path)):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))


# replace "images/" with "../images/" and "_static/" with "../_static/"
for file in html_files:
    with open(file, 'r+') as f:
        t = f.read()
        t = t.replace("_images/", "../_images/").replace("_static/", "../_static/")
        f.seek(0)
        f.write(t)
        f.truncate()
        # print("t2", t.replace("images/", "../images/").replace("_static/", "../_static/"))
        # f.write(t.replace("images/", "../images/").replace("_static/", "../_static/"))


# delete _images and _static
import shutil
shutil.rmtree(f'{folder_path}/_images')
shutil.rmtree(f'{folder_path}/_static')