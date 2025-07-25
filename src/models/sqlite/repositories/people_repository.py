from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.__db_connection as db:
            try:
                person_data = PeopleTable(
                    first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
                )

                db.session.add(person_data)
                db.session.commit()
            except Exception as execption:
                db.session.rollback()
                raise execption

    def get_person(self, person_id: int) -> PeopleTable:
        with self.__db_connection as db:
            try:
                person = (
                    db.session.query(PeopleTable)
                    .outerjoin(PetsTable, PeopleTable.pet_id == PetsTable.id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type"),
                    )
                    .one()
                )

                return person
            except NoResultFound:
                return None
