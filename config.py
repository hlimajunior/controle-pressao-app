import os


class Config:
    """Configurações da aplicação"""

    SECRET_KEY = os.environ.get(
        "SECRET_KEY") or "chave-secreta-desenvolvimento-2024"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL") or "sqlite:///controles.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
