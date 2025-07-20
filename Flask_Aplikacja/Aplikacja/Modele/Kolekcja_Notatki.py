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

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="notatki",
        lazy=True
    )

    def __repr__(self):
        return f"Notatka ---> ID: '{self.id}', Tytuł: '{self.tytul}'."