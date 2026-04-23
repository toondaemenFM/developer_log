# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'TOON DAEMEN'
copyright = '2026, Flanders Make vzw'
author = 'Flanders Make vzw'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
]

numfig = True
numfig_format = {'figure': 'Figure %s'}
numfig_secnum_depth = 1


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['img']
html_logo = "img/fm.svg"
html_favicon = "img/fm_48x48.svg"

html_show_sphinx = False

html_context = {
    "display_github": True,
    "github_user": "toondaemenFM",
    "github_repo": "implementation_best_practices",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

footnote_backlinks = False
