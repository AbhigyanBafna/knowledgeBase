'''
Q1) Overload comparision operators for comparing vectors.
'''

import math
ans = True

class vectors:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v = [0 , 0]
        self.mod = 0

    def set_v(self):
        self.x = int(input("Enter X Coordinate: "))
        self.y = int(input("Enter Y Coordinate: "))
        self.v = [self.x, self. y]

    def get_v(self):
        print(f" {self.x}i + {self.y}j")
        
    def magnitude(self):
        self.mod = math.sqrt(sum(i**2 for i in self.v))
        print( math.sqrt(sum(i**2 for i in self.v)) )
        
    def __lt__(self, v2):
        if(self.mod < v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __gt__(self, v2):
        if(self.mod > v2.mod):
            print(ans)
        else:
            print(not ans)
    
    def __le__(self, v2):
        if(self.mod <= v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __ge__(self, v2):
        if(self.mod >= v2.mod):
            print(ans)
        else:
            print(not ans)
            
    def __eq__(self, v2):
        if(self.mod == v2.mod):
            print(ans)
        else:
            print(not ans)

v1 = vectors()
v1.set_v()
v1.get_v()
v1.magnitude()
v2 = vectors()
v2.set_v()
v2.get_v()
v2.magnitude()
v1 < v2
v1 > v2
v1 <= v2
v1 >= v2
v1 == v2

'''
Q2) Create an interface which includes calculate and update as two methods.
    a) Customer class can use calculate to calculate interest on their balance. Saving = 4, Current = 6
        and the update method will give them a 5% bonus if their balance is more than 1 lakh.
    b) Employee class can use calculate to calculate their gross salary based on their class (Class1, Class2).
    Class 1
    Basic Salary = 30k
    DA = 121% Basic Salary
    Class 2
    Basic Salary = 20k
    DA = 115% Basic Salary
    
    HRA for both = 30% Basic Salary. and the update method adds 20% bonus but only if they have been working
    for more than 15 years.
'''

from abc import ABC, abstractmethod
 
class banking(ABC):
    
    @abstractmethod
    def calculate():
        pass
     
    @abstractmethod
    def update():
        pass
   
class customer(banking):
    def __init__(self, acctype, bal):
        self.acc = acctype 
        self.bal = bal
        self.irate = 0
        
        if(self.acc == "saving"):
            self.irate = 4/100
        elif(self.acc == "current"):
            self.irate = 6/100
        else:
            print("Undefined acc type")
    
    def calculate(self):
        self.interest = self.bal*self.irate
        print(f"Current Interest : {self.interest}")
        
    def update(self):
        if(self.bal > 100000):
            self.bal += self.bal*5/100
            print(f"Your Updated Balance is : {self.bal}")
        else:
            print("Acc balance too low")
            

class employee(banking):
    def __init__(self, emptype, wtime):
        self.emptype = emptype
        self.wtime = wtime
        self.gsal = 0
        self.bsal = 0
        
        if(self.emptype == "class1"):
            self.bsal = 30000
            self.da = self.bsal*121/100
        elif(self.emptype == "class2"):
            self.bsal = 20000
            self.da = self.bsal*115/100
        else:
            print("Undefined employee type")
    
        self.hra = self.bsal*30/100    
    
    def calculate(self):
        self.gsal = self.bsal + self.da + self.hra
        print(f"Your Gross salary is : {self.gsal}")
        
    def update(self):
        if(self.wtime > 15):
            self.gsal += self.gsal*20/100
            print(f"Your Salary with Bonus is : {self.gsal}")
        else:
            print("You have worked too less")
        
c1 = customer("saving", 1000)
c2 = customer("current", 1000000000)
e1 = employee("class1", 10)
e2 = employee("class2", 20)

c1.calculate()
c2.calculate()
e1.calculate()
e2.calculate()

c1.update()
c2.update()
e1.update()
e2.update()
    
