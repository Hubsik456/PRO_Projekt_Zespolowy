"""Model bazy danych dla tabeli 'Zdjecia'.

Moduł definiuje model SQLAlchemy dla zdjęć, które można
przypisać do przedmiotów w kolekcji.
"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB


#! Main
class Zdjecie(DB.Model):
    """Model tabeli 'Zdjecia' w bazie danych.

    Reprezentuje zdjęcie powiązane z konkretnym przedmiotem.

    :ivar int id: Unikalny identyfikator zdjęcia (klucz główny).
    :ivar int id_przedmiot: Klucz obcy wskazujący na przedmiot, do którego należy zdjęcie.
    :ivar bytes zdjecie_dane: Binarne dane pliku graficznego.
    :ivar str tytul: Tytuł zdjęcia.
    :ivar str opis: Opcjonalny opis zdjęcia.
    :ivar str mimetype: Typ MIME pliku (np. 'image/jpeg').
    :ivar Przedmiot przedmiot: Relacja do obiektu nadrzędnego Przedmiot.
    """

    __tablename__ = "Zdjecia"

    id = DB.Column(DB.Integer, primary_key=True)
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"), nullable=False)
    zdjecie_dane = DB.Column(DB.LargeBinary, nullable=False)
    tytul = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)
    mimetype = DB.Column(DB.String(50), nullable=False)  # <--- DODANA KOLUMNA

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="zdjecia",
        lazy=True,
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Zdjecie.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Zdjęcie ---> ID: '{self.id}', Tytuł: '{self.tytul}'."
