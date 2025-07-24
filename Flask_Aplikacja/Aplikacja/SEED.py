# CRUD3.py

"""
Skrypt usuwający bazę danych, tworzący nową i wypełniający ją
realistycznym zestawem danych, w tym prawdziwymi plikami zdjęć.
"""

#! Importy
import os

from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Notatki import Notatka
from Aplikacja.Modele.Kolekcja_Pola_Własne import PoleWlasne
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Kolekcja_Zdjęcia import Zdjecie
from Aplikacja.Modele.Użytkownicy import Uzytkownik
from Aplikacja.Rozszerzenia import DB


#! Usunięcie i Utworzenie Od Nowa Bazy Danych
def seed_data():
    #! Użytkownicy (4)
    # Hasło dla wszystkich to: "Hasło#123"
    uzytkownik_1 = Uzytkownik(
        id=1,
        login="Numizmatyk",
        haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
        email="numizmatyk@example.com",
        opis="Kolekcjoner monet i militariów z okresu II RP.",
    )
    uzytkownik_2 = Uzytkownik(
        id=2,
        login="Bibliofil",
        haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
        email="bibliofil@example.com",
        opis="Miłośnik literatury fantasy i klasycznego rocka na winylu.",
    )
    uzytkownik_3 = Uzytkownik(
        id=3,
        login="Gracz",
        haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
        email="gracz@example.com",
        opis="Kolekcjoner gier retro i komiksów z lat 90.",
    )
    uzytkownik_4 = Uzytkownik(
        id=4,
        login="Historyk",
        haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
        email="historyk@example.com",
        opis="Zbieram autografy i stare fotografie Warszawy.",
    )

    DB.session.add_all([uzytkownik_1, uzytkownik_2, uzytkownik_3, uzytkownik_4])
    DB.session.commit()

    #! Kolekcja - Kategorie
    kategorie = [
        Kategoria(nazwa="Monety"),
        Kategoria(nazwa="Banknoty"),
        Kategoria(nazwa="Militaria"),
        Kategoria(nazwa="Książki"),
        Kategoria(nazwa="Płyty Winylowe"),
        Kategoria(nazwa="Gry Komputerowe"),
        Kategoria(nazwa="Komiksy"),
        Kategoria(nazwa="Autografy"),
        Kategoria(nazwa="Fotografie Historyczne"),
    ]
    DB.session.add_all(kategorie)
    DB.session.commit()

    #! Kolekcja - Waluty
    waluty = [
        Waluta(skrot="PLN", nazwa="Polski Złoty"),
        Waluta(skrot="USD", nazwa="Dolar Amerykański"),
        Waluta(skrot="EUR", nazwa="Euro"),
    ]
    DB.session.add_all(waluty)
    DB.session.commit()

    #! Kolekcja - Pola Własne Rodzaje
    pola_wlasne_rodzaje = [
        PoleWlasneRodzaj(
            nazwa="Stan Menniczy",
            typ_danych="Tekst",
            opis="Stan zachowania monety/banknotu (I-VII).",
        ),
        PoleWlasneRodzaj(
            nazwa="Rok Emisji",
            typ_danych="Liczba Całkowita",
            opis="Rok wybicia monety lub wydania banknotu.",
        ),
        PoleWlasneRodzaj(
            nazwa="Metal",
            typ_danych="Tekst",
            opis="Stop metalu, z którego wykonano monetę.",
        ),
        PoleWlasneRodzaj(
            nazwa="Autor",
            typ_danych="Tekst",
            opis="Twórca dzieła (np. pisarz, artysta).",
        ),
        PoleWlasneRodzaj(
            nazwa="Wydawnictwo", typ_danych="Tekst", opis="Wydawca książki lub komiksu."
        ),
        PoleWlasneRodzaj(
            nazwa="Platforma",
            typ_danych="Tekst",
            opis="Konsola lub system, na który wydano grę.",
        ),
    ]
    DB.session.add_all(pola_wlasne_rodzaje)
    DB.session.commit()

    #! Kolekcja - Przedmioty
    przedmioty = [
        # --- KOLEKCJA UŻYTKOWNIKA 1 (Numizmatyk) ---
        Przedmiot(
            id=1,
            nazwa="5 groszy 1934",
            opis="Moneta próbna z brązu z okresu II RP.",
            id_wlasciciel=1,
            cena_zakupu=800.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=1200.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=1,
            czy_prywatne=False,
        ),
        Przedmiot(
            id=2,
            nazwa="100 marek polskich 1919",
            opis="Banknot z początku istnienia II RP.",
            id_wlasciciel=1,
            cena_zakupu=30.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=120.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=2,
            czy_prywatne=False,
        ),
        Przedmiot(
            id=3,
            nazwa="Hełm wz. 31 'Salamandra'",
            opis="Polski hełm wojskowy, stan dobry.",
            id_wlasciciel=1,
            cena_zakupu=1500.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=2200.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=3,
            czy_prywatne=True,
        ),
        # --- KOLEKCJA UŻYTKOWNIKA 2 (Bibliofil) ---
        Przedmiot(
            id=4,
            nazwa="Wiedźmin: Ostatnie życzenie",
            opis="Pierwsze wydanie SuperNowa z 1993 roku.",
            id_wlasciciel=2,
            cena_zakupu=50.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=800.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=4,
            czy_prywatne=False,
        ),
        Przedmiot(
            id=5,
            nazwa="Led Zeppelin IV",
            opis="Wydanie winylowe z 1971 roku.",
            id_wlasciciel=2,
            cena_zakupu=100.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=350.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=5,
            czy_prywatne=False,
        ),
        # --- KOLEKCJA UŻYTKOWNIKA 3 (Gracz) ---
        Przedmiot(
            id=6,
            nazwa="The Legend of Zelda: A Link to the Past",
            opis="Edycja pudełkowa na Super Nintendo.",
            id_wlasciciel=3,
            cena_zakupu=250.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=600.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=6,
            czy_prywatne=False,
        ),
        Przedmiot(
            id=7,
            nazwa="Komiks 'Thorgal - Zdradzona czarodziejka'",
            opis="Oryginalne wydanie KAW z 1988 roku.",
            id_wlasciciel=3,
            cena_zakupu=15.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=150.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=7,
            czy_prywatne=False,
        ),
        # --- KOLEKCJA UŻYTKOWNIKA 4 (Historyk) ---
        Przedmiot(
            id=8,
            nazwa="Autograf Marii Skłodowskiej-Curie",
            opis="Podpis na liście z 1925 roku.",
            id_wlasciciel=4,
            cena_zakupu=5000.00,
            id_cena_zakupu_waluta=3,
            wartosc_rynkowa=8000.00,
            id_wartosc_rynkowa_waluta=3,
            id_kategoria=8,
            czy_prywatne=True,
        ),
        Przedmiot(
            id=9,
            nazwa="Fotografia z Powstania Warszawskiego",
            opis="Odbitka z barykady na ul. Złotej.",
            id_wlasciciel=4,
            cena_zakupu=200.00,
            id_cena_zakupu_waluta=1,
            wartosc_rynkowa=450.00,
            id_wartosc_rynkowa_waluta=1,
            id_kategoria=9,
            czy_prywatne=False,
        ),
    ]
    DB.session.add_all(przedmioty)
    DB.session.commit()

    #! Kolekcja - Notatki
    notatki = [
        Notatka(
            id_przedmiot=1,
            tytul="Pochodzenie",
            opis="Moneta zakupiona na aukcji numizmatycznej w Warszawie.",
            czy_prywatne=False,
        ),
        Notatka(
            id_przedmiot=4,
            tytul="Stan zachowania",
            opis="Grzbiet książki lekko przetarty, blok zwarty. Ogólnie stan dobry.",
            czy_prywatne=True,
        ),
        Notatka(
            id_przedmiot=6,
            tytul="Kompletność",
            opis="Gra kompletna: pudełko, instrukcja i kartridż w bardzo dobrym stanie.",
            czy_prywatne=False,
        ),
    ]
    DB.session.add_all(notatki)
    DB.session.commit()

    #! Kolekcja - Pola Własne
    pola_wlasne = [
        PoleWlasne(id_rodzaj=1, id_przedmiot=1, wartosc="Stan I (menniczy)"),
        PoleWlasne(id_rodzaj=2, id_przedmiot=1, wartosc="1934"),
        PoleWlasne(id_rodzaj=3, id_przedmiot=1, wartosc="Brąz"),
        PoleWlasne(id_rodzaj=4, id_przedmiot=4, wartosc="Andrzej Sapkowski"),
        PoleWlasne(id_rodzaj=5, id_przedmiot=4, wartosc="SuperNowa"),
        PoleWlasne(id_rodzaj=6, id_przedmiot=6, wartosc="SNES"),
    ]
    DB.session.add_all(pola_wlasne)
    DB.session.commit()

    #! Kolekcja - Zdjęcia
    def wczytaj_zdjecie(sciezka, nazwa_pliku):
        """Funkcja pomocnicza, która teraz przyjmuje ścieżkę jako argument."""
        try:
            with open(os.path.join(sciezka, nazwa_pliku), "rb") as plik:
                return plik.read()
        except FileNotFoundError:
            print(
                f"BŁĄD: Plik '{nazwa_pliku}' nie został znaleziony w folderze '{sciezka}'"
            )
            return None

    sciezka_do_zdjec = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "../..",
        "Dane_Poczatkowe",
        "Zdjecia",
    )

    zdjecia_info = [
        {
            "id_przedmiotu": 1,
            "plik": "moneta_5gr_awers.jpg",
            "tytul": "Awers",
            "opis": "Awers monety 5 gr z 1934.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 1,
            "plik": "moneta_5gr_rewers.jpg",
            "tytul": "Rewers",
            "opis": "Rewers monety 5 gr z 1934.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 2,
            "plik": "banknot_100m.jpg",
            "tytul": "Awers banknotu",
            "opis": "100 marek polskich z 1919 roku.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 3,
            "plik": "helm_wz31.jpg",
            "tytul": "Hełm wz. 31",
            "opis": "Widok z przodu.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 4,
            "plik": "wiedzmin_ksiazka.jpg",
            "tytul": "Okładka",
            "opis": 'Pierwsze wydanie "Ostatniego życzenia".',
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 5,
            "plik": "led_zeppelin_iv.jpg",
            "tytul": "Okładka płyty",
            "opis": "Album Led Zeppelin IV.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 6,
            "plik": "zelda_snes.jpg",
            "tytul": "Pudełko z grą",
            "opis": "The Legend of Zelda na SNES.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 7,
            "plik": "thorgal_komiks.jpg",
            "tytul": "Okładka komiksu",
            "opis": "Komiks Thorgal - Zdradzona czarodziejka.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 8,
            "plik": "autograf_curie.jpg",
            "tytul": "Autograf na liście",
            "opis": "Podpis Marii Skłodowskiej-Curie.",
            "mime": "image/jpeg",
        },
        {
            "id_przedmiotu": 9,
            "plik": "powstanie_foto.jpg",
            "tytul": "Barykada na ul. Złotej",
            "opis": "Oryginalna odbitka z 1944 roku.",
            "mime": "image/jpeg",
        },
    ]

    zdjecia_do_dodania = []
    for info in zdjecia_info:
        dane_pliku = wczytaj_zdjecie(sciezka_do_zdjec, info["plik"])
        if dane_pliku:
            zdjecia_do_dodania.append(
                Zdjecie(
                    id_przedmiot=info["id_przedmiotu"],
                    zdjecie_dane=dane_pliku,
                    tytul=info["tytul"],
                    opis=info["opis"],
                    mimetype=info["mime"],
                )
            )

    if zdjecia_do_dodania:
        DB.session.add_all(zdjecia_do_dodania)
        DB.session.commit()

    #! Koniec
    print("Baza danych została pomyślnie utworzona i wypełniona danymi.")
