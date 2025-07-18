# URL'e i logika związana z kolekcjami użytkowników

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE

#! Lokalne importy
from Aplikacja.Kolekcja import Blueprint_3


#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """
    Strona główna z kolekcjami użytkowników.
    """

    return RENDER_TEMPLATE("Kolekcja/index.html")
