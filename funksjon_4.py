#Skriv ut studieplanen med hvilke emner som er i hvert semester



def skriv_ut_studieplan(studieplan_liste):
    t=1
    for i in range(len(studieplan_liste)):
        emner = ""
        for emne in studieplan_liste[i]:
            emner += f"{emne}, "
        print(f"Semester {t} = {emner}")
        t=t+1
