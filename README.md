# QA Automation - REST API

#### En este repositorio se simula la interacción con una API REST y una base de datos PostgreSQL (proporcionada por Supabase) para realizar operaciones sobre un servicio /POST y una tabla con informacion de personas.

---

## 📚 Descripción

El objetivo es validar el funcionamiento de una API que permite crear personas, y asegurar que las operaciones sobre la base de datos se realizan correctamente.

Se utiliza Supabase como motor de base de datos (PostgreSQL) y su **API REST** para simular el endpoint `/person`. La automatización se implementa con **Python + Pytest**.

---

## 🧱 Arquitectura del Proyecto

```text
.
├── src/
│   ├── api/
│   │   └── person_api.py                   # Encapsula llamadas a la API de Supabase
│   └── db/
│       └── supabase_persons_table.py       # Acceso a base de datos (tabla persons)
├── tests/ 
|       └── test_import.py                  # Suite de tests para la API y DB
├── utils/
│   └── person_generator.py                 # Generador de datos válidos y aleatorios
├── conftest.py                             # Configuración de entorno de ejecución
├── .env                                    # Variables de entorno (Supabase)
└── requirements.txt                        # Dependencias del proyecto
```
## ¿Como ejecuto los test?

- Instala las dependencias
    ```bash
    pip install -r requirements.txt
    ```
- Crea un archivo .env en la raiz con los siguientes valores

    ```bash
    SUPABASE_URL=https://jwcmrlnetstxzoctwnxv.supabase.co
    SUPABASE_API_KEY=sb_publishable_Ky-SL26g3HvsFPgsFMOiNA_eFm9pRfe
    SUPABASE_REST_API_URL=https://jwcmrlnetstxzoctwnxv.supabase.co/rest/v1
    ```
- Ejecuta los test, puedes ingresar el ambiente env o stage
    ```bash
     pytest tests/test_import.py --env=dev
    ```
- Tambien puedes ejecutarlo directamente en el ambiente default (dev)
    ```bash
     pytest tests/test_import.py
    ```
## ¿Qué se testea?

 ✅ Flujos válidos:

    Crear persona vía POST
    
    Verificar datos insertados vía consulta directa a Supabase
    
    Limpieza de datos con teardown posterior

❌ Flujos inválidos:

    Envío sin token → status 401
    
    Envío con personid faltante o nulo → status 400
    
    Envío con campos inválidos (tipos erróneos, nulls)
    
    Validación de que campos requeridos (personid, email, age) no aceptan None

## Herramientas utilizadas

- Pytest
- Supabase (DB + REST API)
- dotenv para manejo de configuraciones
- Requests
- Faker

## Notas

- La generación de datos aleatorios está controlada para evitar conflictos con claves únicas (personid).

- Se puede extender fácilmente con más validaciones o integración continua (CI).

- La estructura sigue principios de separación de responsabilidades y orientación a objetos, la nomenclatura del archivo de test (`tests/test_import_api.py`) se define como `test_import` dado el requerimiento del challange. En otro contexto se llamaria `person_api.py`
