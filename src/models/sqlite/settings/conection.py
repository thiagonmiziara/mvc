from sqlalchemy import create_engine


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__conection_string: str = "sqlite:///storage.db"
        self.__engine = None

    def conect_to_db(self):
        self.__engine = create_engine(self.__conection_string, echo=True)

    def get_engine(self):
        return self.__engine


db_connection_handler = DBConnectionHandler()
