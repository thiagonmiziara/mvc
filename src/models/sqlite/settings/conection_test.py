import pytest
from sqlalchemy import Engine
from .conection import db_connection_handler


@pytest.mark.skip(reason="Skipping test for db connection")
def test_db_connection():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.conect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
