"""Inicjalizacja Blueprintu #2 - Konta.

Ten moduł jest odpowiedzialny za stworzenie i skonfigurowanie
Blueprintu dla funkcjonalności związanych z kontami użytkowników.
"""

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_2 = BLUEPRINT("Blueprint_2", __name__, url_prefix="/konto")

from Aplikacja.Konto import Widoki
