#Sjekk om studieplanen er gyldig eller ikke. En studieplan er bare gyldig hvis hvert av de
#seks semestrene inneholder 30 studiepoeng emner. Er ikke studieplanen gyldig, skriv ut
#hvilke semestre som ikke er gyldige og hvor mange studiepoeng emner det er i det
#semesteret.


def sjekk_studieplan(studieplan_liste , studiepoeng_sum):
    for i in range(6):
        if sum(studiepoeng_sum[i])==30:
            print(f"Du har lagt til nok emner i faget ditt i semester {i+1}")
        if sum(studiepoeng_sum[i])<30:
            print(f"du har lagt til for få emner i semester {i+1}, du må legge til flere!")