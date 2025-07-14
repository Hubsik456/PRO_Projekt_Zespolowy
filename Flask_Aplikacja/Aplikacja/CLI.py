# TODO: Do poprawienia

import os as OS
from flask import Blueprint as BLUEPRINT
import click as CLICK

Blueprint_CLI = BLUEPRINT("cli", __name__, cli_group=None)

@Blueprint_CLI.cli.group()
def translate():
    """
        Polecenia do tłumaczenia i lokalizowania tłumaczeń.
    """

    pass

@translate.command()
@CLICK.argument("język")
def init(język):
    """
        Utworzenie tłumaczenia w nowym języku.
    """

    if OS.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("Polecenie 'init' wygenerowało błąd podczas tworzenia nowego języka.")

    if OS.system("pybabel init -i messages.pot -d Aplikacja/Tłumaczenia -l " + język):
        raise RuntimeError(f"Polecenie 'init' wygenerowało błąd podczas dodawania języla '{język}'.")

@translate.command()
def update():
    """
        Aktualizacja wszsytkich tłumaczeń.
    """

    if OS.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("Polecenie 'update' wygenerowało błąd podczas wyciągania tłumaczeń.")

    if OS.system("pybabel update -i messages.pot -d Aplikacja/Tłumaczenia"):
        raise RuntimeError("Polecenie 'update' wygenerowało błąd podczas aktualizacji tłumaczeń.")

    OS.remove("Tłumaczenia.pot")

@translate.command()
def compile():
    """
        Kompilacja wszystkich tłumaczeń.
    """

    if OS.system("pybabel compile -d Aplikacja/translations"):
        raise RuntimeError("Polecenie 'compile' wygenerowało błąd podczas kompilowania tłumaczeń.")