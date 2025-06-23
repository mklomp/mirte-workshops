import json, os, shutil
from pathlib import Path

BUILD_DIR = Path("_build/html")

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

for lang in data['languages']:
    os.system(f'sphinx-build "." "_build/html/{lang["short"]}" -t lang_{lang["short"]}')

shutil.copyfile('scripts/index.html', '_build/html/index.html')
