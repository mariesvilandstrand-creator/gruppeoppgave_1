#Les inn emnene og studieplanen fra fil. Denne skal lese samme fil som bel skrevet i
#punkt 6.

import csv

def lese_fil():
    with open("studeplan_fil.csv", "r") as fila:
        csvreader = csv.reader(fila)
    for row in csvreader:
        if not row:
            continue
        if row[0].startswith[row+1]:
            print(f"semesteret ditt er: {row[0]}, emnekoden din er {row[1]}, studiepoengene er {row[2]}")
            