def emne_i_studieplan(self):
    for i in range (6):
        print (f"\n semester 1: \n {self.emnekode[i]}")


class Emne():
    def __init__(self, navn, emnekode, semester, studiepoeng):
        self.navn = navn
        self.emmnekode = emnekode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"\n navn : {self.navn} \n emnekode : {self.emnekode} \n semester : {self.semester} \n studiepoeng : {self.studiepoeng} \n"
    

class Studieplan():
    def __init__(self, ID, navn, emne):
        self.ID = ID
        self.navn = navn
        self.emne = {
            
        }
            
    
    def __str__(self):
        return f"\n student-ID : {self.ID} \n studie : {self.navn} \n emne :{emne_i_studieplan()} "