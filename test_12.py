liste_1=[1,3,5]
liste_2=[2,4,6]
liste_3=[7,8,9]
full_liste=[liste_1,liste_2,liste_3]
liste_ok_1=["lol","hei","hei"]
full_liste_ok=[liste_ok_1,liste_ok_1,liste_ok_1]

import csv
with open("test_1.csv", "w", encoding="UTF-8") as fila:
    skriver=csv.writer(fila)
    for i in range(len(full_liste)):
        fila.write(f"{str(full_liste[i][0])}\n")
        fila.write(f"{str(full_liste_ok[i][0])}\n")
        fila.write(f"{str(full_liste[i][1])}\n")
        fila.write(f"{str(full_liste_ok[i][1])}\n")
        fila.write(f"{str(full_liste[i][2])}\n")
        fila.write(f"{str(full_liste_ok[i][2])}\n")
    



    
    
