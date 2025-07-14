"""
    Program do sprawdzania czy jesteś obecnie w venv.

    Źródło: https://stackoverflow.com/a/1883251
"""

import sys as SYS

Prefix = SYS.prefix
Base_Prefix = SYS.base_prefix

print(f"Prefix: \t{Prefix}")
print(f"Base Prefix: \t{Base_Prefix}")

if Prefix == Base_Prefix:
    print("Venv: Nie")
else:
    print("Venv: Tak")