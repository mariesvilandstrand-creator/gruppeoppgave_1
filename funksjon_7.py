#Les inn emnene og studieplanen fra fil. Denne skal lese samme fil som bel skrevet i
#punkt 6.

import csv

with open("studieplan_fil.csv", "r") as fila:
    csvreader = csv.reader(fila)
rader=list(csvreader)

for rad in rader:
    if not rad:
        continue
    if rad[0]=="1":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")

for rad in rader:
    if not rad:
        continue
    if rad[0]=="2":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")

for rad in rader:
    if not rad:
        continue
    if rad[0]=="3":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")

for rad in rader:
    if not rad:
        continue
    if rad[0]=="4":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")

for rad in rader:
    if not rad:
        continue
    if rad[0]=="5":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")
            
for rad in rader:
    if not rad:
        continue
    if rad[0]=="6":
        print(f"{rad[0]} semester, emnekode: {rad[1]}, studiepoeng: {rad[2]}")