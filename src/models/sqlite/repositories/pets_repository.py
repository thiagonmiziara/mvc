from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as db:
            try:
                pets = db.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connection as db:
            try:
                db.session.query(PetsTable).filter(PetsTable.name == name).delete()
                db.session.commit()
            except Exception as exeption:
                db.session.rollback()
                raise exeption
