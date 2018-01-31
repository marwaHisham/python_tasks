class Human:
    def __init__(self):
        print("constructor_one")

    def eat(self):
        print("human");

    # def eat(self,i):
    #     print("human2",i);    
    pass       

class Mammal:
    def __init__(self):
        print("constructor_two")

    def eat(self):
        print("Mammal");
    pass       
#first case :output
# constructor_one
#constructor_two
# Mammal
class Emp(Mammal,Human) :
    def __init__(self):
        Human.__init__(self)
        Mammal.__init__(self)
    pass   

#second case :output 
#  constructor_one
#constructor_two
# Human
# class Emp(Human,Mammal) :
#     def __init__(self):
#         Human.__init__(self)
#         Mammal.__init__(self)

    #if  methods have the same name it will return first left class
    pass 

e=Emp();
e.eat()


