#Lagre emnene og studieplanen til fil. Lag ei eller flere tekstfiler med denne
#informasjonen, det er opp til dere å finne ut hvilket format denne fila skal ha

def lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_liste):
    with open ("studieplan_fil.csv", "a", encoding="UTF-8") as fila:
        for i in len(studieplan_liste[i]):
            fila.write(f"1, {studieplan_liste[i][0]}, {studiepoeng_liste[i][0]}")
        for i in len(studieplan_liste[i]):
            fila.write(f"2, {studieplan_liste[i][1]}, {studiepoeng_liste[i][1]}")               
        for i in len(studieplan_liste[i]):
            fila.write(f"3, {studieplan_liste[i][2]}, {studiepoeng_liste[i][2]}")
        for i in len(studieplan_liste[i]):
            fila.write(f"4, {studieplan_liste[i][3]}, {studiepoeng_liste[i][3]}")
        for i in len(studieplan_liste[i]):
            fila.write(f"5, {studieplan_liste[i][4]}, {studiepoeng_liste[i][4]}")
        for i in len(studieplan_liste[i]):
            fila.write(f"6, {studieplan_liste[i][5]}, {studiepoeng_liste[i][5]}")