"""Model bazy danych dla tabeli 'Kategorie'.

Moduł definiuje model SQLAlchemy dla kategorii, do których mogą być
przypisywane przedmioty z kolekcji.
"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB


#! Main
class Kategoria(DB.Model):
    """Model tabeli 'Kategorie' w bazie danych.

    Reprezentuje kategorię, którą można przypisać do przedmiotu.

    :ivar int id: Unikalny identyfikator kategorii (klucz główny).
    :ivar str nazwa: Nazwa kategorii, musi być unikalna.
    :ivar str opis: Opcjonalny, dłuższy opis kategorii.
    :ivar list przedmioty: Lista przedmiotów powiązanych z tą kategorią.
    """

    __tablename__ = "Kategorie"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)
    opis = DB.Column(DB.Text)

    przedmioty = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="kategoria",
        lazy=True,
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Kategoria.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Kategoria ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."
