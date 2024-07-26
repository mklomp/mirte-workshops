$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install sphinx sphinx-book-theme sphinx-design sphinxcontrib-video
(docs-env)$ make html
(docs-env)$ python3 -m http.server


$ firefox _build/html/index.html


requires python3.10 for sphinx==7.4.7