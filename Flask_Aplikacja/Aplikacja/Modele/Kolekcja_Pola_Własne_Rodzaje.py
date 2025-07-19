"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class PoleWlasneRodzaj(DB.Model):
    __tablename__ = "Pola_Wlasne_Rodzaje"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)
    typ_danych = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)

    # Używamy back_populates tutaj, aby powiązać z relacją 'typ_pola_wlasnego' w PoleWlasne
    # Zmieniona nazwa atrybutu relacji, aby była unikalna i nie kolidowała z 'rodzaj_pola_wlasnego'
    powiazane_pola_wlasne = DB.relationship( # Zmieniono nazwę atrybutu relacji
        "Aplikacja.Modele.Kolekcja_Pola_Własne.PoleWlasne",
        back_populates="typ_pola_wlasnego", # Wskazuje na atrybut relacji w PoleWlasne
        lazy=True
    )

    def __repr__(self):
        return f"Pole Własne Rodzaj ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."