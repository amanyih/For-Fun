class info:
    isrobot ="our employees aren't robot"#class attribute
    def __init__(self,name,age,sex,job):
        #these are instance attribute
        self.name = name
        self.age=age
        self.sex=sex
        self.job=job
    def pri(self):#print a weird thing
        print(f"wow {self.name} is a weird name")
    def codeLang(self,language):
        print(f"{self.name} can code in {language}")
    def re(self):
        return self.age
    def __str__(self):#a method for printing a human readable info not a memory location
        return (f"name:{self.name},age:{self.age},sex:{self.sex},job:{self.job}")
    def __eq__(self,other):#otherwise it will compare memeory location
        return self.name==other.name

    







s1=info("aman",20,"M","SE") #an instance or an object
s2=info("kdf",24,"F","Pilot")
x = s2.re()
print(s1.name,s1.job)
print(s2.sex)
print(x+7)
s2.codeLang("Python")
s1.pri()
print(s1)
print(s1.isrobot,info.isrobot)

