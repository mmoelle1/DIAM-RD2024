# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "DIAM-RD2024"
copyright = "2024, Matthias Möller"
author = "Matthias Möller"
release = "2024"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

extensions = [
]


templates_path = ["_templates"]
exclude_patterns = []

pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_title  = "DIAM Research Day 2024"
html_static_path = ["_static"]
