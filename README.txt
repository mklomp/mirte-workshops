$ python3 -m venv docs-env
$ source docs-env/bin/activate
(docs-env)$ pip install sphinx furo sphinx-panels
(docs-env)$ mkdir _modules
(docs-env)$ cd _modules
(docs-env)$ git clone https://github.com/sphinx-contrib/video.git
(docs-env)$ cd video
(docs-env)$ pip install .
(docs-env)$ make html
(docs-env)$ python3 -m http.server


$ firefox _build/html/index.html
