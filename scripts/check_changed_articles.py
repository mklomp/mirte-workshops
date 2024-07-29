import json, sys

# Open the articles.json file
with open('_static/js/articles.json') as file:
    # Parse the JSON data
    data = json.load(file)

# arg1 = list of changed files

changed_files = sys.argv[1] 
changed_files = changed_files.split(" ")
print("Changed files: " + str(changed_files))

# for every article, check that if one of the files is changed, all are changed
for article in data['articles']:
    article_files = []
    for lang in data['languages']:
        article_files.append(f'docs/{article}/{article}.{lang["short"]}.rst')
    # article_files.append(f'docs/{article}/{article}.rst')
    print("Article files: " + str(article_files))
    print([file in changed_files for file in article_files])

    if any(file in changed_files for file in article_files) and not all(file in changed_files for file in article_files):
        print(f'::error title=::All files for article {article} should be changed')
        exit(1)