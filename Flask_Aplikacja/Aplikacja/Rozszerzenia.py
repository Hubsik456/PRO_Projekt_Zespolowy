# Rozszerzenia aplikacji

#! Importy Zewnętrzne
from flask import request as REQUEST, current_app as CURRENT_APP
from flask_sqlalchemy import SQLAlchemy as SQL_ALCHEMY
from flask_babel import Babel as BABEL

#! Tłumaczenia
Babel = BABEL()
def get_locale():
    """
        Ustawia język, sprawdzając kolejno:
            1) Wartość ciasteczka `Jezyk`.
            2) Preferowany język przglądarki użytkownika.
            3) Domyślny język
    """

    if REQUEST.cookies.get("Jezyk") in CURRENT_APP.config["LANGUAGES"]:
        Język = REQUEST.cookies.get("Jezyk")

        print("Język: Ciasteczko")
        print(f"get_locale() --> {Język=}")

        return Język

    else:
        Język = REQUEST.accept_languages.best_match(CURRENT_APP.config['LANGUAGES'])

        print("Język: Preferowany Język")
        print(f"get_locale() --> {Język=}")

        if Język:
            return Język

    Domyślny_Język = CURRENT_APP.config.get("BABEL_DEFAULT_LOCALE", "pl")
    return Domyślny_Język

#! Baza Danych
DB = SQL_ALCHEMY()