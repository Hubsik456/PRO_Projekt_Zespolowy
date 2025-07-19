"""WIP

Widoki (routes) dla Blueprintu #3 - Kolekcja.

Ten moduł zawiera logikę i definicje URL dla wszystkich stron
związanych z zarządzaniem kolekcjami użytkowników.
"""

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, request as REQUEST, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR
from flask_login import login_required as LOGIN_REQUIRED

#! Lokalne importy
from Aplikacja.Kolekcja import Blueprint_3
from Aplikacja.Kolekcja.Formularze.Dodanie_Przedmiotu import Formularz_Dodanie_Przedmiotu

#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """Renderuje stronę główną z kolekcjami użytkownika.

    :return: Wyrenderowany szablon HTML strony głównej kolekcji.
    :rtype: str
    """
    return RENDER_TEMPLATE("Kolekcja/index.html")

@Blueprint_3.route("/podsumowanie/")
def Widok_Kolekcja_Podsumowanie():
    return RENDER_TEMPLATE("Kolekcja/Podsumowanie.html")

@Blueprint_3.route("/kolekcja/<int:ID>")
@LOGIN_REQUIRED
def Widok_Kolekcja_Kolekcja(ID):
    return RENDER_TEMPLATE("Kolekcja/Kolekcja.html", ID=ID)

@Blueprint_3.route("/moja-kolekcja/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Moja_Kolekcja():
    return RENDER_TEMPLATE("Kolekcja/Moja_Kolekcja.html")

@Blueprint_3.route("/moja-kolekcja/dodaj/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Dodaj():
    Formularz = Formularz_Dodanie_Przedmiotu()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Nazwa = Formularz.Pole_Nazwa.data
            Opis = Formularz.Pole_Opis.data
            Cena_Zakupu = Formularz.Pole_Cena_Zakupu.data
            Cena_Zakupu_Waluta = Formularz.Pole_Cena_Zakupu_Waluta.data
            Wartość_Rynkowa = Formularz.Pole_Wartość_Rynkowa.data
            Wartość_Rynkowa_Waluta = Formularz.Pole_Wartość_Rynkowa_Waluta.data
            Kategoria = Formularz.Pole_Kategoria.data
            Czy_Prywatne = Formularz.Pole_Czy_Prywatne.data
            Pola_Własne = Formularz.Pola_Własne.data

            TEMP = [Nazwa, Opis, Cena_Zakupu, Cena_Zakupu_Waluta, Wartość_Rynkowa, Wartość_Rynkowa_Waluta, Kategoria, Czy_Prywatne, Pola_Własne]

            FLASH(f"Dodano nowy przedmiot do Twojej kolekcji.---{TEMP}", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Dodaj.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/edytuj/<int:ID>/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Edytuj(ID):
    return RENDER_TEMPLATE("Kolekcja/Edytuj.hmtl", ID=ID)

@Blueprint_3.route("/moja-kolekcja/usun/<int:ID>")
@LOGIN_REQUIRED
def Widok_Kolekcja_Usuń():
    return RENDER_TEMPLATE("Kolekcja/Usuń.html")
