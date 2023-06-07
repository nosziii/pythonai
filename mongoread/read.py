from pymongo import MongoClient

# MongoDB adatbázis kapcsolat létrehozása
# client = MongoClient("mongodb://your_username:your_password@your_host:your_port/your_database")
client = MongoClient("mongodb://192.168.0.64:27017")
db = client["pssword"]
words_collection = db["words"]

# Txt fájl beolvasása
with open("D:\crackstation\diceware8k.txt", "r") as file:
    for line in file:
        word = line.strip()
        words_collection.insert_one({"word": word})

# Kapcsolat bezárása
client.close()
