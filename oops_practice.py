#syntax
#class classname():
#attributes
#method
#method syntax....   .methodname(arguements)
# syntax for object...objectname=classname

#Example_1
class person_details():
    user_name="anusha" #Attributes
    roll_nmb=639#attributes
    height="tall"
    def details(self):#methods:
        print(f"studying in siddhartha school",self.user_name)
    def details_2(self):#methods
        print(f"she is 12 years old", self.roll_nmb)
    def details_3(self):
        print(f"she is very tall and beautiful",self.height)

#objectname=classname()
Manu=person_details()
Manu.details()
Manu.details_2()
Manu.details_3()


Chinnu=person_details()
Chinnu.details()
Chinnu.details_2()
Chinnu.details_3()

class mobile_phone():
    brand_name="oneplus"
    colour="lightgreen"
    storage="128GB"
    def calling(self,bn):
        print(f"you are calling from ....{bn}")
    def message(self,pn):
        print(f"message sent successfully.....{pn}")
    def camera(self):
        print(f"photo captured...intrenal storage{self.storage}")
    def browsing(self):
        print(f"network issue...{self.brand_name}")   
    def pouch(self,clr):
        print(f"pouch colour is ..{clr}")
oneplus=mobile_phone()
oneplus.calling(oneplus)
oneplus.browsing()
oneplus.camera()
oneplus.message(123)
oneplus.pouch("red")

Moto=mobile_phone()
Moto.calling("moto")
Moto.browsing()
Moto.camera()
Moto.message(90876)
Moto.pouch("blue")





    