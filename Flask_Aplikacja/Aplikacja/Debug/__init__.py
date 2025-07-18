"""Inicjalizacja Blueprintu #0 - Debug.

Ten moduł jest odpowiedzialny za stworzenie i skonfigurowanie
Blueprintu dla funkcjonalności związanych z debugowaniem i testowaniem aplikacji.
"""

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_0 = BLUEPRINT("Blueprint_0", __name__, url_prefix="/debug")

from Aplikacja.Debug import Widoki
