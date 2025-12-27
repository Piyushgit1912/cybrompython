# abstraction
#     abstractclass 
#     abstract method
#     concrete method 

# from abc, import ABC, abstract method 
# class a (ABC):
# abstract base class 
# minimum 1 abstract method hon chahiye 
# 1 concrete method ho sakta hai 
# @abstractmethod 
# from abc import ABC ,abstractmethod

# class base(ABC):
#     def dashboard(self):
#         print('welcome here ')

#     @abstractmethod
#     def login(self):
#       print('this is abstract method ')

# class b (base):
#   def login(self):
#         print('login successful')
#         # pass
  

# obj=b()
# obj.dashboard()
# obj.login()




# encapsulation

#     access specifier/ modifier
#     public variable /method   
#     protected
#     private variable /method

# public variable access specifier 

class a:
    x=10
    def show(self):
        print('this is parent clss a')

class b (a):
    pass

obj=b()
print(obj.x)
obj.show()
# print(a.x)
print(a.show(10))

# protected variable access specifier 
# # not supported by python 
# bcoz it should not be accessible outside the class 
# class a:
#     _x=10
#     def show(self):
#         print('this is parent clss a')

# class b (a):
#     pass

# obj=b()
# print(obj._x)
# obj.show()
# # print(a.x)
# print(a.show(10))
# 10
# this is parent clss a
# this is parent clss a
# None

# private accessifier /variable
# it is only accessibl within the class 

# class a:
#     __x=10
#     def __show(self):
#         print('this is parent clss a')

# class b (a):
#     pass

# obj=b()
# # print(obj.__x)
# obj.__show()
# through the object or can say within the class 
# print(a.x)
# print(a.show(10))
# through the class or can be say outside the class 

# print(dir(a))
# _a__show', '_a__x'
# namemangling

# print(a._a__x)

# hence the private object is accesed outside the clss through the name mangling so it it can be say that the private accessifier is not supported by python 
#  __classname__variable/method 
