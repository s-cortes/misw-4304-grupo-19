import os

from utils.constants import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


class DatabaseUtil:
    @staticmethod
    def generate_database_uri():
        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
