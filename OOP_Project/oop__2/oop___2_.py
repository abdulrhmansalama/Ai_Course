class Student :
    def __init__(self, student_name) :
        self.student_name=student_name
        self.subjects={}
    
    def add_subject (self, subject):
        self.subjects[subject.name]=subject
    def add_agrade(self, grade, subject):
        if subject in self.subjects:
            self.subjects[subject].add_grade(grade)
        else:
            print("Error! The subject does not exist.")
            

            
class subject :
    def __init__ (self, subject_name):
        self.subject_name=subject_name
        self.grades = []
        
    def add_grade(self, g):
        if  0>g>100 :
            self.grades.append(g)
        else:
            print ("Invalid Grade")
