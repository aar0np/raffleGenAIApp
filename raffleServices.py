import json

from astraConn import get_names_by_vector
from astraConn import put_doc
from sentence_transformers import SentenceTransformer

DATA_COLLECTION_NAME = "raffle_data"
model = None

async def submit_name(name):
	global model

	if model is None:
		# initialize the all-MiniLM-L6-v2 model locally
		model = SentenceTransformer('all-MiniLM-L6-v2')

	vector_embedding = model.encode(name)
	strJson = (f'{{"_id":"{name.replace(" ","")}","name":"{name}","$vector":{str(vector_embedding.tolist())}}}')
	doc = json.loads(strJson)

	# await needed?
	await put_doc(DATA_COLLECTION_NAME, doc)

async def get_names(search_string):
	global model

	if model is None:
		# initialize the all-MiniLM-L6-v2 model locally
		model = SentenceTransformer('all-MiniLM-L6-v2')

	vector_embedding = model.encode(search_string)
	results = await get_names_by_vector(DATA_COLLECTION_NAME, vector_embedding, 50)

	return results
