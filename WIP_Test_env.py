"""
    Program do testowania zmiennych środowiskowych.

    Źródło: https://stackoverflow.com/a/61029741
"""

import os as OS
from dotenv import load_dotenv as LOAD_DOTENV

LOAD_DOTENV()

WIP_1 = OS.getenv("SECRET_KEY")

print(f"SECRET_KEY: '{WIP_1}'")