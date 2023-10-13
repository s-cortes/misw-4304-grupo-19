import os


class DatabaseUtil():
    def generate_database_uri():
        DB_USER = os.environ["DB_USER"]
        DB_PASSWORD = os.environ["DB_PASSWORD"]

        DB_HOST = os.environ["DB_HOST"]
        DB_PORT = os.environ["DB_PORT"]
        DB_NAME = os.environ["DB_NAME"]

        return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
