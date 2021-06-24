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


# -- Project information -----------------------------------------------------

project = '杰理开源文档'
copyright = '2021, Jieli'
author = 'Jieli'

# The full version, including alpha/beta/rc tags
release = 'v0.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['breathe']

# breathe settings
breathe_projects = {
        "adapter_sdk": "doxygen_out/xml",
}

breathe_default_project = "adapter_sdk"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# import sphinx_rtd_theme
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
}
html_title = "JL Project Documentation"
# html_logo = "_static/images/jl_logo.png"
# html_logo = "_static/images/logo.svg"
# html_favicon = "images/zp_favicon.png"
html_last_updated_fmt = "%b %d, %Y"
html_domain_indices = False
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
# html_search_scorer = "_static/js/scorer.js"

# is_release = tags.has("release")  # pylint: disable=undefined-variable
# docs_title = "Docs / {}".format(version if is_release else "Latest")
# html_context = {
    # "show_license": True,
    # "versions": (
        # ("latest", "/"),
        # ("2.6.0", "/2.6.0/"),
        # ("2.5.0", "/2.5.0/"),
        # ("2.4.0", "/2.4.0/"),
        # ("2.3.0", "/2.3.0/"),
        # ("2.2.0", "/2.2.0/"),
        # ("1.14.1", "/1.14.1/"),
    # ),
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


