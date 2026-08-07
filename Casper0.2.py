#Casper 0.2

from bs4 import BeautifulSoup
import urllib.request , urllib.parse
from urllib.parse import urljoin
import requests
import json, ssl




nome_ia = "Casper"
risposte_utente = []
info_utente = []
argomenti = ["Meteo" , "di che vuoi parlare?" , "fammi navigare" , "trovami questa città"]


#----------definizioni


def domanda():
    reqU = input()
    risposte_utente.append(reqU)
    return reqU

def dati_nome():
    dati_nome = input()
    info_utente.append(dati_nome)
    return dati_nome
    
    


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
print("Come ti chiami")
nome_utente = dati_nome()

while True:
    print("\n Cosa facciamo" , nome_utente , "?")
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

            
    
            
        














    if reqU == "esci":
        print("Okey ciao!")
        print("Ecco la tua cronologia \n" , info_utente ,  risposte_utente)
        exit()


