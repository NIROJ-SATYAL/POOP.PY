
class dog:
    def __init__(self,name,age):
        self.a=name
        self.b=age

    def bark(self):
        print("bark bark!")

    def doginfo1(self):
        print(ozzy.a+ " is " + str(ozzy.b) + " years old")
    def doginfo2(self):
        print(skippy.a+ " is " + str(skippy.b) + " years old")

    def doginfo3(self):
        print(filou.a+ " is " + str(filou.b) + " years old")

ozzy=dog("ozzy",2)
skippy=dog("skippy",12)
filou=dog("filou",8)
while True:
    #d=None
    #dogtype=["ozzy","skippy","filou"]
    #while d not in dogtype:
    dogname=input("enter the dog name(ozzy,skippy or filou):  ").lower()
    if dogname=="ozzy":
        ozzy.doginfo1()
        ozzy.bark()
    elif dogname=="skippy":
        skippy.doginfo2()
        skippy.bark()
    elif dogname=="filou":
            filou.doginfo3()
            filou.bark()
    else:
        print("sorry..This dog in not available in here:::::::::updated version comming soon!!!!")
    
    c=None
    list=["yes","no"] 
    while c not in list:  
        c=input("do you want to continue:(yes or no)").lower()
    if c!="yes":
        break



   
