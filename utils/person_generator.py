import random
import os
from faker import Faker

fake = Faker('es_AR')

def generate_persons(n):
    """
    Genera un Dict con datos de personas aleatorias usando Faker.
    Agrega el valor de la variable de entorno 'env' como sufijo al nombre.
    :param n: Cantidad de personas a generar
    :return: Lista de dicts con estructura válida para insert
    """
    env = os.getenv('env')
    persons = []

    for _ in range(n):
        person_id = random.randint(1, 20)
        name = f"{fake.first_name()}_{env}"
        email = fake.email()
        age = random.randint(18, 60)

        person = {
            "personid": person_id,
            "name": name,
            "email": email,
            "age": age
        }
        persons.append(person)

    return persons
