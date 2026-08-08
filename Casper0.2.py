#Casper 0.2

from bs4 import BeautifulSoup
import urllib.request , urllib.parse
from urllib.parse import urljoin
import requests
import json, ssl
import sqlite3





connSQlite = sqlite3.connect("Casperdatabase0.1.sqlite")
cur = connSQlite.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Memoria (nomeUtente TEXT ,
richieste TEXT)''')



nome_ia = "Casper"
risposte_utente = []
argomenti = ["Meteo" , "di che vuoi parlare?" , "fammi navigare" , "trovami questa città" , "esci"]


#----------definizioni


def domanda():
    reqU = input()
    cur.execute('''INSERT INTO Memoria (nomeUtente , richieste) VALUES (? , ?)''' , (nomeU , reqU,))
    connSQlite.commit()
    risposte_utente.append(reqU)
    return reqU
   


def meteo():
            
        url = ("https://api.open-meteo.com/v1/forecast"
        "?latitude=43.5443"
            "&longitude=10.3262"
            "&current=temperature_2m")

        
        urlresponse = requests.get(url)
        
        if urlresponse.ok:


            data = urlresponse.json()

            temperatura = data["current"]["temperature_2m"]
            print("a Livorno ci sono" , temperatura)

        else:
            print("Errore nella lettura del sito")
            



#----------PROGRAMMA



print("Ciao, sono ", nome_ia)
nomeU = input("Come ti chiami?: ")

cur.execute('''INSERT INTO Memoria (nomeUtente) VALUES (?)''' , (nomeU,)) 
connSQlite.commit()

while True:
    print("\n Cosa facciamo" , nomeU , "?")
    for x , y in enumerate(argomenti):
         print(x , y)
    reqU = domanda()

    #meteo

    if reqU == "0" or reqU == "meteo":
        meteo()

    #barzellette

    if reqU == "1" or reqU == "di che vuoi parlare?":
        print("vuoi che ti racconto una barzelletta?")
        reqU = domanda()
        if reqU == "si":
            print(".....")
        else:
            print("ok come vuoi")
            print("\n")
            continue

    #navigazione su links
    
    if reqU == "2" or reqU == "fammi navigare":
        url = input("inserisci link: ")
        if not url.startswith("https:"):
            print("Link non valido")
            exit()

        while True:


            conn = []
            html = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup("a")
            for tag in tags:
                link = tag.get("href")
                if link:
                    conn.append(link)
            for num, way in enumerate(conn):
                print(num, way)


            scelta = input("\nDove vuoi andare?\n")

            if scelta.lower() == "esci":
                break

            try:
                strada = int(scelta)
            except ValueError:
                print("Inserisci un numero valido.")
                continue

            if strada < 0 or strada >= len(conn):
                print("Collegamento non trovato")
                continue

            url = urljoin(url, conn[strada])

    #geoposition

    if reqU == "3" or reqU == "trovami questa città":
        serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        cittàreq = input("Inserisci città: ")
        d = {}
        d["q"] = cittàreq

        url = serviceurl + urllib.parse.urlencode(d)

        urlh = urllib.request.urlopen(url , context=ctx)
        data = urlh.read().decode()
        datajson = json.loads(data)
        print("\n longitudine: " , datajson["features"][0]["properties"]["lon"])
        print(" latitudine: " , datajson["features"][0]["properties"]["lat"]) 
        print(datajson["features"][0]["properties"]["country_code"])
        print(datajson["features"][0]["properties"]["state"]) 
        print("---------------------------------------")         

            
    
            

    if reqU == "esci" or reqU == "4":
        print("Okey ciao!")
        exit()


