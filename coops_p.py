#compossition
# 
# class Jocker:
    # def info (self,name,age):
        # self.name=name
        # self.age=age
    # def get_info(self):
        # print(self.name, self.age)
# class Circus:
    # def __init__(self,loc):
        # self.loc=loc
        # x=Jocker()
        # x.info("raju",32)
        # x.get_info()
    # def display_info(self):
        # print(self.loc)
# 
# c=Circus("Pune")
# c.display_info()

#single level inheritance with super and method and constructor chanining
 
# class Test:
    # def __init__(self,name,id):
        # self.name=name
        # self.id=id
    # def display(self):
        # print(self.name,self.id)
# class Test2(Test):
    # def __init__(self, age,grnder):
        # super().__init__(name="saurabh",id=100)
        # self.age=age
        # self.gender=grnder
    # def display(self):
        #  super().display()
        #  print(self.age,self.gender)
# t=Test2(21,"male")
# t.display()

# multilevel inheritance -


# class University:
    # def __init__(self,usn):
        # self.usn=usn
    # def display(self):
        # print(self.usn)
# class College(University):
    # def __init__(self,college_name):
        # super().__init__(usn="33546")
        # self.college_name=college_name
    # def display(self):
        #  super().display()
        #  print(self.college_name)
# class Student(College):
    # def __init__(self, student_name):
        # super().__init__(college_name="dy patil akurdi")
        # self.student_name=student_name
    # def display(self):
        #  super().display()
        #  print(self.student_name)
# s=Student("saurabh")
# s.display()    


#multiple 
# 
# class Paresnt1:
    # def __init__(self,property,villa):
        # self.property=property
        # self.villa=villa
        # super().__init__("gold","clothes")
# 
    # def dad(self):
        # print(self.property,self.villa)
# 
# class Parent2:
    # def __init__(self,gold,clothes):
# 
        # self.gold=gold
        # self.clothes=clothes
# 
    # def mom(self):
        # print(self.clothes,self.gold)
# 
# class Child(Paresnt1,Parent2):
    #    def __init__(self,name):
            # self.name=name
            # super().__init__("property","villa")
# 
    #    def money(self):
                #   print(self.name)
                
# 
            #  
# c=Child(1000)
# c.money()
# c.mom()
# c.dad()

