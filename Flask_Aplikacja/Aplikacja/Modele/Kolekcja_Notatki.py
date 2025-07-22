"""Model bazy danych dla tabeli 'Notatki'.

Moduł definiuje model SQLAlchemy dla notatek, które można
dodawać do poszczególnych przedmiotów w kolekcji.
"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB


#! Main
class Notatka(DB.Model):
    """Model tabeli 'Notatki' w bazie danych.

    Reprezentuje notatkę powiązaną z konkretnym przedmiotem.

    :ivar int id: Unikalny identyfikator notatki (klucz główny).
    :ivar int id_przedmiot: Klucz obcy wskazujący na przedmiot, do którego należy notatka.
    :ivar str tytul: Tytuł notatki.
    :ivar str opis: Treść notatki.
    :ivar bool czy_prywatne: Flaga określająca, czy notatka jest widoczna publicznie.
    :ivar Przedmiot przedmiot: Relacja do obiektu nadrzędnego Przedmiot.
    """

    __tablename__ = "Notatki"

    id = DB.Column(DB.Integer, primary_key=True)
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"))
    tytul = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)
    czy_prywatne = DB.Column(DB.Boolean)

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="notatki",
        lazy=True,
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Notatka.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Notatka ---> ID: '{self.id}', Tytuł: '{self.tytul}'."
