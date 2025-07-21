"""WIP

Widoki (routes) dla Blueprintu #3 - Kolekcja.

Ten moduł zawiera logikę i definicje URL dla wszystkich stron
związanych z zarządzaniem kolekcjami użytkowników.
"""

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, request as REQUEST, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, abort as ABORT
from flask_login import login_required as LOGIN_REQUIRED, current_user as CURRENT_USER
from sqlalchemy.sql import func as FUNC
from flask_wtf.file import FileRequired
import base64 as BASE64

#! Lokalne importy
from Aplikacja.Rozszerzenia import DB
from Aplikacja.Kolekcja import Blueprint_3

from Aplikacja.Kolekcja.Formularze.Dodanie_Przedmiotu import Formularz_Dodanie_Przedmiotu
from Aplikacja.Kolekcja.Formularze.Pole_Własne import Formularz_Pole_Własne
from Aplikacja.Kolekcja.Formularze.Notatka import Formularz_Notatka
from Aplikacja.Kolekcja.Formularze.Zdjęcie import Formularz_Zdjecie

from Aplikacja.Modele.Użytkownicy import Uzytkownik
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Pola_Własne import PoleWlasne
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Notatki import Notatka
from Aplikacja.Modele.Kolekcja_Zdjęcia import Zdjecie

#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """Renderuje stronę główną z kolekcjami użytkownika.

    :return: Wyrenderowany szablon HTML strony głównej kolekcji.
    :rtype: str
    """
    return RENDER_TEMPLATE("Kolekcja/index.html")

@Blueprint_3.route("/podsumowanie/")
def Widok_Kolekcja_Podsumowanie():
    return RENDER_TEMPLATE("Kolekcja/Podsumowanie.html")

@Blueprint_3.route("/<int:ID>/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Kolekcja(ID):
    return RENDER_TEMPLATE("Kolekcja/Kolekcja.html", ID=ID)

@Blueprint_3.route("/moja-kolekcja/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Moja_Kolekcja():
    Kolekcja = CURRENT_USER.przedmioty_uzytkownika

    return RENDER_TEMPLATE("Kolekcja/Moja_Kolekcja.html", Kolekcja=Kolekcja)

@Blueprint_3.route("/moja-kolekcja/dodaj/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Dodaj():
    Formularz = Formularz_Dodanie_Przedmiotu()

    #? Dodanie opcji do `<select>`
    Select_Waluty = DB.session.execute(DB.select(Waluta)).scalars().all()
    Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
    Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]

    Select_Kategorie = DB.session.execute(DB.select(Kategoria)).scalars().all()
    Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

    #Select_Pola_Wlasne_Rodzaje = DB.session.execute(DB.select(PoleWlasneRodzaj)).scalars().all()
    #Select_Pola_Wlasne_Rodzaje_Pozycje = [(str(x.id), x.nazwa) for x in Select_Pola_Wlasne_Rodzaje]

    #? Jeśli formularz został przesłany
    if REQUEST.method == "POST":
        Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

        if Formularz.validate_on_submit():
            Nowy_Przedmiot = Przedmiot(
                nazwa=Formularz.nazwa.data,
                opis=Formularz.opis.data,
                id_wlasciciel=CURRENT_USER.id,
                cena_zakupu=Formularz.cena_zakupu.data,
                id_cena_zakupu_waluta=Formularz.id_cena_zakupu_waluta.data,
                wartosc_rynkowa=Formularz.wartosc_rynkowa.data,
                id_wartosc_rynkowa_waluta=Formularz.id_wartosc_rynkowa_waluta.data,
                id_kategoria=Formularz.id_kategoria.data,
                czy_prywatne=Formularz.czy_prywatne.data
            )

            DB.session.add(Nowy_Przedmiot)
            #DB.session.flush()
            DB.session.commit()

            FLASH(f"Dodano nowy przedmiot do Twojej kolekcji.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

        FLASH("Podano niepoprawne dane.", "danger")

    #return RENDER_TEMPLATE("Kolekcja/Dodaj.html", Formularz=Formularz, Select_Pola_Wlasne_Rodzaje_Pozycje=Select_Pola_Wlasne_Rodzaje_Pozycje)
    return RENDER_TEMPLATE("Kolekcja/Dodaj.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/szczegoly/<int:ID>/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Szczegóły(ID):
    #? Pobranie przedmiotów
    _Przedmiot = DB.session.execute(DB.select(Przedmiot).filter_by(id=ID)).scalar_one_or_none()

    #? Sprawdzenie czy przedmiot istnieje
    if _Przedmiot is None:
        ABORT(404)

    #? Sprawdzenie czy obecny użytkownik to właściciel przedmiotu
    if _Przedmiot.id_wlasciciel != CURRENT_USER.id:
        ABORT(403)

    #? Przetworzenie zdjęć do wyświetlenia w szablonie
    zdjecia_do_szablonu = []
    for zdjecie in _Przedmiot.zdjecia:
        if zdjecie.zdjecie_dane and zdjecie.mimetype:
            encoded_image = BASE64.b64encode(zdjecie.zdjecie_dane).decode('utf-8')
            # Zbuduj pełny Data URI
            data_uri = f"data:{zdjecie.mimetype};base64,{encoded_image}"
        else:
            data_uri = None # Jeśli brakuje danych lub mimetype, nie wyświetlaj

        zdjecia_do_szablonu.append({
            'id': zdjecie.id,
            'tytul': zdjecie.tytul,
            'opis': zdjecie.opis,
            'data_uri': data_uri
        })

    return RENDER_TEMPLATE("Kolekcja/Przedmiot_Szczegóły.html", Przedmiot=_Przedmiot, Zdjęcia=zdjecia_do_szablonu)

@Blueprint_3.route("/moja-kolekcja/edytuj/<int:ID>/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Edytuj(ID):
    #? Sprawdzenie czy przedmiot istnieje
    Edytowany_Przedmiot = DB.session.execute(DB.select(Przedmiot).filter_by(id=ID, id_wlasciciel=CURRENT_USER.id)).scalar_one_or_none()

    if not Edytowany_Przedmiot:
        FLASH("Nie można odnaleźć tego przedmiotu.", "danger")
        ABORT(404)

    #? Formularz
    Formularz = Formularz_Dodanie_Przedmiotu()

    #? Dodanie opcji do `<select>`
    Select_Waluty = DB.session.execute(DB.select(Waluta)).scalars().all()
    Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
    Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]

    Select_Kategorie = DB.session.execute(DB.select(Kategoria)).scalars().all()
    Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

    #? GET
    if REQUEST.method == "GET":
        Formularz.nazwa.data = Edytowany_Przedmiot.nazwa
        Formularz.opis.data = Edytowany_Przedmiot.opis
        Formularz.cena_zakupu.data = Edytowany_Przedmiot.cena_zakupu
        Formularz.id_cena_zakupu_waluta.data = Edytowany_Przedmiot.id_cena_zakupu_waluta
        Formularz.wartosc_rynkowa.data = Edytowany_Przedmiot.wartosc_rynkowa
        Formularz.id_wartosc_rynkowa_waluta.data = Edytowany_Przedmiot.id_wartosc_rynkowa_waluta
        Formularz.id_kategoria.data = Edytowany_Przedmiot.id_kategoria
        Formularz.czy_prywatne.data = Edytowany_Przedmiot.czy_prywatne

    #? POST
    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            Edytowany_Przedmiot.nazwa = Formularz.nazwa.data
            Edytowany_Przedmiot.opis = Formularz.opis.data
            Edytowany_Przedmiot.cena_zakupu = Formularz.cena_zakupu.data
            Edytowany_Przedmiot.id_cena_zakupu_waluta = Formularz.id_cena_zakupu_waluta.data
            Edytowany_Przedmiot.wartosc_rynkowa = Formularz.wartosc_rynkowa.data
            Edytowany_Przedmiot.id_wartosc_rynkowa_waluta = Formularz.id_wartosc_rynkowa_waluta.data
            Edytowany_Przedmiot.id_kategoria = Formularz.id_kategoria.data
            Edytowany_Przedmiot.czy_prywatne = Formularz.czy_prywatne.data

            DB.session.commit()

            FLASH(f"Zaktualizowano przedmiot '{Edytowany_Przedmiot.nazwa}'.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Przedmiot_Edycja.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/usun/<int:ID>/", methods=["POST"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Usuń(ID):
    #? Sprawdzenie czy przedmiot istnieje
    Przedmiot_Do_Usuniecia = DB.session.execute(DB.select(Przedmiot).filter_by(id=ID, id_wlasciciel=CURRENT_USER.id)).scalar_one_or_none()

    if not Przedmiot_Do_Usuniecia:
        FLASH("Nie można odnaleźć przedmiotu do usunięcia lub nie masz do niego uprawnień.", "danger")
        ABORT(404)

    DB.session.delete(Przedmiot_Do_Usuniecia)
    DB.session.commit()

    FLASH(f"Przedmiot '{Przedmiot_Do_Usuniecia.nazwa}' został pomyślnie usunięty.", "success")
    return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

@Blueprint_3.route("/moja-kolekcja/<int:ID>/notatki/dodaj/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Notatka_Dodaj(ID):
    przedmiot_parent = DB.session.execute(
        DB.select(Przedmiot).filter_by(id=ID, id_wlasciciel=CURRENT_USER.id)
    ).scalar_one_or_none()

    if not przedmiot_parent:
        FLASH("Nie znaleziono przedmiotu lub nie masz uprawnień do dodawania do niego notatek.", "danger")
        ABORT(404)

    Formularz = Formularz_Notatka()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            nowa_notatka = Notatka(
                tytul=Formularz.tytul.data,
                opis=Formularz.opis.data,
                czy_prywatne=Formularz.czy_prywatne.data,
                id_przedmiot=ID
            )

            DB.session.add(nowa_notatka)
            DB.session.commit()

            FLASH(f"Notatka '{nowa_notatka.tytul}' została dodana.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Notatka_Dodanie.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/notatki/edytuj/<int:ID_Notatka>/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Notatka_Edytuj(ID_Przedmiot, ID_Notatka):
    edytowana_notatka = DB.session.execute(
        DB.select(Notatka)
        .join(Przedmiot)
        .filter(
            Notatka.id == ID_Notatka,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    if not edytowana_notatka:
        FLASH("Nie znaleziono notatki lub nie masz uprawnień do jej edycji.", "danger")
        ABORT(404)

    Formularz = Formularz_Notatka()

    if REQUEST.method == "GET":
        Formularz.tytul.data = edytowana_notatka.tytul
        Formularz.opis.data = edytowana_notatka.opis
        Formularz.czy_prywatne.data = edytowana_notatka.czy_prywatne

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            edytowana_notatka.tytul = Formularz.tytul.data
            edytowana_notatka.opis = Formularz.opis.data
            edytowana_notatka.czy_prywatne = Formularz.czy_prywatne.data

            DB.session.commit()

            FLASH(f"Notatka '{edytowana_notatka.tytul}' została zaktualizowana.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=edytowana_notatka.id_przedmiot))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Notatka_Edycja.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/notatki/usuń/<int:ID_Notatka>/", methods=["POST"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Notatka_Usuń(ID_Przedmiot, ID_Notatka):
    Notatka_Do_Usuniecia = DB.session.execute(
        DB.select(Notatka)
        .join(Przedmiot) # Dołączamy tabelę Przedmioty
        .filter(
            Notatka.id == ID_Notatka,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    print(Notatka_Do_Usuniecia)

    if not Notatka_Do_Usuniecia:
        FLASH("Nie można odnaleźć notatki do usunięcia lub nie masz do niej uprawnień.", "danger")
        ABORT(404)

    DB.session.delete(Notatka_Do_Usuniecia)
    DB.session.commit()

    FLASH(f"Notatka '{Notatka_Do_Usuniecia.tytul}' została pomyślnie usunięta.", "success")
    return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID_Przedmiot))

@Blueprint_3.route("/moja-kolekcja/<int:ID>/pola-wlasne/dodaj/", methods=["POST", "GET"])
def Widok_Kolekcja_Pole_Własne_Dodaj(ID):
    przedmiot_parent = DB.session.execute(
        DB.select(Przedmiot).filter_by(id=ID, id_wlasciciel=CURRENT_USER.id)
    ).scalar_one_or_none()

    if not przedmiot_parent:
        FLASH("Nie znaleziono przedmiotu lub nie masz uprawnień do dodawania pól własnych do niego.", "danger")
        ABORT(404)

    Formularz = Formularz_Pole_Własne()

    rodzaje_pol_wlasnych = DB.session.execute(DB.select(PoleWlasneRodzaj)).scalars().all()
    Formularz.id_rodzaj.choices = [(str(r.id), r.nazwa) for r in rodzaje_pol_wlasnych]

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            nowe_pole_wlasne = PoleWlasne(
                id_rodzaj=Formularz.id_rodzaj.data,
                wartosc=Formularz.wartosc.data,
                id_przedmiot=ID
            )

            DB.session.add(nowe_pole_wlasne)
            DB.session.commit()

            FLASH(f"Pole własne '{nowe_pole_wlasne.typ_pola_wlasnego.nazwa}: {nowe_pole_wlasne.wartosc}' zostało dodane.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Pole_Włsne_Dodanie.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/pola-wlasne/edytuj/<int:ID_Pole_Wlasne>/", methods=["POST", "GET"])
def Widok_Kolekcja_Pole_Własne_Edytuj(ID_Przedmiot, ID_Pole_Wlasne):
    edytowane_pole_wlasne = DB.session.execute(
        DB.select(PoleWlasne)
        .join(Przedmiot)
        .filter(
            PoleWlasne.id == ID_Pole_Wlasne,
            PoleWlasne.id_przedmiot == ID_Przedmiot,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    if not edytowane_pole_wlasne:
        FLASH("Nie znaleziono pola własnego do edycji lub nie masz do niego uprawnień.", "danger")
        ABORT(404)

    Formularz = Formularz_Pole_Własne()

    rodzaje_pol_wlasnych = DB.session.execute(DB.select(PoleWlasneRodzaj)).scalars().all()
    Formularz.id_rodzaj.choices = [(str(r.id), r.nazwa) for r in rodzaje_pol_wlasnych]

    if REQUEST.method == "GET":
        Formularz.id_rodzaj.data = edytowane_pole_wlasne.id_rodzaj
        Formularz.wartosc.data = edytowane_pole_wlasne.wartosc

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            edytowane_pole_wlasne.id_rodzaj = Formularz.id_rodzaj.data
            edytowane_pole_wlasne.wartosc = Formularz.wartosc.data

            DB.session.commit()
            FLASH(f"Pole własne '{edytowane_pole_wlasne.typ_pola_wlasnego.nazwa}: {edytowane_pole_wlasne.wartosc}' zostało zaktualizowane.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID_Przedmiot))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Pole_Włsne_Edycja.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/pola-wlasne/usun/<int:ID_Pole_Wlasne>/", methods=["POST"])
def Widok_Kolekcja_Pole_Własne_Usuń(ID_Przedmiot, ID_Pole_Wlasne):
    Pole_Wlasne_Do_Usuniecia = DB.session.execute(
        DB.select(PoleWlasne)
        .join(Przedmiot)
        .join(PoleWlasneRodzaj)
        .filter(
            PoleWlasne.id == ID_Pole_Wlasne,
            PoleWlasne.id_przedmiot == ID_Przedmiot,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    if not Pole_Wlasne_Do_Usuniecia:
        FLASH("Nie można odnaleźć pola własnego do usunięcia lub nie masz do niego uprawnień.", "danger")
        ABORT(404)

    nazwa_typu_pola = Pole_Wlasne_Do_Usuniecia.typ_pola_wlasnego.nazwa

    DB.session.delete(Pole_Wlasne_Do_Usuniecia)
    DB.session.commit()

    FLASH(f"Pole własne '{nazwa_typu_pola}: {Pole_Wlasne_Do_Usuniecia.wartosc}' zostało pomyślnie usunięte.", "success")
    return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID_Przedmiot))

@Blueprint_3.route("/moja-kolekcja/<int:ID>/grafiki/dodaj/", methods=["POST", "GET"])
def Widok_Kolekcja_Zdjęcie_Dodaj(ID):
    przedmiot_parent = DB.session.execute(
        DB.select(Przedmiot).filter_by(id=ID, id_wlasciciel=CURRENT_USER.id)
    ).scalar_one_or_none()

    if not przedmiot_parent:
        FLASH("Nie znaleziono przedmiotu lub nie masz uprawnień do dodawania grafik do niego.", "danger")
        ABORT(404)

    Formularz = Formularz_Zdjecie()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            zdjecie_dane_binarne = Formularz.zdjecie_plik.data.read()
            mimetype_pliku = Formularz.zdjecie_plik.data.mimetype

            nowe_zdjecie = Zdjecie(
                id_przedmiot=ID,
                zdjecie_dane=zdjecie_dane_binarne,
                tytul=Formularz.tytul.data,
                opis=Formularz.opis.data,
                mimetype=mimetype_pliku
            )

            DB.session.add(nowe_zdjecie)
            DB.session.commit()

            FLASH(f"Zdjęcie '{nowe_zdjecie.tytul}' zostało dodane.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Zdjęcie_Dodanie.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/grafiki/<int:ID_Grafika>/", methods=["POST", "GET"])
def Widok_Kolekcja_Zdjęcie_Edytuj(ID_Przedmiot, ID_Grafika):
    edytowane_zdjecie = DB.session.execute(
        DB.select(Zdjecie)
        .join(Przedmiot)
        .filter(
            Zdjecie.id == ID_Grafika,
            Zdjecie.id_przedmiot == ID_Przedmiot,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    if not edytowane_zdjecie:
        FLASH("Nie znaleziono grafiki do edycji lub nie masz do niej uprawnień.", "danger")
        ABORT(404)

    Formularz = Formularz_Zdjecie()

    Formularz.zdjecie_plik.validators = [x for x in Formularz.zdjecie_plik.validators if not isinstance(x, FileRequired)]

    if REQUEST.method == "GET":
        Formularz.tytul.data = edytowane_zdjecie.tytul
        Formularz.opis.data = edytowane_zdjecie.opis

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            edytowane_zdjecie.tytul = Formularz.tytul.data
            edytowane_zdjecie.opis = Formularz.opis.data

            if Formularz.zdjecie_plik.data and Formularz.zdjecie_plik.data.filename:
                edytowane_zdjecie.zdjecie_dane = Formularz.zdjecie_plik.data.read()
                edytowane_zdjecie.mimetype = Formularz.zdjecie_plik.data.mimetype

            DB.session.commit()

            FLASH(f"Grafika '{edytowane_zdjecie.tytul}' została zaktualizowana.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID_Przedmiot))

        FLASH("Wystąpiły błędy w formularzu. Popraw dane i spróbuj ponownie.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Zdjęcie_Edycja.html", Formularz=Formularz)

@Blueprint_3.route("/moja-kolekcja/<int:ID_Przedmiot>/grafiki/usun/<int:ID_Grafika>/", methods=["POST"])
def Widok_Kolekcja_Zdjęcie_Usuń(ID_Przedmiot, ID_Grafika):
    Zdjecie_Do_Usuniecia = DB.session.execute(
        DB.select(Zdjecie)
        .join(Przedmiot)
        .filter(
            Zdjecie.id == ID_Grafika,
            Zdjecie.id_przedmiot == ID_Przedmiot,
            Przedmiot.id_wlasciciel == CURRENT_USER.id
        )
    ).scalar_one_or_none()

    if not Zdjecie_Do_Usuniecia:
        FLASH("Nie można odnaleźć grafiki do usunięcia lub nie masz do niej uprawnień.", "danger")
        ABORT(404)

    tytul_zdjecia = Zdjecie_Do_Usuniecia.tytul

    DB.session.delete(Zdjecie_Do_Usuniecia)
    DB.session.commit()

    FLASH(f"Grafika '{tytul_zdjecia}' została pomyślnie usunięta.", "success")
    return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Szczegóły", ID=ID_Przedmiot))
