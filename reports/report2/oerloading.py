# There is no method overloading in python. You can however use default arguments,
class Human:
 
    def welcome(self, name=None):
 
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
 

obj = Human()
 
obj.welcome()
 
obj.welcome('marwa')