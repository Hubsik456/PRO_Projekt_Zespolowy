# Do automatycznego generowania dokumentacji
import sys as SYS
from pathlib import Path as PATH
import os
SYS.path.insert(0, str(PATH(__file__).resolve().parents[2]))
SYS.path.insert(0, str(PATH(__file__).resolve().parents[2] / "Flask_Aplikacja"))

print("---")
print(SYS.path)
print("---")


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kurator Kolekcji'
copyright = '2025, Hubert Michna, Patryk Pieniążek'
author = 'Hubert Michna, Patryk Pieniążek'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']

# Dopisane
autodoc_mock_imports = ['Aplikacja']