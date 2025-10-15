#Sjekk om studieplanen er gyldig eller ikke. En studieplan er bare gyldig hvis hvert av de
#seks semestrene inneholder 30 studiepoeng emner. Er ikke studieplanen gyldig, skriv ut
#hvilke semestre som ikke er gyldige og hvor mange studiepoeng emner det er i det
#semesteret.


def sjekk_studieplan(studieplan_liste , studiepoeng_liste):
    for i in range(len(studieplan_liste))