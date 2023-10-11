###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = 'Pantelis Monogioudis, Ph.D'
bibtex_bibfiles = ['ai.bib']
bibtex_reference_style = 'author_year'
comments_config = {'hypothesis': False, 'utterances': False}
copyright = '2023'
exclude_patterns = ['**.ipynb_checkpoints', '.DS_Store', 'Thumbs.db', '_build']
extensions = ['sphinx_togglebutton', 'sphinx_copybutton', 'myst_nb', 'jupyter_book', 'sphinx_thebe', 'sphinx_comments', 'sphinx_external_toc', 'sphinx.ext.intersphinx', 'sphinx_design', 'sphinx_book_theme', 'sphinxcontrib.youtube', 'sphinxcontrib.inkscapeconverter', 'sphinxcontrib.bibtex', 'sphinx_jupyterbook_latex']
external_toc_exclude_missing = True
external_toc_path = '_toc.yml'
html_baseurl = 'https://pantelis.github.io/lab'
html_favicon = './logo.ico'
html_logo = './logo.png'
html_sidebars = {'lab/*': []}
html_sourcelink_suffix = ''
html_theme = 'sphinx_book_theme'
html_theme_options = {'search_bar_text': 'Search this book...', 'launch_buttons': {'notebook_interface': 'classic', 'binderhub_url': 'https://mybinder.org', 'jupyterhub_url': '', 'thebe': True, 'colab_url': 'https://colab.research.google.com'}, 'path_to_docs': 'lab', 'repository_url': 'https://github.com/pantelis/lab', 'repository_branch': 'master', 'extra_footer': '', 'home_page_in_toc': True, 'announcement': '', 'analytics': {'google_analytics_id': ''}, 'use_repository_button': True, 'use_edit_page_button': True, 'use_issues_button': True, 'use_download_button': True, 'show_navbar_depth': 1, 'intersphinx_mapping': None, 'python': ['https://docs.python.org/3/', None], 'numpy': ['https://numpy.org/doc/stable/', None], 'pandas': ['https://pandas.pydata.org/docs/', None], 'scikit-learn': ['https://scikit-learn.org/stable/', None], 'torch': ['https://pytorch.org/docs/master/', None], 'tf2': ['https://pytorch.org/docs/master/', None]}
html_title = 'Lab'
latex_elements = {'preamble': '\\newcommand\\N{\\mathbb{N}}\n\\newcommand\\floor[1]{\\lfloor#1\\rfloor}\n\\newcommand{\\bmat}{\\left[\\begin{array}}\n\\newcommand{\\emat}{\\end{array}\\right]}\n'}
latex_engine = 'xelatex'
mathjax3_config = {'tex': {'macros': {'floor': ['\\lfloor#1\\rfloor', 1], 'bmat': ['\\left[\\begin{array}'], 'emat': ['\\end{array}\\right]']}}}
myst_enable_extensions = ['amsmath', 'deflist', 'colon_fence', 'dollarmath', 'html_admonition', 'html_image', 'linkify', 'replacements', 'smartquotes', 'substitution']
myst_url_schemes = ['mailto', 'http', 'https']
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_show_tb = True
nb_execution_timeout = 3600
nb_merge_streams = True
nb_output_stderr = 'show'
numfig = True
pygments_style = 'sphinx'
suppress_warnings = ['myst.domains']
use_jupyterbook_latex = True
use_multitoc_numbering = True
