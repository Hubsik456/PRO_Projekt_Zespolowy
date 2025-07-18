"""Inicjalizacja Blueprintu #3 - Kolekcja.

Ten moduł jest odpowiedzialny za stworzenie i skonfigurowanie
Blueprintu dla funkcjonalności związanych z kolekcjami użytkownika.
"""

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_3 = BLUEPRINT("Blueprint_3", __name__, url_prefix="/kolekcja")

from Aplikacja.Kolekcja import Widoki
