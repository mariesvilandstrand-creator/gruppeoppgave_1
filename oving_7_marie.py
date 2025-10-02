#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne

def legg_til_nytt_emne():
    semester=input("Er det vår elller høst").lower().strip()
    if semester==("vår"):
        print("emne ftgjjgj")
        
def legg_til_emne():

    
        
while True:
    ip = input("Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" | "ne":
            legg_til_nytt_emne()
        case "2" | "lte":
            legg_til_emne()
        case "3" | "sul"
            skriv_ut_liste()
        case "4" | "sus"
            skriv_ut_studieplan()
        case "5" | "stg":
            sjekk_studieplan_gyldig()
        case "6" | "lesf":
            lagre_emne_studieplan_fil()
        case "7" | "lin":
            les_inn()
        case "8" | "abort":
            break
        case _:
            print("ugyldig commando:", ip)

emnekode=input("hva er emnekoden?")

    

emnekode_liste=[]

semester_liste=[]

antall_studiepoeng=[]
