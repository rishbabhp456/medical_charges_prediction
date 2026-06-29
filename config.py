import os

MONGO_URL = "mongodb://localhost:27017"
db_name = "test_db"
user_collection_name = "collection_user"
data_collection_name = "collection_data"

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

ML_MODEL_PATH = os.path.join(os.getcwd(), "artifacts", "LR_med_ins.pkl")
INPUT_DATA_PATH = os.path.join(os.getcwd(), "data", "medical_insurance.csv")
JSON_DATA_PATH = os.path.join(os.getcwd(), "artifacts", "med_ins_column_data.json") 