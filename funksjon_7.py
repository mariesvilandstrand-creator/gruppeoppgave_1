#Les inn emnene og studieplanen fra fil. Denne skal lese samme fil som bel skrevet i
#punkt 6.

def les_inn():
    with open("studieplan_fil.txt", "r" , newline="", encoding="utf-8") as fila:
        print(fila.read())