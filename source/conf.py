# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ardour'
copyright = '2025, The Ardour Team'
author = 'The Ardour Team'
release = '9.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #[...]
    "sphinxcontrib.video",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'renku'
# html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']

# Renku-specific options below
#html_sidebars = {
#    "**": [
#        "globaltoc.html",   # always show global TOC
#        "searchbox.html"
#    ]
#}

# Book theme specific options below
html_theme = "sphinx_book_theme"
html_theme_options = {
    "toc_title": "On this page",
    "show_toc_level": 2,
    "use_repository_button": False,
}

# Multiversion setup
extensions.append("sphinx_multiversion")

# Optional: set what versions to build
smv_tag_whitelist = r'^v\d+\.\d+'     # Build tags like v1.0, v2.1
smv_branch_whitelist = r'^(main|dev)$'  # Or build from main/dev branches
smv_remote_whitelist = r'^origin$'    # Only from origin