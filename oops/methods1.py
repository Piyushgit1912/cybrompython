# methods in python
#  instance methods  self ki jagah cls parameter use krte  h 
# aesi methods jiska pahla parameter self hota h 
# #  class methods       @classmethod decorator use krte h
# class student:
#     grade = '10th'
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#     @classmethod
#     def update(cls,new):
#         cls.grade=new
# obj1=student('piyush',106)
# print(student.grade)
# obj1.update('11th') to update 
# print(student.grade)
m
# class student:
#     grade = '10th'
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#     @classmethod
#     def update(cls,new):
#         cls.grade=new
#     @classmethod
#     def add_new(cls,add):
#         cls.code=add
    
# obj1=student('piyush',106)
# # print(student.grade)
# obj1.update('11th')
# # print(student.grade)
# obj1.add_new('0127')
# print(obj1.code,obj1.n,obj1.r,obj1.grade)

# # static methods      @staticmethod decorator use krte h
# cls, self pass nahi hote 
# class k kisi bi variablw se releationn  nahi karta 
# class student:
#     def __init__(self, roll):
#         self.n=roll
#     @staticmethod           #
#     def greet(name):
#         print(f'welcome {name} in my page')
# obj=student()
# x=obj.n
# obj.greet(x)
# print(obj.n)