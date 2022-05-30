""" Illustrates what classes are for
Using the Employee class and two derived classes
and the Employees class which contains a dictionary
of Employee class instances"""

# class representing public speakers
class Speaker():
    def inviteTalk(self):
        pass
    def giveTalk(self):
        pass


class Employee():
    def __init__(self, frname, lname, salary):
        self.idnum = 0          # place holder
        self.frname = frname    # save name
        self.lname = lname
        self._salary = salary   # and salary
        self.benefits = 1000    # and benefits

    @property
    def salary(self):           # get the salary
        return self._salary

    def setSalary(self, val):   # store the salary
        self._salary = val

class PublicEmployee(Employee, Speaker):
    def __init__(self, frname, lname, salary):
        super().__init__(frname, lname, salary)


# Contains a dictionary of Employees, keyd by ID number
class Employees:
    def __init__(self):
        self.empDict = {}
        self.index=101
    def addEmployee(self, emp):
        emp.idnum = self.index
        self.index += 1
        self.empDict.update({emp.idnum: emp})
    def find(self, idnum):
        return self.empDict.get(idnum)

# Temp employees get no benefits
class TempEmployee(Employee):
    def __init__(self, frname, lname, salary):
        super().__init__(frname, lname, salary)
        self.benefits=0

# Interns get no benefits and smaller salary
# What sadist designed this system?
class Intern(TempEmployee):
    def __init__(self, frname, lname, sal):
        super().__init__(frname, lname, sal)
        self.setSalary(sal) # cap salary

    # limit intern salary
    def setSalary(self, val):
        self._salary = min(val, 500)


# This creates a small group of Employees
class HR():
    def __init__(self):
        self.empdata = Employees()
        self.empdata.addEmployee(Employee('Sarah', 'Smythe',2000))
        self.empdata.addEmployee(PublicEmployee('Fran', 'Alien',3000))
        self.empdata.addEmployee(TempEmployee('Billy', 'Bob', 1000))
        self.empdata.addEmployee((Intern('Arnold', 'Stang', 800)))

    def listEmployees(self):
        dict = self.empdata.empDict
        for key in dict:
            empl= dict[key]
            print (empl.frname, empl.lname, empl.salary)

def main():
   hr = HR()
   hr.listEmployees()


if __name__ == '__main__':
    main()


