# "Application Factory"

#! Zewnętrzne Importy
from flask import Flask as FLASK, flash as FLASH, render_template as RENDER_TEMPLATE, abort as ABORT, request as REQUEST
from flask_login import LoginManager as LOGIN_MANAGER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED
# from flask_babel import Babel as BABEL

#! Lokalne Importy
from Konfiguracja import Konfiguracja
from Aplikacja.Rozszerzenia import DB, Babel, get_locale
from Aplikacja.Modele.Użytkownicy import Użytkownicy

#! Funkcje
def create_app(Ustawienia = Konfiguracja):
    Aplikacja = FLASK(__name__, template_folder="Szablony", static_folder="Statyczne")
    Aplikacja.config.from_object(Ustawienia)

    #! Baza Danych
    DB.init_app(Aplikacja)

    #! Konta Użytkowników
    # TODO:
    Login_Manager = LOGIN_MANAGER()
    Login_Manager.login_view = "Blueprint_2.Widok_Konto_Logowanie"
    Login_Manager.login_message = "Ta strona jest dostępna tylko dla zalogowanych użytkowników. Jeśli nie masz konta, musisz się zarejstrować."
    Login_Manager.login_message_category = "info"
    Login_Manager.init_app(Aplikacja)

    @Login_Manager.user_loader
    def load_user(user_id):
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
    # TODO: Dodać pozostałe błędy HTTP
    @Aplikacja.errorhandler(401)
    def Błąd_401(Błąd):
        return RENDER_TEMPLATE("Błędy/401.html"), 401

    @Aplikacja.errorhandler(404)
    def Błąd_404(Błąd):
        return RENDER_TEMPLATE("Błędy/404.html"), 404

    @Aplikacja.errorhandler(500)
    def Błąd_500(Błąd):
        return RENDER_TEMPLATE("Błędy/500.html"), 500

    #! Jinja2
    @Aplikacja.context_processor
    def Jinja2_Zmienne_Globalne():
        """
            Dodanie niektórych zmiennych do zmiennych globalnych, tak żeby można je było wykorzystać w szablonach Jinja2.
        """

        Zmienne_Globalne = {
            "Tryb_Ciemny": REQUEST.cookies.get("Tryb_Ciemny"),
            "Język": get_locale(),
        }

        print(f"{Zmienne_Globalne=}")

        return dict(Zmienne_Globalne)

    #! Koniec
    return Aplikacja