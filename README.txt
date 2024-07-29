$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install -r requirements.txt
(docs-env)$ make build_lang
(docs-env)$ python3 -m http.server


$ firefox _build/html/index.html


requires python3.10 for sphinx==7.4.7