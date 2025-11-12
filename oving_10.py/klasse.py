




class Emne():
    def __init__(self, navn, emnekode, semester = 0, studiepoeng = 0):
        self.navn = navn
        self.emnekode = emnekode
        self.semester = semester
        self.studiepoeng = studiepoeng

    def __str__(self):
        return f"\n navn : {self.navn} \n emnekode : {self.emnekode} \n semester : {self.semester} \n studiepoeng : {self.studiepoeng} \n"
    
    def semester_til_emnet(self):
        return self.semester
    

class Studieplan():
    def __init__(self, ID, navn, semester = list(), emner = list()):
        self.ID = ID
        self.navn = navn
        self.emner = emner 
        for i in range(6):
            self.emner.append(list())
        
    
    def legg_til_emne(self, emne, semesterNr):
        for semester in self.emner:
            if emne in semester:
                print("Emne allerede i studieplan")
                return
        
        self.emner[semesterNr].append(emne)
        
    def emne_i_studieplan(self):
        for i, semester in enumerate(self.emner):
            print (f"\n semester {i+1}")
            for emne in semester:
                print(f"{emne.navn}")
            
            
    def __str__(self):
        return f"\n student-ID : {self.ID} \n studie : {self.navn} \n{self.emne_i_studieplan()})"
    
