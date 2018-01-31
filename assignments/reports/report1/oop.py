#1- super can use to define the parent you need to call even if you inherit from parent
#only and parent inherit from top parent you can use child to call top parent

class Human:
    name="marwa"
    makeFault=0
    def __init__(self,name):# constructor  definition
        self.name=name
        print("i am",name)

    def speak(self):
        print("my name is",self.name)    
    @classmethod 
    def fault(cls):
        cls.makeFault+=1
        print(cls.makeFault)
    @staticmethod
    def measuretmp(temp):
        if(temp ==37):
            return 'normal'
        return 'not normal'

class Employee(Human):
    def __init__(self,name,salary):
        print("child \n")
        super(Employee,self).__init__(name)
        self.salary=salary
    def work(self):
        print("welcome")

class Employee2(Employee):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)
        print("child2 \n")
        self.salary=salary
    def work(self):
        print("njggfgfghjk") 
#emp=Employee("marwa",500)
emp2=Employee2("marwa",500)
#emp.speak()
#emp.work()               
# Human.fault() 
# print("----------------------") 
# print(Human.measuretmp(38))
# print("----------------------") 
# man=Human("Ahmed") 
# mostafa=Human("mostafa")
# man.speak()
# print(man.measuretmp(37))
# print("----------------------") 
# print('man1 :',man.makeFault) 
# print('man2 :',mostafa.makeFault)
# print('Human',Human.makeFault) 


# mostafa.makeFault=2
# print('man2 :',mostafa.makeFault)
# print('Human',Human.makeFault)
# print('man1 :',man.makeFault) 

