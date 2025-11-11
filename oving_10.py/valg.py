
from legg_til_emne import*

while True:
    with open("oving_10.py\menyvalg_tekst", "r", encoding="UTF-8") as fila:
        print(fila.read())
    ip = input(f"Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" :
            Legg_til_nytt_emne(emnekode_liste)
        case "2" :
            
        case "3" :
            
        case "4" :
            
        case "5" :
            
        case "6" :
            
        case "7" :
            
        case "8" :
            break
        case _:
            print("ugyldig commando:", ip)