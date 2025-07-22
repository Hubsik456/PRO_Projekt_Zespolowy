"""Model bazy danych dla tabeli 'Pola_Wlasne_Rodzaje'.

Moduł definiuje model SQLAlchemy dla rodzajów niestandardowych pól,
które użytkownik może tworzyć i przypisywać do przedmiotów.
"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB


#! Main
class PoleWlasneRodzaj(DB.Model):
    """Model tabeli 'Pola_Wlasne_Rodzaje' w bazie danych.

    Definiuje szablon dla niestandardowego pola (np. "Numer seryjny", "Materiał").

    :ivar int id: Unikalny identyfikator rodzaju pola (klucz główny).
    :ivar str nazwa: Nazwa rodzaju pola (np. "Materiał"), musi być unikalna.
    :ivar str typ_danych: Określa typ danych dla tego pola (np. "tekst", "liczba").
    :ivar str opis: Opcjonalny opis rodzaju pola.
    :ivar list powiazane_pola_wlasne: Lista konkretnych wartości pól tego rodzaju.
    """

    __tablename__ = "Pola_Wlasne_Rodzaje"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)
    typ_danych = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)

    powiazane_pola_wlasne = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Pola_Własne.PoleWlasne",
        back_populates="typ_pola_wlasnego",
        lazy=True,
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu PoleWlasneRodzaj.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Pole Własne Rodzaj ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."
