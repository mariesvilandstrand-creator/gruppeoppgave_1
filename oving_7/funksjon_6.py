#Lagre emnene og studieplanen til fil. Lag ei eller flere tekstfiler med denne
#informasjonen, det er opp til dere å finne ut hvilket format denne fila skal ha
import csv

def lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_liste):
    with open ("studieplan_fil.csv", "a", encoding="UTF-8") as fila:
        skriver=csv.writer(fila)
        for i in range(len(studieplan_liste)):
            fila.write(f"1, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")
        for i in range(len(studieplan_liste)):
            fila.write(f"2, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")    
        for i in range(len(studieplan_liste)):
            fila.write(f"3, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")
        for i in range(len(studieplan_liste)):
            fila.write(f"4, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")
        for i in range(len(studieplan_liste)):
            fila.write(f"5, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")
        for i in range(len(studieplan_liste)):
            fila.write(f"6, {studieplan_liste[i]}, {int(studiepoeng_liste[i])}\n")