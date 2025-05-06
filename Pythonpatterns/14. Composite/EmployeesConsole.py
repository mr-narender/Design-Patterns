""" Program to create a Boss -- Employee tree fpr a small company
And print it out """

from random import *

#compute salaries under selected employee
class SalarySpan():
    def __init__(self, boss, name):
        self.boss = boss
        self.name = name
    # print sum of salaries for employee and subordinates
    def print(self):
        #search for match
        if self.name == self.boss.name:
            print(self.name, self.boss.name)
            newEmp = self.boss
        else:
            newEmp = self.boss.getChild(self.name)
        sum = newEmp.getSalaries()      # sum the salaries
        print(f'Salary span for {self.name}', sum)

# Employee is the base class
class Employee():
    def __init__(self, name, salary:int):
        self.name = name
        self.salary = salary
        self.isleaf = True

    def getSalaries(self):
        return self.salary

    def getSubordinates(self):
        return None


# Boss is derived from Employee. Only Bosses can have subordinates
class Boss(Employee):
    def __init__(self, name, salary:int):
        super().__init__(name, salary)
        self.subordinates = []
        self.isleaf = False

    def getSubordinates(self)->list[Employee]:
        return self.subordinates

    def add(self, e:Employee):
        self.subordinates.append(e)

    # called recursively as it walks down the tree
    def getSalaries(self):
        self.sum = self.salary
        for e in self.subordinates:
            self.sum = self.sum + e.getSalaries()
        return self.sum

    # Create the tree for the Employee structure
    def makeTree(self):
        self.indent=0
        print(self.name, self.salary)
        self.addNodes( self)

# print employee tree recursively, walking down the tree
    def addNodes(self,  emp:Employee ):
        if not emp.isleaf:      #Bosses are not Leaves
            empList = emp.getSubordinates()
            if empList != None: # must be a Boss
               for newEmp in empList:
                    print(" "*self.indent, newEmp.name, newEmp.salary)
                    self.indent += 2
                    self.addNodes( newEmp)
                    self.indent-=2

    #finds child node with matching name
    def getChild(self, name:str):
        if self.name == name:
            return self
        found = False
        index = 0
        newEmp = None
        while not found and index < len(self.subordinates):
            newEmp = self.subordinates[index]
            found = newEmp.name.lower() == name.lower()

            if not found:
                newEmp = None if newEmp.isleaf else newEmp.getChild(name)
            found = newEmp != None
            index += 1

        return newEmp if found else None

# Creates the employee tree structure
# salaries are generated partly using random numbers
class Builder():

    #builds the employee tree
    def build(self):
        seed(None, 2)       #initiialize random seed
        self.boss = Boss("CEO", 200000)
    # add VPs under Boss
        marketVP = Boss("Marketing_VP", 100000)
        self.boss.add(marketVP)
        prodVP = Boss("Production_VP", 100000)
        self.boss.add(prodVP)
        salesMgr = Boss("Sales_Mgr", 50000)
        marketVP.add(salesMgr)
        advMgr = Boss("Advt_Mgr", 50000)
        marketVP.add(advMgr)
        # add salesmen reporting to Sales Mgr
        for i in range(6):
            salesMgr.add(Employee(f"Sales_{str(i)}", int(30000.0 + random() * 10000)))
        advMgr.add(Employee("Secy", 20000))
        prodMgr = Boss("Prod_Mgr", 40000)
        prodVP.add(prodMgr)
        shipMgr = Boss("Ship_Mgr", 35000)
        prodVP.add(shipMgr)

        # Add manufacturing and shipping employees
        for i in range(4):
            prodMgr.add(Employee(f"Manuf_{str(i)}", int(25000 + random() * 5000)))
        for i in range(4):
            shipMgr.add(Employee(f"Ship_Clrk_{str(i)}", int(20000 + random() * 5000)))

        self.buildTree(self.boss)
        #print(self.boss.getSalaries())

    #creates the tree
    def buildTree(self, boss):
        boss.makeTree()
        ename=''
        while ename != 'q':
            ename = input('Enter employee name for salary span (q for quit): ')
            if ename != 'q':
                span = SalarySpan(self.boss, ename)
                span.print()
# --program starts here---
def main():
    bui = Builder()
    bui.build()

###  Here we go  ####
if __name__ == "__main__":
    main()
