import pymongo
from config import MONGO_URL

try:
    print("Attempting connection...")
    # serverSelectionTimeoutMS=5000 forces it to fail quickly (5 seconds) if blocked
    client = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ SUCCESS: Connected to Azure Cosmos DB!")
except Exception as e:
    print(f"❌ FAILED: {e}")