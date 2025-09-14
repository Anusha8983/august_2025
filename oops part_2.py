#Inheritance 
class mobilephone():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def Make_call(self,number=88888):
        print(f"calling  {number} from {self.brand} {self.model}")
    def send_message(self,message="Hello",number=9999): 
        print(f"sending {message} from {number}")
#Object_name=classname
Apple=mobilephone("Apple","16promax")
Apple.Make_call(5555)
Apple.send_message("Good morning, have a nice day,6666")
Apple.Make_call()
Apple.send_message()

class smartphone(mobilephone): #inherit from mobile phone
    def browsing(self):
        print(f"you are browsing from {self.brand}")
    def app(self,appname):
        print(f"using{appname}app on {self.brand}")
Apple=smartphone("Apple","16promax")
Apple.browsing()
Apple.app("instagram")
Apple.Make_call(1234)
Apple.send_message("Good evening",6789)

#hierarchiel Inheritence 
class a():
    def parent(self):
        print("this is parent class")  
class b(a):
    def child1(self):
        print("this id child 1 class")
class c(a):
    def child2(self):
        print("this is child 2 class")
#object is for both child
Anusha=b()
Anusha.parent()
Anusha.child1()

Anusha=c()
Anusha.parent()
Anusha.child2()

Anusha=a()
Anusha.parent()

#Multiple inheritance
class parent1():
    def father(self):
        print("This is father class")
class parent2():
    def mother(self):
        print("This is mother class")
class child(parent1,parent2):
    def daughter(self):
        print("This is child 2 class")
obj=child()
obj.father()
obj.daughter()
obj.mother()

#Multilevel
class grandfather():
    def Thatha(self):
        print("earned 100cr properties")
class father(grandfather):
    def Nanna(self):
        print(f"This is father class")
class child (father):
    def daughter(self):
        print(f"this is child class")
obj=child() #Object is for last derived
obj.Thatha()
obj.Nanna()
obj.daughter()

#Polymorphism ....
#1 operator overloading,2 method oveloading is not suport in python
#Example
class calculator():#operator overloading
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
obj=calculator()
obj.add(100,200)
obj.add(10,20,30)

#method overloading
class calculator():#method name is same arguments are different
    def add(self,a=None,b=None,c=None):
        print(a,b,c)
obj=calculator()
obj.add(10,20,30)
obj.add("anu","manu","chinnu")
obj.add("anu","manu")
obj.add("anu")
obj.add()

#method overriding
class grandfather():
    def details(self,a):
        print("this is grandfather class",a)
class father(grandfather):
    def details(self,a):
        print("this is father class",a)#output is father details because of overriding
        super().details
obj=grandfather()
obj.details("100cr")
#super is used to acess base methods
#without super we will take object for father and output is father details
