"""
    ;dsjlkdfnmglkfd
"""

# Ogólne URL'e

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE

#! Lokalne Importy
from Aplikacja.Main import Blueprint_1

#! Main
@Blueprint_1.route("/")
def Widok_Main_Index():
    """
        Strona główna.
    """
    return RENDER_TEMPLATE("Main/index.html")

@Blueprint_1.route("/o-programie/")
def Widok_Main_O_Programie():
    """
        Strona z podstawowymi informacjami o programie.
    """

    return RENDER_TEMPLATE("Main/O_Programie.html")

@Blueprint_1.route("/polityka-prywatnosci/")
def Widok_Main_Polityka_Prywatności():
    """
        Strona z informacjami na temat polityki prywatności.
    """

    return RENDER_TEMPLATE("Main/Polityka_Prywatności.html")