"""Inicjalizacja Blueprintu #1 - Main.

Ten moduł jest odpowiedzialny za stworzenie i skonfigurowanie
głównego Blueprintu aplikacji, obsługującego ogólne widoki.
"""

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_1 = BLUEPRINT("Blueprint_1", __name__)

from Aplikacja.Main import Widoki
