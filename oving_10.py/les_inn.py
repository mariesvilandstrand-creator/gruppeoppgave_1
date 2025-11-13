from klasse import*

def les_inn():
    with open("studieplan_fil.txt", "r" , newline="", encoding="utf-8") as fila:
        print(fila.read())