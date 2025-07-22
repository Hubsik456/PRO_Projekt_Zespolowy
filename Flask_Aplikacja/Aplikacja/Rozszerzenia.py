"""Moduł inicjalizujący rozszerzenia Flask.

Centralne miejsce do tworzenia instancji rozszerzeń, które są
następnie importowane i inicjalizowane w głównym pliku aplikacji.
"""

#! Importy Zewnętrzne
# from flask_babel import Babel as BABEL
from flask_sqlalchemy import SQLAlchemy as SQL_ALCHEMY

#! Tłumaczenia
# Babel = BABEL()


# def get_locale():
#     """Określa język interfejsu dla żądania.

#     Sprawdza kolejno:
#     1. Ciasteczko 'Jezyk' ustawione przez użytkownika.
#     2. Nagłówek 'Accept-Language' przeglądarki.
#     3. Domyślną konfigurację aplikacji.

#     :return: Kod języka do użycia (np. 'pl', 'en').
#     :rtype: str
#     """
#     # 1. Ciasteczko
#     if REQUEST.cookies.get("Jezyk") in CURRENT_APP.config["LANGUAGES"]:
#         return REQUEST.cookies.get("Jezyk")
#     # 2. Preferowany język
#     Język = REQUEST.accept_languages.best_match(CURRENT_APP.config["LANGUAGES"])
#     if Język:
#         return Język
#     # 3. Domyślny
#     return CURRENT_APP.config.get("BABEL_DEFAULT_LOCALE", "pl")


#! Baza Danych
DB = SQL_ALCHEMY()
