# Blueprint #3 - Kolekcja

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_3 = BLUEPRINT("Blueprint_3", __name__, url_prefix="/kolekcja")

from Aplikacja.Kolekcja import Widoki
