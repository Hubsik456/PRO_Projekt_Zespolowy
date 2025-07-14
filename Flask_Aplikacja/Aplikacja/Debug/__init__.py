# Blueprint #0 - Debug'owanie/Testowanie

#! Zewnętrzne Importy
from flask import Blueprint as BLUEPRINT

#! Main
Blueprint_0 = BLUEPRINT("Blueprint_0", __name__, url_prefix="/debug")

from Aplikacja.Debug import Widoki