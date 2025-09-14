#Encapsulation ---->wrapping of methods and attributes together as single unit
#Access Modifiers---> public=Accessible to Outside,protected=Accessablei to derived classes,
#private=Not Accessible to outside class

#public to Protected by using sel._
class grandfather():
    def __init__(self,a):
        self._a=a #protected  only  for base and derived class acccess
        print("This is base class",a)
class father(grandfather):
    def display(self,):
        print(f"This is derived class",self._a)# to acess self._
obj=father("100cr")
obj.display()

#Public to Private by giving self.__
#class grandfather():
    #def __init__(self,a):
        #self.__=a #private only acess to base  
        #print("This is base class",a)
#class father(grandfather):
    #def display(self,):
       #print(f"This is derived class",self.a)# we cannot acess by self.__ derived class wont access
#obj=father("100cr")
#obj.display()

#Abstraction---->hiding unnessesary implimentation and showing the nessessary part
#Abstract  class contain abstract  methods
#Abstract method---> The method which contains only declaration but not the defination is called abstract method
#class without abstract methods called concrete classes
#Objects cannot create for abstract class, create only for concrete class
#To create a abstract class in python use abc module

from abc import ABC,abstractmethod

class mother():
    def output(self):
        print(f"this is mother class")
class father():
    def output(self):
        print(f"this is father class")
class child(father,mother):
    def output(self):
        print(f"this is child class")
        super().output()
        mother.output(self)
obj = child()
obj.output()