from flask import request as REQUEST
from flask_sqlalchemy import SQLAlchemy as SQL_ALCHEMY
from flask_babel import Babel as BABEL

def get_locale():
    Język = REQUEST.accept_languages.best_match(["pl", "en"])
    #Język = "en"

    print(f"Wybrany język: '{Język}'.")

    return Język

DB = SQL_ALCHEMY()
Babel = BABEL()