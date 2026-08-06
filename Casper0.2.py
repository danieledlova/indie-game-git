#Casper 0.2

import re
from bs4 import BeautifulSoup
import urllib.request , urllib.parse , urllib.error
from urllib.parse import urljoin
import requests
import json




nome_ia = "Casper"
risposte_utente = []
info_utente = []
argomenti = ["Meteo" , "di che vuoi parlare?" , "fammi navigare"]


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
    print("Cosa facciamo" , nome_utente , "?")
    for x , y in enumerate(argomenti):
         print(x , y)
    reqU = domanda()

    if reqU == "0" or reqU == "meteo":
        meteo()


    if reqU == "1" or reqU == "di che vuoi parlare?":
        print("vuoi che ti racconto una barzelletta?")
        reqU = domanda()
        if reqU == "si":
            print(".....")
        else:
            print("ok come vuoi")
            print("\n")
            continue


    
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

            
    
            
        














    if reqU == "esci":
        print("Okey ciao!")
        print("Ecco la tua cronologia \n" , info_utente ,  risposte_utente)
        exit()


