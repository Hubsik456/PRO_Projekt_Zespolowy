"""
Skrypt usuwający bazę danych, tworzący nową i wypełniający ją
rozszerzonym zestawem danych.
"""

#! Importy
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
DB.drop_all()
DB.create_all()

#! Użytkownicy
# Hasło dla wszystkich to: "Hasło#123"
uzytkownik_1 = Uzytkownik(
    id=1,
    login="Login_1",
    haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
    email="login_1@example.com",
)
uzytkownik_2 = Uzytkownik(
    id=2,
    login="Login_2",
    haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
    email="login_2@example.com",
)
uzytkownik_3 = Uzytkownik(
    id=3,
    login="Login_3",
    haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
    email="login_3@example.com",
)
uzytkownik_4 = Uzytkownik(
    id=4,
    login="Login_4",
    haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
    email="login_4@example.com",
)
uzytkownik_5 = Uzytkownik(
    id=5,
    login="Login_5",
    haslo="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771",
    email="login_5@example.com",
)

DB.session.add_all(
    [uzytkownik_1, uzytkownik_2, uzytkownik_3, uzytkownik_4, uzytkownik_5]
)
DB.session.commit()

#! Kolekcja - Kategorie
kategoria_1 = Kategoria(id=1, nazwa="Książki", opis="Książki, starodruki, manuskrypty.")
kategoria_2 = Kategoria(
    id=2, nazwa="Pocztówki", opis="Kolekcje pocztówek z różnych okresów i miejsc."
)
kategoria_3 = Kategoria(
    id=3, nazwa="Znaczki Pocztowe", opis="Filatelistyka, znaczki polskie i zagraniczne."
)
kategoria_4 = Kategoria(
    id=4, nazwa="Fotografie", opis="Stare fotografie, dagerotypy, zdjęcia artystyczne."
)
kategoria_5 = Kategoria(
    id=5, nazwa="Gry Komputerowe", opis="Gry na PC i konsole, edycje kolekcjonerskie."
)
kategoria_6 = Kategoria(
    id=6, nazwa="Elektronika", opis="Retro komputery, konsole, sprzęt audio."
)
kategoria_7 = Kategoria(
    id=7, nazwa="Narzędzia", opis="Zabytkowe narzędzia rzemieślnicze."
)
kategoria_8 = Kategoria(
    id=8, nazwa="Monety", opis="Numizmatyka, monety obiegowe i kolekcjonerskie."
)
kategoria_9 = Kategoria(id=9, nazwa="Banknoty", opis="Banknoty polskie i zagraniczne.")
kategoria_10 = Kategoria(id=10, nazwa="Sztuka", opis="Obrazy, grafiki, rzeźby.")
kategoria_11 = Kategoria(id=11, nazwa="Komiksy", opis="Zeszyty i albumy komiksowe.")
kategoria_12 = Kategoria(
    id=12, nazwa="Płyty Winylowe", opis="Albumy muzyczne na płytach winylowych."
)
kategoria_13 = Kategoria(
    id=13, nazwa="Figurki", opis="Figurki kolekcjonerskie, modele."
)
kategoria_14 = Kategoria(
    id=14, nazwa="Militaria", opis="Odznaczenia, hełmy, elementy umundurowania."
)
kategoria_15 = Kategoria(id=15, nazwa="Autografy", opis="Podpisy znanych osób.")

DB.session.add_all(
    [
        kategoria_1,
        kategoria_2,
        kategoria_3,
        kategoria_4,
        kategoria_5,
        kategoria_6,
        kategoria_7,
        kategoria_8,
        kategoria_9,
        kategoria_10,
        kategoria_11,
        kategoria_12,
        kategoria_13,
        kategoria_14,
        kategoria_15,
    ]
)
DB.session.commit()

#! Kolekcja - Waluty
waluta_1 = Waluta(id=1, skrot="PLN", nazwa="Polski Złoty")
waluta_2 = Waluta(id=2, skrot="USD", nazwa="Dolar Amerykański")
waluta_3 = Waluta(id=3, skrot="EUR", nazwa="Euro")
waluta_4 = Waluta(id=4, skrot="GBP", nazwa="Funt Brytyjski")
waluta_5 = Waluta(id=5, skrot="CHF", nazwa="Frank Szwajcarski")

DB.session.add_all([waluta_1, waluta_2, waluta_3, waluta_4, waluta_5])
DB.session.commit()

#! Kolekcja - Pola Własne Rodzaje
pwr_1 = PoleWlasneRodzaj(
    id=1,
    nazwa="Stan",
    typ_danych="Tekst",
    opis="Stan przedmiotu (np. nowy, używany, menniczy).",
)
pwr_2 = PoleWlasneRodzaj(
    id=2, nazwa="Data Nabycia", typ_danych="Data", opis="Data nabycia przedmiotu."
)
pwr_3 = PoleWlasneRodzaj(
    id=3,
    nazwa="Liczba Stron",
    typ_danych="Liczba Całkowita",
    opis="Liczba stron w książce/komiksie.",
)
pwr_4 = PoleWlasneRodzaj(
    id=4,
    nazwa="Wersja Oprogramowania",
    typ_danych="Tekst",
    opis="Wersja oprogramowania (dla gier/elektroniki).",
)
pwr_5 = PoleWlasneRodzaj(
    id=5, nazwa="Autor", typ_danych="Tekst", opis="Twórca dzieła (np. pisarz, artysta)."
)
pwr_6 = PoleWlasneRodzaj(
    id=6,
    nazwa="Rok Produkcji",
    typ_danych="Liczba Całkowita",
    opis="Rok powstania/produkcji przedmiotu.",
)
pwr_7 = PoleWlasneRodzaj(
    id=7,
    nazwa="Materiał",
    typ_danych="Tekst",
    opis="Materiał, z którego wykonano przedmiot (np. srebro, miedź).",
)
pwr_8 = PoleWlasneRodzaj(
    id=8,
    nazwa="Kraj Pochodzenia",
    typ_danych="Tekst",
    opis="Kraj, z którego pochodzi przedmiot.",
)
pwr_9 = PoleWlasneRodzaj(
    id=9, nazwa="Wydawnictwo", typ_danych="Tekst", opis="Wydawca książki lub komiksu."
)

DB.session.add_all([pwr_1, pwr_2, pwr_3, pwr_4, pwr_5, pwr_6, pwr_7, pwr_8, pwr_9])
DB.session.commit()

#! Kolekcja - Przedmioty
# Dodawanie przedmiotów, po kilka na raz i commit
przedmioty_batch_1 = [
    Przedmiot(
        id=1,
        nazwa="Harry Potter i Kamień Filozoficzny",
        opis="Pierwsza część serii książek o Harrym Potterze.",
        id_wlasciciel=uzytkownik_1.id,
        cena_zakupu=25.50,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=40.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_1.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=2,
        nazwa="Stara pocztówka z Krakowa",
        opis="Pocztówka z lat 70. przedstawiająca Rynek Główny.",
        id_wlasciciel=uzytkownik_1.id,
        cena_zakupu=5.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=15.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_2.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=3,
        nazwa="Fallout: New Vegas",
        opis="Postapokaliptyczna gra RPG z 2010 roku.",
        id_wlasciciel=uzytkownik_4.id,
        cena_zakupu=12.99,
        id_cena_zakupu_waluta=waluta_2.id,
        wartosc_rynkowa=20.00,
        id_wartosc_rynkowa_waluta=waluta_2.id,
        id_kategoria=kategoria_5.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=4,
        nazwa="2 złote, 1934, Józef Piłsudski",
        opis="Srebrna moneta próbna z okresu II RP.",
        id_wlasciciel=uzytkownik_5.id,
        cena_zakupu=200.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=350.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_8.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=5,
        nazwa="Dark Side of the Moon - Pink Floyd",
        opis="Oryginalne wydanie z 1973 roku.",
        id_wlasciciel=uzytkownik_2.id,
        cena_zakupu=150.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=400.00,
        id_wartosc_rynkowa_waluta=waluta_3.id,
        id_kategoria=kategoria_12.id,
        czy_prywatne=False,
    ),
]
DB.session.add_all(przedmioty_batch_1)
DB.session.commit()

przedmioty_batch_2 = [
    Przedmiot(
        id=6,
        nazwa="Kajko i Kokosz: Szkoła Latania",
        opis="Pierwsze wydanie komiksu Janusza Christy.",
        id_wlasciciel=uzytkownik_3.id,
        cena_zakupu=10.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=250.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_11.id,
        czy_prywatne=True,
    ),
    Przedmiot(
        id=7,
        nazwa="Atari 2600",
        opis="Konsola do gier z 1977 roku, w pełni sprawna.",
        id_wlasciciel=uzytkownik_4.id,
        cena_zakupu=300.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=150.00,
        id_wartosc_rynkowa_waluta=waluta_2.id,
        id_kategoria=kategoria_6.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=8,
        nazwa="Hełm wz. 67",
        opis="Polski hełm wojskowy, stan magazynowy.",
        id_wlasciciel=uzytkownik_1.id,
        cena_zakupu=50.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=80.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_14.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=9,
        nazwa="100 marek polskich, 1919",
        opis="Banknot z początku istnienia II RP.",
        id_wlasciciel=uzytkownik_5.id,
        cena_zakupu=30.00,
        id_cena_zakupu_waluta=waluta_1.id,
        wartosc_rynkowa=120.00,
        id_wartosc_rynkowa_waluta=waluta_1.id,
        id_kategoria=kategoria_9.id,
        czy_prywatne=False,
    ),
    Przedmiot(
        id=10,
        nazwa="Autograf Lecha Wałęsy",
        opis="Podpis na fotografii z 1990 roku.",
        id_wlasciciel=uzytkownik_3.id,
        cena_zakupu=100.00,
        id_cena_zakupu_waluta=waluta_3.id,
        wartosc_rynkowa=500.00,
        id_wartosc_rynkowa_waluta=waluta_3.id,
        id_kategoria=kategoria_15.id,
        czy_prywatne=True,
    ),
]
DB.session.add_all(przedmioty_batch_2)
DB.session.commit()

#! Kolekcja - Notatki
notatki = [
    Notatka(
        id=1,
        id_przedmiot=1,
        tytul="Wydanie pierwsze",
        opis="Książka jest pierwszym polskim wydaniem z 1999 roku.",
        czy_prywatne=False,
    ),
    Notatka(
        id=2,
        id_przedmiot=3,
        tytul="Błędy w grze",
        opis="Gra wymaga patcha fanowskiego dla stabilności.",
        czy_prywatne=True,
    ),
    Notatka(
        id=3,
        id_przedmiot=4,
        tytul="Pochodzenie",
        opis="Moneta zakupiona na aukcji numizmatycznej w Warszawie.",
        czy_prywatne=False,
    ),
    Notatka(
        id=4,
        id_przedmiot=5,
        tytul="Jakość dźwięku",
        opis="Brak trzasków, stan płyty VG+.",
        czy_prywatne=False,
    ),
    Notatka(
        id=5,
        id_przedmiot=7,
        tytul="Modyfikacje",
        opis="Konsola posiada mod AV.",
        czy_prywatne=True,
    ),
]
DB.session.add_all(notatki)
DB.session.commit()

#! Kolekcja - Pola Własne
pola_wlasne = [
    PoleWlasne(id=1, id_rodzaj=pwr_1.id, id_przedmiot=1, wartosc="Bardzo dobry"),
    PoleWlasne(id=2, id_rodzaj=pwr_2.id, id_przedmiot=1, wartosc="2022-03-15"),
    PoleWlasne(id=3, id_rodzaj=pwr_1.id, id_przedmiot=3, wartosc="Używany"),
    PoleWlasne(id=4, id_rodzaj=pwr_5.id, id_przedmiot=1, wartosc="J.K. Rowling"),
    PoleWlasne(id=5, id_rodzaj=pwr_9.id, id_przedmiot=1, wartosc="Media Rodzina"),
    PoleWlasne(id=6, id_rodzaj=pwr_7.id, id_przedmiot=4, wartosc="Srebro (Ag 750)"),
    PoleWlasne(id=7, id_rodzaj=pwr_6.id, id_przedmiot=4, wartosc="1934"),
    PoleWlasne(id=8, id_rodzaj=pwr_1.id, id_przedmiot=5, wartosc="Używany, VG+"),
    PoleWlasne(id=9, id_rodzaj=pwr_5.id, id_przedmiot=5, wartosc="Pink Floyd"),
    PoleWlasne(id=10, id_rodzaj=pwr_6.id, id_przedmiot=6, wartosc="1987"),
    PoleWlasne(id=11, id_rodzaj=pwr_5.id, id_przedmiot=6, wartosc="Janusz Christa"),
    PoleWlasne(id=12, id_rodzaj=pwr_1.id, id_przedmiot=9, wartosc="Obiegowy, stan III"),
    PoleWlasne(id=13, id_rodzaj=pwr_8.id, id_przedmiot=9, wartosc="Polska"),
]
DB.session.add_all(pola_wlasne)
DB.session.commit()

#! Kolekcja - Zdjęcia
zdjecia = [
    Zdjecie(
        id=1,
        id_przedmiot=1,
        zdjecie_dane=b"zdjecie_ksiazki_harry_potter",
        tytul="Okładka przód",
        opis="Zdjęcie okładki książki Harry Potter.",
    ),
    Zdjecie(
        id=2,
        id_przedmiot=2,
        zdjecie_dane=b"zdjecie_pocztowki_krakow",
        tytul="Widok na Rynek",
        opis="Zdjęcie frontu pocztówki z widokiem na Rynek Główny.",
    ),
    Zdjecie(
        id=3,
        id_przedmiot=4,
        zdjecie_dane=b"zdjecie_monety_2zl_1934_awers",
        tytul="Awers",
        opis="Awers monety 2 zł z 1934.",
    ),
    Zdjecie(
        id=4,
        id_przedmiot=4,
        zdjecie_dane=b"zdjecie_monety_2zl_1934_rewers",
        tytul="Rewers",
        opis="Rewers monety 2 zł z 1934.",
    ),
    Zdjecie(
        id=5,
        id_przedmiot=7,
        zdjecie_dane=b"zdjecie_konsoli_atari_2600",
        tytul="Konsola z joystickiem",
        opis="Zdjęcie konsoli Atari 2600.",
    ),
    Zdjecie(
        id=6,
        id_przedmiot=5,
        zdjecie_dane=b"zdjecie_plyty_dsotm",
        tytul="Okładka płyty",
        opis="Okładka albumu Dark Side of the Moon.",
    ),
]
DB.session.add_all(zdjecia)
DB.session.commit()

#! Koniec
print("Baza danych została pomyślnie usunięta, stworzona i wypełniona nowymi danymi.")
exit()
