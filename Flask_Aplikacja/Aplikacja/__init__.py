"""Główny plik inicjalizacyjny aplikacji (Application Factory).

Ten moduł zawiera funkcję `create_app`, która jest odpowiedzialna za
tworzenie i konfigurowanie instancji aplikacji Flask.
"""

#! Zewnętrzne Importy
from flask import (
    Flask as FLASK,
    abort as ABORT,
    flash as FLASH,
    render_template as RENDER_TEMPLATE,
    request as REQUEST,
)
from flask_login import (
    LoginManager as LOGIN_MANAGER,
    fresh_login_required as FRESH_LOGIN_REQUIRED,
    login_required as LOGIN_REQUIRED,
)

#! Lokalne Importy
from Konfiguracja import Konfiguracja

from Aplikacja.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Rozszerzenia import DB, Babel, get_locale


#! Funkcje
def create_app(Ustawienia=Konfiguracja):
    """Tworzy i konfiguruje instancję aplikacji Flask.

    Wzorzec "Application Factory" pozwala na tworzenie wielu instancji
    aplikacji z różnymi konfiguracjami, co jest przydatne m.in. do testowania.

    :param Ustawienia: Obiekt konfiguracyjny do użycia.
        Domyślnie `Konfiguracja` z pliku `Konfiguracja.py`.
    :type Ustawienia: object
    :return: Skonfigurowana instancja aplikacji Flask.
    :rtype: flask.Flask
    """
    Aplikacja = FLASK(__name__, template_folder="Szablony", static_folder="Statyczne")
    Aplikacja.config.from_object(Ustawienia)

    #! Baza Danych
    DB.init_app(Aplikacja)

    #! Konta Użytkowników
    Login_Manager = LOGIN_MANAGER()
    Login_Manager.login_view = "Blueprint_2.Widok_Konto_Logowanie"
    Login_Manager.login_message = "Ta strona jest dostępna tylko dla zalogowanych użytkowników. Jeśli nie masz konta, musisz się zarejstrować."
    Login_Manager.login_message_category = "info"
    Login_Manager.init_app(Aplikacja)

    @Login_Manager.user_loader
    def load_user(user_id):
        """Wczytuje użytkownika na podstawie jego ID, wymagane przez Flask-Login.

        :param user_id: ID użytkownika do wczytania.
        :type user_id: str
        :return: Obiekt użytkownika lub None, jeśli nie znaleziono.
        :rtype: Użytkownicy or None
        """
        return Użytkownicy.query.get(int(user_id))

    #! Tłumaczenia
    Babel.init_app(Aplikacja, locale_selector=get_locale)

    #! Blueprint'y
    from Aplikacja.CLI import Blueprint_CLI

    Aplikacja.register_blueprint(Blueprint_CLI)

    from Aplikacja.Debug import Blueprint_0 as Blueprint_Debug

    Aplikacja.register_blueprint(Blueprint_Debug)

    from Aplikacja.Main import Blueprint_1 as Blueprint_Main

    Aplikacja.register_blueprint(Blueprint_Main)

    from Aplikacja.Konto import Blueprint_2 as Blueprint_Konto

    Aplikacja.register_blueprint(Blueprint_Konto)

    from Aplikacja.Kolekcja import Blueprint_3 as Blueprint_Kolekcja

    Aplikacja.register_blueprint(Blueprint_Kolekcja)

    #! Obsługa Błędów
    @Aplikacja.errorhandler(401)
    def Błąd_401(Błąd):
        """Obsługuje błąd 401 (Unauthorized).

        :param Błąd: Obiekt błędu.
        :return: Wyrenderowany szablon błędu 401.
        :rtype: tuple
        """
        return RENDER_TEMPLATE("Błędy/401.html"), 401

    @Aplikacja.errorhandler(404)
    def Błąd_404(Błąd):
        """Obsługuje błąd 404 (Not Found).

        :param Błąd: Obiekt błędu.
        :return: Wyrenderowany szablon błędu 404.
        :rtype: tuple
        """
        return RENDER_TEMPLATE("Błędy/404.html"), 404

    @Aplikacja.errorhandler(500)
    def Błąd_500(Błąd):
        """Obsługuje błąd 500 (Internal Server Error).

        :param Błąd: Obiekt błędu.
        :return: Wyrenderowany szablon błędu 500.
        :rtype: tuple
        """
        return RENDER_TEMPLATE("Błędy/500.html"), 500

    #! Jinja2
    @Aplikacja.context_processor
    def Jinja2_Zmienne_Globalne():
        """Dodaje zmienne globalne do kontekstu szablonów Jinja2.

        Udostępnia w szablonach informacje o aktualnym motywie,
        trybie ciemnym i języku na podstawie ciasteczek.

        :return: Słownik ze zmiennymi globalnymi.
        :rtype: dict
        """
        from Aplikacja.Main.Formularze.Wybór_Motywu import Formularz_Wyboru_Motywu

        Dostępne_Motywy = [
            Wartość
            for Wartość, Klucz in Formularz_Wyboru_Motywu.Pole_Motyw.kwargs["choices"]
        ]

        Zmienne_Globalne = {
            "Tryb_Ciemny": REQUEST.cookies.get("Tryb_Ciemny"),
            "Motyw": REQUEST.cookies.get("Motyw")
            if REQUEST.cookies.get("Motyw") in Dostępne_Motywy
            else "united",
            "Język": get_locale(),
        }
        return dict(Zmienne_Globalne)

    return Aplikacja
