import os
import sys

import pytest
from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Aplikacja import DB, create_app
from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Użytkownicy import Uzytkownik
from Konfiguracja import KonfiguracjaTestowa


@pytest.fixture(scope="module")
def app():
    """Tworzy instancję aplikacji na potrzeby modułu testowego."""
    app = create_app(Ustawienia=KonfiguracjaTestowa)
    with app.app_context():
        DB.create_all()
        yield app
        DB.session.remove()
        DB.drop_all()


@pytest.fixture(scope="function")
def client(app):
    """Tworzy klienta testowego dla aplikacji."""
    return app.test_client()


@pytest.fixture(scope="function")
def init_database(app):
    """
    Inicjalizuje bazę danych przed każdym testem, wstawia dane testowe i czyści ją po zakończeniu.
    """

    uzytkownik1 = Uzytkownik(
        login="testuser1",
        email="test1@example.com",
        haslo=generate_password_hash("password123"),
    )
    kategoria1 = Kategoria(nazwa="Elektronika", opis="Urządzenia elektroniczne")
    waluta1 = Waluta(skrot="PLN", nazwa="Polski Złoty")
    pwr1 = PoleWlasneRodzaj(id=1, nazwa="Stan", typ_danych="Tekst")

    DB.session.add_all([uzytkownik1, kategoria1, waluta1, pwr1])
    DB.session.commit()

    przedmiot1 = Przedmiot(
        nazwa="Laptop",
        opis="Używany laptop",
        wlasciciel=uzytkownik1,
        kategoria=kategoria1,
        cena_zakupu=2500.00,
        id_cena_zakupu_waluta=waluta1.id,
        wartosc_rynkowa=2000.00,
        id_wartosc_rynkowa_waluta=waluta1.id,
        czy_prywatne=False,
    )
    DB.session.add(przedmiot1)
    DB.session.commit()

    yield DB

    DB.session.remove()
    DB.drop_all()

    DB.create_all()
