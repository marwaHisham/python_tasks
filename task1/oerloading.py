# There is no method overloading in python. You can however use default arguments,
class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
 
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')