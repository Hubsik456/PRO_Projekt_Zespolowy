# Dokumentacja/source/conf.py

import os
import sys

# Wskazanie Sphinxowi, gdzie znajduje się kod aplikacji
# Wychodzimy dwa katalogi w górę (do PRO_Projekt_Zespolowy-main), a potem wchodzimy do Flask_Aplikacja
sys.path.insert(0, os.path.abspath("../../Flask_Aplikacja"))


# -- Informacje o projekcie ---------------------------------------------------

project = "Kurator Kolekcji"
copyright = "2025, Hubert Michna, Patryk Pieniążek"
author = "Hubert Michna, Patryk Pieniążek"
release = "1.0"

# -- Konfiguracja ogólna -----------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",  # Automatyczne generowanie z docstringów
    "sphinx.ext.viewcode",  # Dodaje linki do kodu źródłowego
    "sphinx.ext.napoleon",  # Obsługa docstringów w stylu Google
]

templates_path = ["_templates"]
exclude_patterns = []
language = "pl"

# -- Opcje dla wyjścia HTML --------------------------------------------------

# Używamy popularnego motywu "Read the Docs"
html_theme = "furo"
# html_static_path = ["_static"]

# Opcje dla autodoc
autodoc_member_order = "bysource"  # Sortuj elementy wg kolejności w kodzie
