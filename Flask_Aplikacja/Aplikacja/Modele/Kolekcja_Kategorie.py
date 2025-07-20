"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Kategoria(DB.Model):
    __tablename__ = "Kategorie"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)
    opis = DB.Column(DB.Text)

    przedmioty = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="kategoria",
        lazy=True
    )

    def __repr__(self):
        return f"Kategoria ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."