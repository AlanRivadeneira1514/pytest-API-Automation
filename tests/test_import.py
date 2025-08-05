import os

import pytest
from src.api.person_api import PersonsAPI
from utils.person_generator import generate_persons
from src.db.supabase_persons_table import SupabasePersonsTable


@pytest.mark.api
@pytest.mark.persons
class TestPersonAPI:

    def setup_class(self):
        self._api = PersonsAPI(os.environ['env'])
        self._db = SupabasePersonsTable(os.environ['env'])

    @pytest.fixture()
    def delete_personid_inserted(self, person_data):
        yield
        if person_data:
            print(f"Eliminando usuario de prueba con ID {person_data['personid']}")
            res = self._db.delete_person_by_person_id(person_data["personid"])
            print(f'se elimino el usuario: {res}')

    @pytest.mark.parametrize("person_data", generate_persons(3))
    def test_post_person_and_validate_in_db(self, person_data, delete_personid_inserted):

        status,response = self._api.post_create_person(person_data)
        assert status in [200, 201]

        db_data= self._db.find_person_by_person_id(person_data["personid"])
        assert db_data is not None
        assert db_data["email"] == person_data["email"]
        assert db_data["name"] == person_data["name"]
        assert db_data["age"] == person_data["age"]
        assert db_data["personid"] == person_data["personid"]
        print(f"SUCCESS: personId POST: {person_data["personid"]}, personid Database: {response["personid"]}")

    def test_post_person_without_token(self):
        person_data = generate_persons(1)
        status, response = self._api.post_create_person(person_data, auth_token="")

        assert status == 401
        assert response["message"] == 'No API key found in request'
        assert response["hint"] == 'No `apikey` request header or url param was found.'

        print("sin token devuelve 401 Unauthorized")

    import pytest

    @pytest.mark.parametrize("field, value", [

        ("age", "veinte"),  # tipo incorrecto [string]
        ("age", None),      #campo requerido null
        ("personid", None), # campo requerido null
        ("email", None),    # campo requerido null
        #("email", "sinarroba.com"),  # mal formateado no se puede validar contra supabase


    ])
    def test_post_person_with_invalid_fields(self, field, value):
        person = generate_persons(1)[0]
        person[field] = value

        status, response = self._api.post_create_person(person)
        assert status in [400, 422]

