class Person:
    def __init__(self,name="",money=0,mood="",healthRate=1):
        self.name = name
        self.money = money
        self.mood=mood
        self.healthRate=healthRate

    @property
    def name(self):
        return self.__name
    @property
    def money(self):
        return self.__money
    @property
    def mood(self):
        return self.__mood
    @property
    def healthRate(self):
        return self.__healthRate

    @name.setter
    def name(self,name):
        self.__name = name
    @money.setter
    def money(self,money):
        self.__money = money
    @mood.setter
    def mood(self,mood):
        self.__mood = mood

    @healthRate.setter
    def healthRate(self,healthRate):
        
	if healthRate >=0 and healthRate <=100 :
		self.__healthRate = healthRate
	
	else: 
		self.__healthRate =50

    def slep(self,houers):
        if(houers == 7 ):
            self.__mode = "happy"
        elif houers < 7 :
            self.__mode = "tired"
        elif hours > 7:
            self.__mode = "lazy"


    def eat(self,meals):
        if(meals == 3 ):
            self.__healthRate  = 100
        elif meals == 2 :
            self.__healthRate = 75
        elif meal ==  1:
            self.__healthRate = 50

    def buy(self,items):
	self.__money -= 10 * items

    

  class Empolyee(Person):
    def __init__(self,Eid=0,car="",email="",salary=1000,distanceToWork=10):
        self.Eid = Eid
        self.email = email
        self.salary = salary
        self.distanceToWork=distanceToWork
        self.car = Car("Fiat 128",50)


        @property
        def Eid(self):
            return self.__Eid
        @property
        def car(self):
            return self.__car
        @property
        def email(self):
            return self.__email
        @property
        def salary(self):
            return self.__salary
        @property
        def distanceToWork(self):
            return self.__distanceToWork

        @Eid.setter
        def Eid(self,Eid):
            self.__Eid = Eid

        @car.setter
        def car(self,car):
            self.__car = car

        @email.setter
        def email(self,email):
            self.__email = email

        @salary.setter
        def salary(self,salary):
            if salary > 1000:
		self.__salary = salary 

	    else 
	        self.__salary =1000

        @distanceToWork.setter
        def distanceToWork(self,distanceToWork):
            self.__distanceToWork = distanceToWork

        def work(self,hours):
            if(hours == 8  ):
                self.__mode = "happy"
            elif(hours > 8 ):
                self.__mode = "tired"
            elif(hours < 8 ):
                self.__mode = "lazy"

        def drive(self):
            self.car.run(10,self.__distanceToWork)

        def refuel(self):
            print("Empolyee ", self.__name , "refuel")

        def send_mail(self):
	    print("Empolyee ", self.__name , "send_mail")

class car:
    class Car:

    def __init__(self,name,fuelRate):
        self.name =name
        self.fuelRate = fuelRate
        self.velocity = 0


    def run(self,velocity, distance):
        if self.fuelRate > 0:
            self.fuelRate -= 1;
            self.velocity = velocity
        else:
            self.stop(distance)


    def stop(self,velocity, distance):
	self.velosity=0;
	print("distance".distance);

    	pass



class office:
    def __init__(self,name,empolyees={},late):
        self.name = name
        self.empolyees = empolyees
	self.late=late

    @property
    def name(self):
        return self.__name
    @property
    def empolyees(self):
        return self.__empolyees


    def get_all_employees():
        return self.__empolyees



    def get_employee(id):
        return self.__empolyees[id]

    def hire(empolyee):
        emp=get_employee(id);
	return emp
        pass


    def fire(empolyee):
	emp=get_employee(id);
	return emp
        pass
    def check_lateness (self,status,empId, moveHour):
        
	if status=='late':
		deduct();
	else:
		reward();


    def calculate_lateness(self,argetHour , moveHour, distance, velocity):
        pass

    def deduct():
	late-=10;
        pass

    def reward():
	late+=10;	
    	pass    



