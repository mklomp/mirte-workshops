import json, os, shutil, argparse

parser = argparse.ArgumentParser(description="Build script")
parser.add_argument('--dir', required=True, help='Directory to the workshop directory (located in docs/workshops) to build')
parser.add_argument('--lang', required=False, help='Language to build (default: all)')
args = parser.parse_args()

# Add symlinks to all the modules
os.system(f'ln -s ../../modules ./docs/workshops/{args.dir}')
os.system(f'ln -s ../../../_static ./docs/workshops/{args.dir}')
os.system(f'ln -s ../../../_templates ./docs/workshops/{args.dir}')
os.system(f'ln -s ../../../conf.py ./docs/workshops/{args.dir}')
#TODO: include conf.py locally so author can be overridden


# Open the articles.json file
data = {}
if (not args.lang):
    with open('_static/js/articles.json') as file:
        # Parse the JSON data
        data = json.load(file)
else:
    data['languages'] = [{'short': args.lang}]

for lang in data['languages']:
    os.system(f'sphinx-build "./docs/workshops/{args.dir}" "_build/html/{lang["short"]}/{args.dir}" -t lang_{lang["short"]}')

shutil.copyfile('scripts/index.html', '_build/html/index.html')

# Remove symlink to all modules
os.system(f'rm ./docs/workshops/{args.dir}/modules')
os.system(f'rm ./docs/workshops/{args.dir}/_static')
os.system(f'rm ./docs/workshops/{args.dir}/_templates')
os.system(f'rm ./docs/workshops/{args.dir}/conf.py')
