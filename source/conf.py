# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "The UMH"
author = "Ubuntu Contributors"
copyright = f"2022 {author}"
release = "1.0"


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'basic'
html_short_title = project

# Some customization of the theme to show GitHub links, a limited amount of the
# global ToC, and no source links (other than the GitHub ones)
html_theme_options = {
    'globaltoc_maxdepth': 2,
}

html_context = {
    'display_github': True,
    'github_user': 'waveform80',
    'github_repo': 'ubuntu-maintainers-handbook',
    'github_version': 'rest',
    'conf_py_path': '/source/',
}
html_show_sourcelink = False
html_last_updated_fmt = '%A, %d %B %Y'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {'**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html']}

# Link :manpage: directives to the Ubuntu manpages archive. Technically, this
# is a universal option but is currently only implemented for HTML writers,
# hence why it is under HTML options here
manpages_url = 'https://manpages.ubuntu.com/manpages/focal/en/man{section}/{page}.{section}.html'
