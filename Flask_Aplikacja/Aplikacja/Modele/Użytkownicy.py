# Tabela z użytkownikami

#! Zewnętrzne Importy
#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB
from flask_login import UserMixin as USER_MIXIN
from sqlalchemy.sql import func as FUNC


#! Main
class Użytkownicy(USER_MIXIN, DB.Model):
    __tablename__ = "Użytkownicy"

    ID = DB.Column(DB.Integer, primary_key=True)
    Login = DB.Column(DB.String(100), unique=True, nullable=False)
    Hasło = DB.Column(
        DB.String(100), nullable=False
    )  # TODO: Czy tu na pewno ma być String(100)
    Email = DB.Column(DB.String(100), nullable=False, unique=False)
    Dodano = DB.Column(
        DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False
    )
    Opis = DB.Column(DB.Text)

    def get_id(self):
        return self.ID

    def __repr__(self):
        return f"Użytkownik ---> ID: '{self.ID}'"
