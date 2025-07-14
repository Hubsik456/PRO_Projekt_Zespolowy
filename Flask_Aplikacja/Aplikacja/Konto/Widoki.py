# Ogólne URL'e i logika związana z kontami użytkowników

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, request as REQUEST
from werkzeug.security import check_password_hash as CHECK_PASSWORD_HASH, generate_password_hash as GENERATE_PASSWORD_HASH
from flask_login import login_user as LOGIN_USER, logout_user as LOGOUT_USER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED, current_user as CURRENT_USER

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB
from Aplikacja.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Konto import Blueprint_2
from Aplikacja.Konto.Formularze.Logowanie import Formularz_Logowanie
from Aplikacja.Konto.Formularze.Rejestracja import Formularz_Rejestracja
from Aplikacja.Konto.Formularze.Zmiana_Hasła import Formularz_Zmiana_Hasła
from Aplikacja.Konto.Formularze.Edytuj_Konto import Formularz_Edytuj_Konto
from Aplikacja.Konto.Formularze.Usuń_Konto import Formularz_Usuń_Konto

#! Main
@Blueprint_2.route("/")
def Widok_Konto_Index():
    """
        Strona główna z kontami użytkowników.
    """

    return RENDER_TEMPLATE("Konto/index.html")

@Blueprint_2.route("/logowanie/", methods=["POST", "GET"])
def Widok_Konto_Logowanie():
    """
        Strona z logowaniem dla zarejestrowanych użytkowników.
    """

    # TODO: Zrobić redirect jeśli ktoś jest już zalogowany

    Formularz = Formularz_Logowanie()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Input_Login = Formularz.Pole_Login.data
            Input_Hasło = Formularz.Pole_Hasło.data

            Użytkownik = Użytkownicy.query.filter_by(Login = Input_Login).first()

            if not Użytkownik or not CHECK_PASSWORD_HASH(Użytkownik.Hasło, Input_Hasło):
                FLASH("Taki użytkownik nie istnieje lub podano niepoprawne hasło.", "danger")
                return RENDER_TEMPLATE("Konto/Logowanie.html", Formularz = Formularz)

            FLASH(f"Zalogowano jako: '{Użytkownik.Login}'.", "success")
            LOGIN_USER(Użytkownik)

            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Konto/Logowanie.html", Formularz = Formularz)

@Blueprint_2.route("/rejestracja/", methods=["POST", "GET"])
def Widok_Konto_Rejestracja():
    """
        Strona z rejestracją dla nowych użytkowników.
    """

    # TODO: Zrobić redirect jeśli ktoś jest już zalogowany

    Formularz = Formularz_Rejestracja()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Input_Login = Formularz.Pole_Login.data
            Input_Hasło = Formularz.Pole_Hasło_1.data
            Input_Email = Formularz.Pole_Email.data

            Użytkownik = Użytkownicy.query.filter_by(Login = Input_Login).first()

            if Użytkownik:
                FLASH("Takie konto już istnieje.", "danger")
                return RENDER_TEMPLATE("Konto/Rejestracja.html", Formularz = Formularz)

            Nowy_Użytkownik = Użytkownicy(Login = Input_Login, Hasło = GENERATE_PASSWORD_HASH(Input_Hasło), Email = Input_Email)
            DB.session.add(Nowy_Użytkownik)
            DB.session.commit()
            LOGIN_USER(Nowy_Użytkownik)
            FLASH("Rejestracja zakońoczna pomyślnie.", "success")

            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Konto/Rejestracja.html", Formularz = Formularz)

@Blueprint_2.route("/zmiana-hasla/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konto_Zmiana_Hasła():
    """
        Strona z formularzem zmiany hasła obecnie zalogowanego użytkownika.
    """

    Formularz = Formularz_Zmiana_Hasła()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()
            Input_Stare_Hasło = Formularz.Pole_Stare_Hasło.data
            Input_Nowe_Hasło = Formularz.Pole_Nowe_Hasło_1.data

            if not Użytkownik or not CHECK_PASSWORD_HASH(Użytkownik.Hasło, Input_Stare_Hasło):
                FLASH("Podano niepoprawne stare hasło.", "danger")
                return RENDER_TEMPLATE("Konto/Zmiana_Hasła.html", Formularz = Formularz)

            Użytkownik.Hasło = GENERATE_PASSWORD_HASH(Input_Nowe_Hasło)
            DB.session.commit()

            FLASH("Hasło zostało zmienione.", "success")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Konto/Zmiana_Hasła.html", Formularz = Formularz)

@Blueprint_2.route("/edytuj-konto/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konto_Edytuj_Konto():
    """
        Strona z formularzem edycji konta obecnie zalogowanego użytkownika.
    """

    Formularz = Formularz_Edytuj_Konto()

    Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Użytkownik.Login = Formularz.Pole_Login.data
            Użytkownik.Email = Formularz.Pole_Email.data
            Użytkownik.Opis = Formularz.Pole_Opis.data

            DB.session.commit()

            FLASH("Zapisano zmiany konta.", "success")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))

        FLASH("Podano niepoprawne dane.", "danger")

    Formularz.Pole_Login.data = Użytkownik.Login
    Formularz.Pole_Email.data = Użytkownik.Email
    Formularz.Pole_Opis.data = Użytkownik.Opis

    return RENDER_TEMPLATE("Konto/Edytuj_Konto.html", Formularz = Formularz)

@Blueprint_2.route("/usun-konto/", methods=["POST", "GET"])
@FRESH_LOGIN_REQUIRED
def Widok_Konto_Usuń_Konto():
    """
        Strona z formularzem usuwania konta obecnie zalogowanego użytkownika.
    """

    Formularz = Formularz_Usuń_Konto()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Użytkownik = Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).first()
            Input_Hasło = Formularz.Pole_Hasło_1.data

            if not Użytkownik or not CHECK_PASSWORD_HASH(Użytkownik.Hasło, Input_Hasło):
                FLASH("Podano niepoprawne hasło.", "danger")
                return RENDER_TEMPLATE("Konto/Usuń_Konto.html", Formularz = Formularz)

            Użytkownicy.query.filter_by(ID = CURRENT_USER.get_id()).delete()
            DB.session.commit()

            FLASH("Twoje konto zostało usunięte.", "success")
            return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))

        FLASH("Podano niepoprawne hasło.", "danger")

    return RENDER_TEMPLATE("Konto/Usuń_Konto.html", Formularz = Formularz)

@Blueprint_2.route("/wyloguj/")
@LOGIN_REQUIRED
def Widok_Konto_Wyloguj():
    """
        Wylogowanie obecnie zalgowanego użytkownika.
    """
    FLASH("Wylogowano.", "info")
    LOGOUT_USER()

    return REDIRECT(URL_FOR("Blueprint_2.Widok_Konto_Index"))
