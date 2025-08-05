import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()


class SupabasePersonsTable:
    def __init__(self, env):
        self._env = env
        self.table_name = f"{self._env}persons"
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_API_KEY")

        if not url or not key:
            raise ValueError("Se debe setear la url y apikey de supabase en el .env")

        self.client: Client = create_client(url, key)

    def find_person_by_person_id(self, person_id: int):
        """
        Realiza una busqueda de una persona por person_id en la tabla persons.
        :param person_id: ID numerico de la persona a consultar.
        :return: Request status and response body.
        """
        response = (
            self.client
            .table(self.table_name)
            .select("*")
            .eq("personid", person_id)
            .maybe_single()
            .execute()
        )
        return response.data

    def delete_person_by_person_id(self, person_id: int):
        """
        Elimina una persona de la tabla según el person_id.
        :param person_id: ID numérico de la persona a eliminar.
        :return: Resultado del delete.
        """
        response = (
            self.client
            .table(self.table_name)
            .delete()
            .eq("personid", person_id)
            .execute()
        )
        return response.data
