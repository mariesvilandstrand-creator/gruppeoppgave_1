#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne
def legg_til_nytt_emne():
    semester=input("Er det vår elller høst").lower().strip()
    if semester==("vår"):
        print("emne ftgjjgj")
        
while True:
    ip = input("Hva vil du gjøre?")
    match ip:
        case "add":
            legg_til_nytt_emne()
        case "avslutt":
            break
        case _:
            print("ugyldig commando:", ip)

emnekode=input("hva er emnekoden?")

    

emnekode_liste=[]

semester_liste=[]

antall_studiepoeng=[]


