#Each employee has their own characteristics
from calendar import weekday


class Employee():
    num_of_emps = 0
    raise_amount = 1.4
    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname  = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"
        self.fullname = first +" " + last
        Employee.num_of_emps += 1
    def getFullName(self):
        return self.firstname + " " + self.lastname
    def applyRaise(self):
        self.pay = self.pay*Employee.raise_amount
    
    @classmethod
    def setRaiseAmount(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def fromString(cls,empty_string):
        first,last,pay = empty_string.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_Workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


""" empty_string_1 = "nabeel-m-1000"
emp_3=Employee.fromString(empty_string_1)
#print(Employee.num_of_emps)
emp_1 = Employee('nabeel','m',100)
emp_2 = Employee("lal","b",100)
Employee.setRaiseAmount(1.05)
#print(Employee.raise_amount)
emp_1.applyRaise()
#print(emp_1.pay)
#print(emp_1.num_of_emps)
print(emp_3.__dict__) """

""" import datetime
my_date = datetime.date(2022,6,5)
print(Employee.is_Workday(my_date))
print(emp_1.is_Workday(my_date)) """

class Developer(Employee):
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay)
        self.prog_lang = lang



dev_1 = Developer("nabeel","m",150,"python")

class Manager(Employee):
    def __init__ (self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees
    def add_Employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def delete_Employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def printEmployee(self):
        for emp in self.employees:
            print("___>>>",emp.fullname)
    
emp_1 = Employee('nabeel','m',100)
emp_2 = Employee("lal","b",100)
mgr_1  = Manager("SUE","j",50000,[emp_1,emp_2])
dev_2 = Developer ("lal","b",100,"java")

mgr_1.add_Employee(dev_2)
#mgr_1.printEmployee()
#print(isinstance(mgr_1,Developer))
print(issubclass(Manager,Developer))







#print(emp_1.firstname)
#print(emp_1.getFullName())
#print(Employee.getFullName(emp_1))
#whats happening above is emp_1 (instance) is automatically passed as argument of the method


""" print(emp_1,emp_2)

#Instance variable are data that are unique to each instances
emp_1.first = "Nabeel"
emp_1.emaail = "nabeelm25698@gmail.com"

emp_2.first = "lal"
emp_2.email = "@goggla"

print(emp_1.first,emp_2.email)

#if we create like this (instance variable) it requires a lot of code. We need to
# initialise each time for every instance  so we use class variable 
 """


""" instead of doing this every timewe use a special method __init__ it like a constructor  
we construct instance varialble using this __init__ method. self denotes the instance
"""
