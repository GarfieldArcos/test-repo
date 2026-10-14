#Kapitel 1: 
#Kapitel 2:
#Kapitel 3:
#Kapitel 4:
from datetime import date
import mysql.connector

print("Fahrrad erfassen")

rahmenNr = input("Rahmennummer (1–6 Zeichen): ")

while len(rahmenNr) > 6 or len(rahmenNr) == 0:
    if len(rahmenNr) > 6:
        print("Die Rahmennummer ist zu lang.")
    elif len(rahmenNr) == 0:
        print("Die Rahmennummer fehlt.")

    rahmenNr = input("Rahmennummer (1–6 Zeichen): ")



tagesmietpreis = input("Tagespreis: ")
jahr = int(input("Anschaffungsjahr: "))
monat = int(input("Anschaffungsmonat: "))
tag = int(input("Anschaffungstag: "))
artikelNr = int(input("Artikelnummer: "))

tagesmietpreis = tagesmietpreis.replace(",", ".")
tagesmietpreis = float(tagesmietpreis)
anschaffungsdatum = date(jahr, monat, tag)
datum = anschaffungsdatum.strftime("%Y.%m.%d")
datum = datum.replace(".", "-")
print("Übernommen: ", rahmenNr)

connection = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="fahrradverleih",
)
cursor = connection.cursor()

sql = """
INSERT INTO fahrraeder (rahmenNr, tagesmietpreis, anschaffungsdatum, artikelNr)
VALUES (%s, %s, %s, %s);
"""

daten = (rahmenNr, tagesmietpreis, anschaffungsdatum, artikelNr)

cursor.execute(sql, daten)

connection.commit()
cursor.close()
connection.close()

print("Fahrrad gespeichert.")
