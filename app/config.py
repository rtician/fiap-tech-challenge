import os

DATABASE_URL = ""

CONFIG_DB_HOST: str = os.getenv("CONFIG_DB_HOST", "postgres")
CONFIG_DB_NAME: str = "app_db"
CONFIG_DB_USER: str = "user"
CONFIG_DB_PASSWORD: str = "randomP*ssword!"
SQLALCHEMY_DATABASE_URL: str = (
    f"postgresql://{CONFIG_DB_USER}:{CONFIG_DB_PASSWORD}@{CONFIG_DB_HOST}/{CONFIG_DB_NAME}"  # noqa
)
