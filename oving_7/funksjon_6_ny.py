

def lagre_emne_studieplan_fil(studieplan_liste, studiepoeng_sum):
    with open ("studieplan_fil.txt", "w", newline="", encoding="UTF-8") as fila:
        for i, semester in enumerate(studieplan_liste):
            fila.write(f"Semester, {i+1}, Antall studiepoeng: , {sum(studiepoeng_sum[i])}\n")
            for j, emne in enumerate(semester):
                fila.write(f"{emne}, studiepoeng: {studiepoeng_sum[i][j]} \n")