class Employee():
    def __init__(self,first,last):
        self.firstname = first
        self.lastname  = last
 #getter
    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
#setter
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.firstname = first
        self.lastname = last
#deleter
    @fullname.deleter
    def fullname(self):
        print("name deleted!")
        self.firstname = None
        self.lastname = None

emp = Employee("Anbeel","Muhmd") 
print(emp.fullname)
""" emp.fullname = "cory chase"
print(emp.fullname)
del emp.fullname
print(emp.fullname) """
emp_1  = Employee("Nabeel","Muhmd")
print(emp_1.fullname)
emp_1.fullname = emp.fullname
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)