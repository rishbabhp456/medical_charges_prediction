import os


db_name = "med_ins_db"
MONGO_USER = "rishabhp"
MONGO_PASSWORD = "test123$" ## Safely encode the password to convert the '!' into its URL-friendly format (%21)
user_collection_name = "collection_user"
data_collection_name = "collection_data"
MONGO_URL = f"mongodb+srv://rishabhp:{MONGO_PASSWORD}@docdb-cluster-20260630-0923.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"


FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

ML_MODEL_PATH = os.path.join(os.getcwd(), "artifacts", "linear_reg_med_ins.pkl")
INPUT_DATA_PATH = os.path.join(os.getcwd(), "data", "medical_insurance.csv")
INPUT_COLUMN_DATA = os.path.join(os.getcwd(), "artifacts", "med_ins_column_data.json") 
