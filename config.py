import pymongo
import certifi

con_string = "mongodb+srv://christianalbrandaguirre:Test@fsdi-107.abicf.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(con_string, tlsCAFile = certifi.where())
db = client.get_database("organika")