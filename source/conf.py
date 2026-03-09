# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'neuromeka experience guide'
copyright = '2026, RISE LAB'
author = 'RISE LAB'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

try:
    import sphinx_rtd_theme  # noqa: F401
    html_theme = 'sphinx_rtd_theme'
except ModuleNotFoundError:
    html_theme = 'alabaster'

html_static_path = ['_static']
html_copy_source = False
html_show_sourcelink = False
html_logo = '_static/logo.png'
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
}
