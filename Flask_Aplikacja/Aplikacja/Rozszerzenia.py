from flask import request as REQUEST
from flask_sqlalchemy import SQLAlchemy as SQL_ALCHEMY
from flask_babel import Babel as BABEL

def get_locale():
    """
        Ustawia język, sprawdzając kolejno:
            1) Wartość ciasteczka `Jezyk`
            2) Preferowany język przglądarki użytkownika
    """

    if REQUEST.cookies.get("Jezyk") in ["pl", "en"]:
        Język = REQUEST.cookies.get("Jezyk")
        print("Język: Ciasteczko")
    else:
        Język = REQUEST.accept_languages.best_match(["pl", "en"])
        print("Język: Preferowany Język")

    #Język = "pl"

    print(f"get_locale() --> {Język=}")

    return Język

DB = SQL_ALCHEMY()
Babel = BABEL()