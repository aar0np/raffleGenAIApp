import os

from astrapy.db import AstraDB

# Astra connection
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT= os.environ.get("ASTRA_DB_API_ENDPOINT")

# global cache variables to re-use a single Session
db = None
collection = None

def init_collection(table_name):
    global db
    global collection

    if db is None:
        db = AstraDB(
            token=ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
        )
    
    collection = db.collection(table_name)

async def get_names_by_vector(collection_name, vector_embedding, limit=1):
    init_collection(collection_name)

    results = collection.vector_find(vector_embedding.tolist(), limit=limit, fields={"text","name","$vector"})
    return results

async def put_doc(collection_name, document):
    init_collection(collection_name)

    collection.insert_one(document)
