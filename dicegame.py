#gioco di dati 


import random



def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value)
    return roll


while True:
    playersCount = input("Numero di giocatori (2-4): ")
    if playersCount.isdigit():
        playersCount = int(playersCount)
        if 2 <= playersCount <= 4:
            break

max_score = 50
players_scores = [ 0 for _ in range(playersCount)]


while max(players_scores) < max_score:
    
    for  giocatori in range(playersCount):
        print("\n Turno del giocatore numero: " , giocatori + 1 )

        score_attuale = 0

        while True:

            decisione = input("\n Tiri i dadi? (y/n)")
            if decisione.lower() != "y":
                break

            
            valore = roll()
            


            if valore == 1:
                print("Hai fatto:  1, turno concluso.")
                score_attuale = 0
                break
            else:
                score_attuale = score_attuale + valore
                print("\n hai fatto: ", valore)
            

            print("il tuo punteggio è: " , score_attuale)
        print("----------------------------------------")

        


        players_scores[giocatori] += score_attuale
        print("Punteggio attuale: " , players_scores[giocatori])
        print("----------------------------------------\n")

max_score = max(players_scores)
giocatorevincente = players_scores.index(max_score)
print("Il giocatore n: " , giocatorevincente +1 , "ha vinto!!!!\n")


    
