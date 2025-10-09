#Legg til et emne i studieplanen: En studieplan består av seks semester nummeret 1-6
#hvor semester 1, 3 og 5 er høstsemester og semester 2, 4 og 6 er vårsemestre. Hvert
#semester kan representeres som ei liste med indekser inn i emne-listene. Dere skal også
#sjekke at et emne er lovlig i det semesteret brukeren prøver å legge det inn i. Det
#involverer følgende:
#o Sjekk at emnet ikke allerede er med i studieplanen. Et emne skal bare kunne
#legges til en gang.
#o Sjekk at emnet legges til i et gyldig semester. Høstemner skal bare kunne legges
#til i semester 1, 3 eller 5. Våremner skal bare kunne legges til i semester 2, 4 eller
#6.
#o Sjekk at det er plass i semesteret til emnet. Et semester skal inneholder
#maksimalt 30 studiepoeng med emner


def legg_til_emne_i_studieplan(emnekode_liste, semester_liste, studiepoeng_liste):
    print(emnekode_liste)
    while True:
        try:
            hvilket_emne=int(input("Hvilket emne vil du legge inn i studieplanen din?(skriv inn tallet i rekken som emnet ditt er i): "))-1
            if hvilket_emne>len(emnekode_liste):
                print("feil")
                continue
            break
        except ValueError:
            print("FEIL")
    

    
    for semester in ["host", "vaar"]:
        for emne_i in range(len(emnekode_liste)):
            if semester_liste[emne_i] == semester:
                print(emnekode_liste[emne_i])