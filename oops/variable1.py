# variable 
# 1 . instance variable 
#      object k sath value change krta h .
#     object depedent 
# 2 . class variable
#     class depedent 
     
# 3 . local variable
#     method k andar define hota h 
#     sirf method k andar hi access hota h .

# instance variable

#  declaration 
# 1, inside class 
#     inside constructor 
#      inside instance method
#       using self keyword
    
# 2.   outside class
#         using object reference variable
    
# calling:-
# 1. inside class 
#     inside constructor
#     inside instance method 
#       using self keyword
# 2. outside class
#         using object reference variable

# kya hum constructor me object bnate samay external constructor ko scap kar sakte h ?
# haan , hum kar sakte h .

# class student:
#     def __init__(self, name, contact):
#         self.n=name
#         self.c=contact                        #declaration inside constructor
#         # print(self.n,self.c)               # calling inside constructor
#     def add_new(self,rollno):                    # declaration inside instance method
#         self.r=rollno                                                   
#     def display(self):                  # calling inside instance method                        
#         print(self.n,self.c,self.r,self.email)                                   
    

# obj1=student('piyush',106)                      # object creation
# obj1.add_new(101)                   # calling instance method
#                                            # calling instance method    
# obj1.email= "upadhyayp108@gmail.com"   
# obj1.display()                      # declaration outside class

# # print(obj1.n,obj1.c,obj1.r,obj1.email)      # calling outside class

# obj2=student('naveen', 12345)
# obj2.display()
# print(obj2.n,obj2.c,obj2.r,obj2.email)

# class variable 
# class variable declaration
# 1. inside class
#     inside constructor
#     inside instance method      
#     inside class method
# 2. outside class
#     using class name
#     using object reference variable

# class variable calling
# 1. inside class
#     inside constructor
#     inside instance method
#     inside class method
# 2. outside class
#     using class name
#     using object reference variable

# class student:
#     school_name='s.h.s.s'          # declaration inside class
#     print(school_name,'calling from class body')
#     def __init__(self,name,rollno):
#         self.n=name
#         self.r=rollno
#         student.school_city='bhopal'    # declaration inside constructor
#         print(self.n,self.r,student.school_name,student.school_city)  # calling inside constructor

#     def add_new(self):
#         student.school_code=101
#         print(student.school_name,student.school_city,student.school_code, student.contact)   # calling inside instance method
#         # declaration inside instance method

# student.contact='1234567890'  # declaration outside class
# obj=student('piyush', 106)
# obj.add_new()
# print(student.school_name)

#  py one.py
# s.h.s.s calling from class body
# piyush 106 s.h.s.s bhopal
# s.h.s.s bhopal 101 1234567890
# s.h.s.s

#local variable 
#  accessible only in a paarticular scope 

# class student:
#     def __init__(self,):
#         x=10
#         print(x)
#     def new(self):
#         y=20
#         z=y+10
        
#         # print(x)
#         print(z)
# obj1=student()
# obj1.new()





    