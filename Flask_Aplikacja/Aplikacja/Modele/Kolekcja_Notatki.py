"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Notatka(DB.Model):
    __tablename__ = "Notatki"

    id = DB.Column(DB.Integer, primary_key=True)
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"))
    tytul = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)
    czy_prywatne = DB.Column(DB.Boolean)

    # Zmieniamy 'backref' na 'back_populates' i wskazujemy na atrybut relacji w klasie Przedmiot.
    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="notatki", # <-- Teraz back_populates wskazuje na istniejącą relację "notatki" w Przedmiot
        lazy=True
    )

    def __repr__(self):
        return f"Notatka ---> ID: '{self.id}', Tytuł: '{self.tytul}'."