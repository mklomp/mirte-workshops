# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import glob


# -- Project information -----------------------------------------------------

project = 'Mirte Workshops'
#copyright = '2023, Martin Klomp, TU Delft Robotics Institute'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.video', 'sphinx_design']

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_modules', 'docs-env']


# intl
locale_dirs = glob.glob('./docs/*/_locale/')
locale_dirs.append('locale/')
print(locale_dirs)
gettext_compact = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_book_theme'
html_title = "Mirte Workshops"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# For now all videos need to be placed in /_static due to this issue:
# https://github.com/sphinx-contrib/video/issues/33

html_js_files = ['js/custom.js']

html_css_files = [
      "css/custom.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css",
]

## For Book Theme
html_context = {
   "mode": "darky"
}

html_theme_options = {
    "use_download_button": False,
    "repository_url": "https://github.com/mirte-robot/mirte-workshops",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": False,
    "extra_footer": "&copy; 2023, Martin Klomp, <a href='https://tudelftroboticsinstitute.nl/'>TU Delft Robotics Institute</a>",
}
