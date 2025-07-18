"""Widoki (routes) dla Blueprintu #3 - Kolekcja.

Ten moduł zawiera logikę i definicje URL dla wszystkich stron
związanych z zarządzaniem kolekcjami użytkowników.
"""

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE

#! Lokalne importy
from Aplikacja.Kolekcja import Blueprint_3


#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """Renderuje stronę główną z kolekcjami użytkownika.

    :return: Wyrenderowany szablon HTML strony głównej kolekcji.
    :rtype: str
    """
    return RENDER_TEMPLATE("Kolekcja/index.html")
