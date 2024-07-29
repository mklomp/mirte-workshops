import json

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

# get current script path
import os
script_path = os.path.dirname(os.path.realpath(__file__))
root = os.path.join(script_path, '..')

# for every article and every language, check that the file exists
for article in data['articles']:
    for lang in data['languages']:
        # Check if the file exists
        try:
            with open(f'{root}/docs/{article}/{article}.{lang["short"]}.rst') as file:
                print("File exists: " + f'{root}/docs/{article}/{article}.{lang["short"]}.rst')
                pass
        except FileNotFoundError:
            print(f'::error {root}/docs/{article}/{article}.{lang["short"]}.rst missing')
            # exit(1)