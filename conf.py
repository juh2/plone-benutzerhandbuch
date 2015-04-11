# -*- coding: utf-8 -*-
#
# Plone-Benutzerhandbuch documentation build configuration file, created by
# sphinx-quickstart on Sat Jun 26 13:12:58 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import datetime
import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.ifconfig']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Plone-Benutzerhandbuch'
thisyear = datetime.datetime.now().year
copyright = u'2010 – %s, Jan Ulrich Hasecke, Creative Commons Lizenz 2.0 BY-NC-SA' % thisyear

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '4.3'
# The full version, including alpha/beta/rc tags.
release = '4.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'de'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# -- Options for HTML output ---------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'plone_org_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {
#
#'source_link_position': "footer",
#'globaltoc_depth': 2
#
#}

# Add any paths that contain custom themes here, relative to this directory.

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Plone Benutzerhandbuch (Deutsche Dokumentation)' 

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/plone-icon-24.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'http://www.hasecke.com/plone-benutzerhandbuch/4.3/'

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Plonedoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '12pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Plone-Benutzerhandbuch-4.3.tex', u'Plone-Benutzerhandbuch',
   u'Jan Ulrich Hasecke', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/plone-logo.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
latex_preamble = '''
\usepackage{lscape}
\usepackage{microtype}
\usepackage{tgtermes}
\usepackage[T1]{fontenc}
\setlength{\paperwidth}{191.000mm} 
\setlength{\paperheight}{235.000mm} 
\setlength{\pdfpagewidth}{\paperwidth} 
\setlength{\pdfpageheight}{\paperheight}
\\typearea[10mm]{14}
\definecolor{TitleColor}{rgb}{0,0,0}
\definecolor{InnerLinkColor}{rgb}{0,0,0}
\setcounter{secnumdepth}{0}
\makeatletter
\\fancypagestyle{normal}{%
\\fancyhf{}%
\\fancyfoot[LE,RO]{{\em\\thepage}}%
\\fancyhead[RO]{{\em\\nouppercase{\\rightmark}}}%
\\fancyhead[LE]{{\em\\nouppercase{\leftmark}}}%
\\renewcommand{\headrulewidth}{0pt}%
\\renewcommand{\\footrulewidth}{0pt}%
}
\\fancypagestyle{plain}{%
\\fancyhf{}%
\\fancyfoot[LE,RO]{{\em\\thepage}}%
\\fancyhead[LE,RO]{} % here's the change
\\renewcommand{\headrulewidth}{0pt}%
\\renewcommand{\\footrulewidth}{0pt}%
}
\makeatother
\clubpenalty = 10000
\widowpenalty = 10000
'''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

latex_elements = {
    'pointsize':'12pt',
    'docclass':'scrreprt'
    }

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'plone-benutzerhandbuch', u'Plone-Benutzerhandbuch',
     [u'Jan Ulrich Hasecke'], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Plone-Benutzerhandbuch 4.3'
epub_author = u'Jan Ulrich Hasecke'
epub_publisher = u'Jan Ulrich Hasecke'
epub_copyright = u'2010 – %s, Jan Ulrich Hasecke, Creative Commons Lizenz 2.0 BY-NC-SA' % thisyear

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = 'german'

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'http://www.hasecke.com/plone-benutzerhandbuch/4.3'

# A unique identification for the text.
#epub_uid = ''

# Titelbild
epub_cover = ('_static/cover.png', '')

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Scale large images.
epub_max_image_width = 600

epub_theme_options = {'relbar1': False, 'footer': False}

# -- Sonstige Options ---------------------------------------------------

todo_include_todos = True
