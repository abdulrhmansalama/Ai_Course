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
    def show_grades(self):
        for i in self.subjects.items():            
            print (i ) 
            

            
class subject :
    def __init__ (self, subject_name):
        self.subject_name=subject_name
        self.grades = []
        
    def add_grades(self, g):
        if  0>g>100 :
            self.grades.append(g)
        else:
            print ("Invalid Grade")
    

def save_student_data(students):
    with open("students.text", 'w') as f:
        for student in students:
            f.write(f"{student.name},{student.subject},{student.grade}\n")

def load_students():

    students = {}
    with open("students.text", 'r') as file:
        for i in file:
            student_name, subject_name, grade = i.strip().split(',')
            
            students[student_name].add_subject(Subject(subject_name))
            students[student_name].add_grade(subject_name, float(grade))
    return students

def interface ():
    students=load_students():
        while True :
            print("____select____")
            print("[1]  add          student.")
            print("[2]  add subject & grades.")
            print("[3]  view student  grades.")
            print("[4]  seve    load    data.")
            print("__________________________")
            selected=int(input('Enter your option:'))
            if   selected==1:
                name=input('Enter the Student Name: ')
                students[name]=Student(name)
            elif  selected==2:
                try:
                    name=input('Enter the Student  Name: ')
                    subj=input('Enter the Subject Name: ')
                    grade=float(input('Enter the Grade: '))
                    students[name].add_subject(subj)
                    students[name].add_grade(subj,grade)
                except ValueError:
                    print ('Incorrect input of Grade! Please enter numeric value only.')
            elif selected ==3:
                with open("students.txt", "r") as file:
                    students = []
                    for line in file:
                        student_data = line.strip().split(":")
                        students.append(student_data)
                for student in students:
                    print(f"Student name: {student[0]}, Grade: {student[1]}")
            if    selected==4:
                name = input("Enter your name: ")
                subjeCt = input("Enter your subject: ")
                grade = float(input("Enter your grade: "))
                data = f"{name}: {subjeCt}: {grade}\n"
                with open("students.txt", "a") as file:
                    file.write(data)
                print("Data has been saved to the file.")
                 
            else:
                print ("Invalid Option!!\n")    


