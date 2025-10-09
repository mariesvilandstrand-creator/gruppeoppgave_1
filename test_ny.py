#Lag et nytt emne: Et emne skal ha minimum en emnekode, om emnet undervises høst
#eller vår, og antall studiepoeng. Dere kan lagre dette i tre lister, en for emnekoder, en for
#semester (høst eller vår) og en for antall studiepoeng, og hvor samme indeks i de tre
#listene representerer samme emne


from funksjon_1 import*

from funksjon_2_ny import*

from funksjon_3 import*

from funksjon_4 import*

semester_liste=[]
emnekode_liste=[]
studiepoeng_liste=[]
aarstid_liste=[]
studieplan_liste=[[],[],[],[],[],[]]
studiepoeng_sum=[[],[],[],[],[],[]]


        

def sjekk_studieplan_gyldig():
    print("...")

def lagre_emne_studieplan_fil():
    print("...")

def les_inn():
    print("...")
        
while True:
    ip = input("Hva vil du gjøre?").lower().strip()
    match ip:
        case "1" | "ne":
            legg_til_nytt_emne(emnekode_liste, semester_liste, studiepoeng_liste, aarstid_liste)
        case "2" | "lte":
            funksjon_2_ny(studieplan_liste, semester_liste, emnekode_liste, studiepoeng_sum, studiepoeng_liste)
        case "3" | "sul":
            skriv_ut_liste(emnekode_liste, semester_liste, studiepoeng_liste)
        case "4" | "sus":
            skriv_ut_studieplan(studieplan_liste)
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

print(emnekode_liste)