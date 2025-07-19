"""Skrypt usuwający bazę danych, tworzący nową i wypełniający ją danymi."""

#! Importy
from Aplikacja.Rozszerzenia import DB

from Aplikacja.Modele.Użytkownicy import Uzytkownik
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Pola_Własne import PoleWlasne
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Notatki import Notatka
from Aplikacja.Modele.Kolekcja_Zdjęcia import Zdjecie

#! Usunięcie i Utworzenie Od Nowa Bazy Danych
DB.drop_all()
DB.create_all()

#! Użytkownicy
uzytkownik_1 = Uzytkownik(id=1, login="Login_1", haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", email="wip_1@wip.wip") # Hasło: "Hasło#123"
uzytkownik_2 = Uzytkownik(id=2, login="Login_2", haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", email="wip_2@wip.wip") # Hasło: "Hasło#123"
uzytkownik_3 = Uzytkownik(id=3, login="Login_3", haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", email="wip_3@wip.wip") # Hasło: "Hasło#123"

DB.session.add_all([uzytkownik_1, uzytkownik_2, uzytkownik_3])
DB.session.commit()

#! Kolekcja - Kategorie
kategoria_1 = Kategoria(id=1, nazwa="Książki", opis="Kategoria dla książek.")
kategoria_2 = Kategoria(id=2, nazwa="Pocztówki", opis="Kategoria dla pocztówek.")
kategoria_3 = Kategoria(id=3, nazwa="Znaczki Pocztowe", opis="Kategoria dla znaczków pocztowych.")
kategoria_4 = Kategoria(id=4, nazwa="Fotografie", opis="Kategoria dla fotografii.")
kategoria_5 = Kategoria(id=5, nazwa="Gry Komputerowe", opis="Kategoria dla gier komputerowych.")
kategoria_6 = Kategoria(id=6, nazwa="Elektronika", opis="Kategoria dla elektroniki.")
kategoria_7 = Kategoria(id=7, nazwa="Narzędzia", opis="Kategoria dla narzędzi.")

DB.session.add_all([
    kategoria_1, kategoria_2, kategoria_3, kategoria_4,
    kategoria_5, kategoria_6, kategoria_7
])
DB.session.commit()

#! Kolekcja - Waluty
waluta_1 = Waluta(id=1, skrot="PLN", nazwa="Polski Złoty")
waluta_2 = Waluta(id=2, skrot="USD", nazwa="Dolar Amerykański")
waluta_3 = Waluta(id=3, skrot="EUR", nazwa="Euro")

DB.session.add_all([waluta_1, waluta_2, waluta_3])
DB.session.commit()

#! Kolekcja - Pola Własne Rodzaje
pole_wlasne_rodzaj_1 = PoleWlasneRodzaj(id=1, nazwa="Stan", typ_danych="Tekst", opis="Stan przedmiotu (np. nowy, używany, zniszczony).")
pole_wlasne_rodzaj_2 = PoleWlasneRodzaj(id=2, nazwa="Data Nabycia", typ_danych="Data", opis="Data nabycia przedmiotu.")
pole_wlasne_rodzaj_3 = PoleWlasneRodzaj(id=3, nazwa="Liczba Stron", typ_danych="Liczba Całkowita", opis="Liczba stron w książce.")
pole_wlasne_rodzaj_4 = PoleWlasneRodzaj(id=4, nazwa="Wersja Oprogramowania", typ_danych="Tekst", opis="Wersja oprogramowania (dla gier/elektroniki).")

DB.session.add_all([pole_wlasne_rodzaj_1, pole_wlasne_rodzaj_2, pole_wlasne_rodzaj_3, pole_wlasne_rodzaj_4])
DB.session.commit()

#! Kolekcja - Przedmioty
przedmiot_1 = Przedmiot(
    id=1,
    nazwa="Harry Potter i Kamień Filozoficzny",
    opis="Pierwsza część serii książek o Harrym Potterze.",
    # data_dodania jest ustawiana domyślnie
    id_wlasciciel=uzytkownik_1.id, # Odwołanie do id istniejącego użytkownika
    cena_zakupu=25.50,
    id_cena_zakupu_waluta=waluta_1.id, # Odwołanie do id istniejącej waluty
    wartosc_rynkowa=35.00,
    id_wartosc_rynkowa_waluta=waluta_1.id, # Odwołanie do id istniejącej waluty
    id_kategoria=kategoria_1.id, # Odwołanie do id istniejącej kategorii
    czy_prywatne=False
)

przedmiot_2 = Przedmiot(
    id=2,
    nazwa="Stara pocztówka z Krakowa",
    opis="Pocztówka z lat 70. przedstawiająca Rynek Główny.",
    id_wlasciciel=uzytkownik_1.id,
    cena_zakupu=5.00,
    id_cena_zakupu_waluta=waluta_1.id,
    wartosc_rynkowa=15.00,
    id_wartosc_rynkowa_waluta=waluta_1.id,
    id_kategoria=kategoria_2.id,
    czy_prywatne=False
)

przedmiot_3 = Przedmiot(
    id=3,
    nazwa="Fallout: New Vegas",
    opis="Postapokaliptyczna gra RPG z 2010 roku.",
    id_wlasciciel=uzytkownik_2.id,
    cena_zakupu=12.99,
    id_cena_zakupu_waluta=waluta_2.id, # USD
    wartosc_rynkowa=20.00,
    id_wartosc_rynkowa_waluta=waluta_2.id, # USD
    id_kategoria=kategoria_5.id,
    czy_prywatne=False
)

DB.session.add_all([przedmiot_1, przedmiot_2, przedmiot_3])
DB.session.commit()

#! Kolekcja - Notatki
notatka_1 = Notatka(
    id=1,
    id_przedmiot=przedmiot_1.id,
    tytul="Wydanie pierwsze",
    opis="Książka jest pierwszym wydaniem z 1997 roku.",
    czy_prywatne=False
)
notatka_2 = Notatka(
    id=2,
    id_przedmiot=przedmiot_3.id,
    tytul="Błędy w grze",
    opis="Gra wymaga patcha fanowskiego dla stabilności.",
    czy_prywatne=True # Prywatna notatka
)

DB.session.add_all([notatka_1, notatka_2])
DB.session.commit()

#! Kolekcja - Pola Własne
pole_wlasne_1 = PoleWlasne(
    id=1,
    id_rodzaj=pole_wlasne_rodzaj_1.id, # Stan
    id_przedmiot=przedmiot_1.id,
    wartosc="Bardzo dobry"
)
pole_wlasne_2 = PoleWlasne(
    id=2,
    id_rodzaj=pole_wlasne_rodzaj_2.id, # Data Nabycia
    id_przedmiot=przedmiot_1.id,
    wartosc="2022-03-15"
)
pole_wlasne_3 = PoleWlasne(
    id=3,
    id_rodzaj=pole_wlasne_rodzaj_1.id, # Stan
    id_przedmiot=przedmiot_3.id,
    wartosc="Używany"
)

DB.session.add_all([pole_wlasne_1, pole_wlasne_2, pole_wlasne_3])
DB.session.commit()

#! Kolekcja - Zdjęcia
zdjecie_1 = Zdjecie(
    id=1,
    id_przedmiot=przedmiot_1.id,
    zdjecie_dane=b"zdjecie_ksiazki_harry_potter", # Przykładowe dane binarne
    tytul="Okładka przód",
    opis="Zdjęcie okładki książki Harry Potter."
)
zdjecie_2 = Zdjecie(
    id=2,
    id_przedmiot=przedmiot_2.id,
    zdjecie_dane=b"zdjecie_pocztowki_krakow",
    tytul="Widok na Rynek",
    opis="Zdjęcie frontu pocztówki z widokiem na Rynek Główny."
)

DB.session.add_all([zdjecie_1, zdjecie_2])
DB.session.commit()

#! Koniec