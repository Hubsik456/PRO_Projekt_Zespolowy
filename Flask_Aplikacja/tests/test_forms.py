from io import BytesIO

import pytest
from Aplikacja.Kolekcja.Formularze.Dodanie_Przedmiotu import (
    Formularz_Dodanie_Przedmiotu,
)
from Aplikacja.Kolekcja.Formularze.Notatka import Formularz_Notatka
from Aplikacja.Kolekcja.Formularze.Zdjęcie import Formularz_Zdjecie
from Aplikacja.Konto.Formularze.Edytuj_Konto import Formularz_Edytuj_Konto
from Aplikacja.Konto.Formularze.Logowanie import Formularz_Logowanie
from Aplikacja.Konto.Formularze.Rejestracja import Formularz_Rejestracja
from Aplikacja.Konto.Formularze.Zmiana_Hasła import Formularz_Zmiana_Hasła
from werkzeug.datastructures import FileStorage


@pytest.mark.usefixtures("app")
class TestFormularzeKonta:
    """Grupa testów dla formularzy z modułu Konto."""

    def test_rejestracja_poprawne_dane(self):
        form = Formularz_Rejestracja(
            Pole_Login="nowy_user",
            Pole_Hasło_1="bardzo_trudne_haslo",
            Pole_Hasło_2="bardzo_trudne_haslo",
            Pole_Email="user@example.com",
        )
        assert form.validate() is True

    def test_rejestracja_niesparowane_hasla(self):
        form = Formularz_Rejestracja(
            Pole_Login="nowy_user", Pole_Hasło_1="haslo1", Pole_Hasło_2="haslo2"
        )
        assert form.validate() is False
        assert "Podane hasła muszą być identyczne." in form.Pole_Hasło_1.errors

    def test_rejestracja_za_krotki_login(self):
        form = Formularz_Rejestracja(
            Pole_Login="user", Pole_Hasło_1="password123", Pole_Hasło_2="password123"
        )
        assert form.validate() is False
        assert "Login musi mieć od 5 do 100 znaków." in form.Pole_Login.errors

    def test_logowanie_poprawne_dane(self):
        form = Formularz_Logowanie(Pole_Login="testuser", Pole_Hasło="password123")
        assert form.validate() is True

    def test_logowanie_brak_hasla(self):
        form = Formularz_Logowanie(Pole_Login="testuser", Pole_Hasło="")
        assert form.validate() is False
        assert "Pole z hasłem nie może być puste." in form.Pole_Hasło.errors

    def test_zmiana_hasla_poprawne_dane(self):
        form = Formularz_Zmiana_Hasła(
            Pole_Stare_Hasło="starehaslo123",
            Pole_Nowe_Hasło_1="nowehaslo123",
            Pole_Nowe_Hasło_2="nowehaslo123",
        )
        assert form.validate() is True

    def test_edycja_konta_poprawne_dane(self):
        form = Formularz_Edytuj_Konto(
            Pole_Login="zmieniony_login",
            Pole_Email="nowy@email.com",
            Pole_Opis="Nowy opis profilu",
        )
        assert form.validate() is True


@pytest.mark.usefixtures("app")
class TestFormularzeKolekcji:
    """Grupa testów dla formularzy z modułu Kolekcja."""

    def test_dodanie_przedmiotu_poprawne_dane(self):
        form = Formularz_Dodanie_Przedmiotu(
            nazwa="Stara moneta",
            opis="Opis monety",
            cena_zakupu=100.50,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=150.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=1,
        )

        form.id_cena_zakupu_waluta.choices = [(1, "PLN"), (2, "USD")]
        form.id_wartosc_rynkowa_waluta.choices = [(1, "PLN"), (2, "USD")]
        form.id_kategoria.choices = [(1, "Numizmatyka"), (2, "Elektronika")]

        assert form.validate() is True

    def test_dodanie_przedmiotu_ujemna_cena(self):
        form = Formularz_Dodanie_Przedmiotu(
            nazwa="Stara moneta",
            cena_zakupu=-50,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=150.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=1,
        )

        form.id_cena_zakupu_waluta.choices = [(1, "PLN")]
        form.id_wartosc_rynkowa_waluta.choices = [(1, "PLN")]
        form.id_kategoria.choices = [(1, "Numizmatyka")]

        assert form.validate() is False
        assert "Cena nie może być ujemna." in form.cena_zakupu.errors

    def test_notatka_poprawne_dane(self):
        form = Formularz_Notatka(tytul="Moja notatka", opis="To jest treść notatki.")
        assert form.validate() is True

    def test_notatka_brak_tytulu(self):
        form = Formularz_Notatka(tytul="", opis="Treść jest.")
        assert form.validate() is False

        assert "Tytuł notatki jest wymagany." in form.tytul.errors

    def test_zdjecie_poprawne_dane(self):
        file_data = FileStorage(
            stream=BytesIO(b"test_image_content"),
            filename="test.jpg",
            content_type="image/jpeg",
        )
        form = Formularz_Zdjecie(
            tytul="Testowe zdjęcie", opis="opis", zdjecie_plik=file_data
        )
        assert form.validate() is True

    def test_zdjecie_zly_format_pliku(self):
        file_data = FileStorage(
            stream=BytesIO(b"to jest plik tekstowy"),
            filename="test.txt",
            content_type="text/plain",
        )
        form = Formularz_Zdjecie(tytul="Zły plik", opis="opis", zdjecie_plik=file_data)
        assert form.validate() is False
        assert (
            "Dozwolone są tylko pliki graficzne (jpg, png, jpeg)!"
            in form.zdjecie_plik.errors
        )
