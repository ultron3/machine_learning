import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["magazzino_farmaci"]
print(mydb.list_collection_names())
mycul=mydb["pharm"]

nome=input("aggiungo il nome del farmaco: ")
prezzo=float(input("aggiungo il prezzo: "))
giacenza=int(input("aggiungo la giacenza: "))
giacenza_minima=int(input("aggiungo la soglia di giacenza minima : "))
disponibile=input("aggiungo la disposnibilità: ")
uso=input("aggiungo il tipo di uso : ")

farmaci={
    "nome":nome,
    "prezzo":prezzo,
    "giacenza":giacenza,
    "giacenza_minima":giacenza_minima,
    "disponibile":disponibile,
    "uso":uso
}

ris=mycul.insert_one(farmaci)