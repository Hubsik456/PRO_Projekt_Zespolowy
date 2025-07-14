# Blueprint #2 - Konta

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_2 = BLUEPRINT("Blueprint_2", __name__, url_prefix="/konto")

from Aplikacja.Konto import Widoki