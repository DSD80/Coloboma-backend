from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("DBURL")
client = MongoClient(url)

db = client["databaseColo"]

user= db["myclients"]