"""Moduł z komendami CLI (Command Line Interface) dla aplikacji.

Ten moduł wykorzystuje `Click` do tworzenia niestandardowych komend
terminalowych, głównie do zarządzania tłumaczeniami za pomocą `pybabel`.
"""

import os as OS

import click as CLICK
from flask import Blueprint as BLUEPRINT

Blueprint_CLI = BLUEPRINT("cli", __name__, cli_group=None)


@Blueprint_CLI.cli.group()
def translate():
    """Grupa komend do zarządzania tłumaczeniami."""
    pass


@translate.command()
@CLICK.argument("język")
def init(język):
    """Inicjalizuje nowe tłumaczenie dla podanego języka.

    Generuje plik `.pot`, a następnie na jego podstawie tworzy
    strukturę katalogów i plik `.po` dla nowego języka.

    :param język: Kod języka (np. 'en', 'de').
    :type język: str
    """
    if OS.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("Polecenie 'extract' wygenerowało błąd.")

    if OS.system("pybabel init -i messages.pot -d Aplikacja/Tłumaczenia -l " + język):
        raise RuntimeError(
            f"Polecenie 'init' wygenerowało błąd podczas dodawania języka '{język}'."
        )
    OS.remove("messages.pot")


@translate.command()
def update():
    """Aktualizuje wszystkie istniejące pliki tłumaczeń.

    Wyciąga nowe ciągi znaków do tłumaczenia z kodu do pliku `.pot`,
    a następnie aktualizuje istniejące pliki `.po`.
    """
    if OS.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("Polecenie 'extract' wygenerowało błąd.")

    if OS.system("pybabel update -i messages.pot -d Aplikacja/Tłumaczenia"):
        raise RuntimeError("Polecenie 'update' wygenerowało błąd.")
    OS.remove("messages.pot")


@translate.command()
def compile():
    """Kompiluje pliki tłumaczeń `.po` do plików `.mo`.

    Pliki `.mo` są wykorzystywane przez aplikację do wyświetlania
    przetłumaczonych tekstów.
    """
    if OS.system("pybabel compile -d Aplikacja/translations"):
        raise RuntimeError("Polecenie 'compile' wygenerowało błąd.")
