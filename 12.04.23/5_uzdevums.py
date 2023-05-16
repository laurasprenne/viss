import sqlite3
conn = sqlite3.connect("datasheet.db")

class PCPart:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def to_file(self):
        with open(self.model + ".txt", "w") as f:
            f.write("-Datora satavdala-\n Veids: " + self.type + "\n Modelis: " + self.model + "\n Cena: " + str(self.price))

part1 = PCPart('RAM', 'Corsair Vengeance LPX 16GB', 99.99)
part1.to_file()


cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datasheet (id INTEGER PRIMARY KEY, type VARCHAR, model VARCHAR, price FLOAT)")

cursor.execute("INSERT INTO datasheet (type, model, price) VALUES (?, ?, ?)", (part1.type, part1.model, part1.price))

cursor.execute("SELECT * FROM datasheet")
records = cursor.fetchhall()
for row in records:
    for value in row:
        print(value, end=" ")
    print()

conn.commit()
conn.close()