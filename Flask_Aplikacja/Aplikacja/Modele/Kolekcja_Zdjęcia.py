"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Zdjecie(DB.Model):
    __tablename__ = "Zdjecia"

    id = DB.Column(DB.Integer, primary_key=True)
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"), nullable=False)
    zdjecie_dane = DB.Column(DB.LargeBinary, nullable=False)
    tytul = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="zdjecia",
        lazy=True
    )

    def __repr__(self):
        return f"Zdjęcie ---> ID: '{self.id}', Tytuł: '{self.tytul}'."