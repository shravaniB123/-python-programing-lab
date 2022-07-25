'''
Define a class person (attributes: name, department, date Of Birth). Derive two classes
employee (attributes: employee id, salary) and student (attributes: PRN, year, CGPA) from
person class. Derive two classes lab_assistant (attributes: labs) and faculty (attributes:
subject, number of research papers, qualification).
i) Create objects for lab assistant, faculties, and students.
ii) Display the data.
iii) Delete a data
iv) Find the total salary of all employees.
v) Find average CGPA of students department wise.
'''
def help():
    print('''
    MENU 
    1) Display the data.
    2) Delete  data
    3) Find the total salary of all employees.
    4) Find average CGPA of students department wise.
    5) Exit
    ''')
class person:
    def __init__(self,name, department,date_of_birth):
        self.name = name
        self.department = department
        self.date_of_birth = date_of_birth
    def display(self):
        print("Name : ",self.name)
        print("Department : ",self.department)
        print("Date of Birth : ",self.date_of_birth)

class employee(person):
    def __init__(self,emp_id,salary,name,department,date_of_birth):
        self.emp_id=emp_id
        self.salary = salary
        person.__init__(self,name,department,date_of_birth)
    def display(self):
        person.display(self)
        print("Employee_id : ",self.emp_id)
        print("Salary : ",self.salary)

class student(person):
    comp=0
    mechanical =0
    def __init__(self,prn,year,cgpa,name, department,date_of_birth):
        self.prn =prn
        self.year=year
        self.cgpa = cgpa
        person.__init__(self, name, department, date_of_birth)

        if department == "Computer":
            student.comp += cgpa
        elif department == "Mechanical":
            student.mechanical += cgpa

    def display(self):
        person.display(self)
        print("PRN : ",self.prn)
        print("Year : ",self.year)
        print("CGPA : ",self.cgpa)


class lab_assistant(employee):
    lab_salary = 0
    def __init__(self,labs,emp_id,salary,name,department,date_of_birth):
        self.labs =labs
        employee.__init__(self,emp_id,salary, name, department, date_of_birth)
        lab_assistant.lab_salary += salary

    def display(self):

        employee.display(self)
        print("labs : ",self.labs)

class faculty(employee):
    faculty_salary =0
    def __init__(self,sub_teaching,no_rpapers,qualification,emp_id,salary,name, department, date_of_birth,):
        self.sub_teaching = sub_teaching
        self.no_rpapers = no_rpapers
        self.qualification = qualification
        employee.__init__(self,emp_id,salary, name, department, date_of_birth)
        faculty.faculty_salary += salary
    def display(self):
        employee.display(self)
        print("Subject Teaching : ", self.sub_teaching)
        print("Number of Research Papers :",self.no_rpapers)
        print("Qualification : ", self.qualification)


#create objects  for lab assistant, faculties, and students.

l1 =lab_assistant("Python Lab",1001,5000,"Ramesh","Computer","09/05/1995")
l2 =lab_assistant("Chemistry Lab",1203,8000,"Yash","Chemistry","18/08/1965")
l3 =lab_assistant("Electrical Lab",1030,6000,"Mahesh","Electrical","22/01/1998")

f1=faculty("Mathematics",2,"Ph.D",2003,15000,"Anita","Chemical","12/05/1980")
f2=faculty("Operating System",4,"M.Tech",5002,25000,"Omkar","Computer","04/07/1998")
f3=faculty("Microprocessor",1,"Ph.D",3002,18000,"Gauri","Information Technology","21/02/1973")

s1=student(2030331245050,"2nd",9.25,"Tanvi Palkar","Computer","01/02/2003")
s2=student(2030331245049,"2nd",9.76,"Sheetal Wanghare","Mechanical","14/02/2002")
s3=student(2130331267051,"2nd",8.50,"Ankit More","Computer","09/07/2001")
s4=student(2030331267016,"2nd",9.20,"Avanti Parte","Mechanical","13/02/2002")
help()
while(True):

    key = int(input("Enter Key To perform operations from Menu : "))
    if key==1:
        # Display the data.
        print("Lab Assistant Data : ")
        l1.display()
        print()
        l2.display()
        print()
        l3.display()
        print(
        "-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Faculty  Data : ")
        f1.display()
        print()
        f2.display()
        print()
        f3.display()
        print()
        print(
        "-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Student  Data : ")
        s1.display()
        print()
        s2.display()
        print()
        s3.display()
        print()
    elif key ==2:
        print('''Enter key to delete data :
        1) Lab Assistant OR Faculty
        2) Student
        ''')
        del_val = int(input("key: "))
        if del_val == 1:
            k = int(input("Enter Employee ID : "))
            if l1.emp_id == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l1.name))
                del l1
                print("Remaining Lab Assistant Data :")
                l2.display()
                print()
                l3.display()
            elif l2.emp_id == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l2.name))
                del l2
                print("Remaining Lab Assistant Data :")
                l1.display()
                print()
                l3.display()

            elif l3.emp_id == k:
                print("Data of Lab Assistant {0} is Deleted!".format(l3.name))
                del l3
                print("Remaining Lab Assistant Data :")
                l1.display()
                print()
                l2.display()

            elif f1.emp_id == k:
                print("Data of Faculty {0} is Deleted!".format(l2.name))
                del f1
                print("Remaining Faculty Data :")
                f2.display()
                print()
                f3.display()
            elif f2.emp_id == k:
                print("Data of Faculty {0} is Deleted!".format(l2.name))
                del f2
                print("Remaining Faculty Data :")
                f1.display()
                print()
                f3.display()
            elif f3.emp_id == k:
                print("Data of Faculty {0} is Deleted!".format(l2.name))
                del f3
                print("Remaining Faculty Data :")
                f1.display()
                print()
                f2.display()
            else:
                print("Employee data Not Found!!")
        elif del_val == 2:
            k = int(input("Enter PRN of Student : "))
            if s1.prn == k:
                print("Data of student {0} is Deleted!".format(l1.name))
                del s1
                print("Remaining Students Data :")
                s2.display()
                print()
                s3.display()
            elif s2.prn == k:
                print("Data of student {0} is Deleted!".format(l1.name))
                del s2
                print("Remaining Students Data :")
                s1.display()
                print()
                s3.display()
            elif s3.prn == k:
                print("Data of student {0} is Deleted!".format(l1.name))
                del s3
                print("Remaining Students Data :")
                s1.display()
                print()
                s2.display()
            else:
                print("Student data not found!!")
    elif key == 3:
        print("Total Salary of Lab Assistants : ", lab_assistant.lab_salary)
        print("Total Salary of Faculty : ", faculty.faculty_salary)
        total = lab_assistant.lab_salary + faculty.faculty_salary
        print("Total Salary of all Employess : ",total)
        print()
    elif key == 4:
        comp_cgpa = student.comp /2
        mechanical_cgpa = student.mechanical/2
        print("Average CGPA of COMPUTER Department :: ", comp_cgpa)
        print("Average CGPA of MECHANICAL Department :: ", mechanical_cgpa)
        print()
    elif key ==5:
        exit()
    else:
        print("Enter Correct Key Input !!")



