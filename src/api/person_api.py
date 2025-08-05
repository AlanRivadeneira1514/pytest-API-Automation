import os
import requests
from dotenv import load_dotenv

load_dotenv()

class PersonsAPI:
    def __init__(self, env):
        self._env = env
        self.base_url = os.getenv("SUPABASE_REST_API_URL")
        self.api_key = os.getenv("SUPABASE_API_KEY")
        if not self.base_url:
            print("Se debe setear la baseurl en el .env")


    def post_create_person(self, person_data: dict, auth_token=None):
        """
        Realiza una petición /POST al endpoint REST de Supabase para insertar una persona.

        :param auth_token: supabase authentication token
        :param person_data: Diccionario con los datos de la persona.
        :return: Objeto requests.Response
        """
        token = auth_token if auth_token is not None else self.api_key
        headers = {
            "apikey": token,
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"  # esta linea es para que devuelva los datos insertados
        }
        response = requests.post(f'{ self.base_url}/{self._env}persons', json=person_data, headers=headers)
        res=response.json() #en ocasiones supabase retorna valores con indice [0] se opto por manejar el caso en el return
        return response.status_code, res[0] if isinstance(res, list) else res