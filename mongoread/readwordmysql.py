import mysql.connector
import os
import cchardet as chardet
import codecs

# MySQL adatbázis kapcsolat létrehozása
conn = mysql.connector.connect(
    host="192.168.0.64",
    user="mzsolt",
    password="MeuGnaE4",
    database="word"
)

cursor = conn.cursor()

# Tábla létrehozása, ha még nem létezik
cursor.execute("CREATE TABLE IF NOT EXISTS wordstwo (id INT AUTO_INCREMENT PRIMARY KEY, word VARCHAR(255))")
cursor.execute("ALTER TABLE wordstwo MODIFY word VARCHAR(1000)")

# Fájl karakterkódolásának megtippelése
with open("D:\\crackstation\\realuniq.lst", "rb") as file:
    result = chardet.detect(file.read(4096))  # Csak az első 4096 bájtot olvassuk be
    
    print(result["encoding"])

# Fájl beolvasása
print("Indul a beolvasás")
with open("D:\\crackstation\\realuniq.lst", "r", encoding="ISO-8859-1") as file:
    for line in file:
        word = line.strip()
        if len(word) <= 1000:
            cursor.execute("INSERT INTO wordstwo (word) VALUES (%s)", (word,))
        else:
            print("Túl hosszú string: " + word)

# Változások mentése és kapcsolat bezárása
conn.commit()
print("END")

cursor.close()
conn.close()
