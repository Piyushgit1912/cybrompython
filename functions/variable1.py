# def display():
    
#     x=10
#     print(x)
# display()
# print(x)      x is  local variable only accesible in the block of function

# Traceback (most recent call last):
#   File "C:\Users\hp\Desktop\python cybrom vsc\functions\variable1.py", line 5, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined

# def display():
#     global x   global variable banane ke liye global kword use krte h jisse sab kahi work karega 
#     x=10
#     print(x)
# display()
# print(x)
# \functions> py variable1.py
# 10
# 10

# def display():
#     global x local to global variable 
#     x=10
#     # print(x)
# display()
# print(x)
# print(x)    this line will make error because x will not be a global variable untill the function display executes
# display()
# print(x)   
# Traceback (most recent call last):
#   File "C:\Users\hp\Desktop\python cybrom vsc\functions\variable1.py", line 28, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined.


# global variable

# x=10
# def show():
#     x=20
#     print(x)
# print(x)
# show()
# print(x)
#  py variable1.py
# 10
# 20
# 10

# x=10
# def show():
#     print(x)    will creat an error bcoz the global and local variavble x has the same name ,, will create a conflict
#     x=20
#     print(x)
# # print(x)
# show()
# print(x)


# x=10
# def show():
#     x=20
#     print(x)
# print(x)
# show()
# py variable1.py
# 10
# 20


# x=10
# def show():
#     x=20
#     print(globals()['x']) to use x as global variable in a local function
# print(x)
# show()
#  py variable1.py
# 10
# 10

# def show():
#     x=10
#     def display():    
    
#         print(x)
#     display()
# show()

# o/p>- 10

# NON-LOCAL

# def show():
#     x=10
#     def display():
#         nonlocal x
#         x=x+5
#         print(x)
#     display()
# show()
# # o/p>- 15

# while(True):
#     # print('hellooooo.....')

#     print(" 1. add\n 2. sub\n 3. div \n 4. multiplication \n 5. exit")
#     n=int(input("enter any button--:"))
#     if n in (1,2,3,4,5):  

#         if n in (1,2,3,4):

#             if n==1:
#                 num=int(input("enter the number of variables for addition")) 
#                 l=[]

#                 for i in range(1,num +1):
#                     value=eval(input(f'enter {i} number:-'))
#                     l.append(value)
#                 sum=0
#                 for i in l:
#                     sum=sum+i
#                 print(sum)
            
#             if n==2:
#                 num=int(input("enter the number of variables for subtraction-:")) 
#                 l=[]

#                 for i in range(1,num +1):
#                     value=eval(input(f'enter {i} number:-'))
#                     l.append(value)
                


#         else:
#             break  
        
#     else:
#         print('enter valid choice')
    
# #  1. add
# #  2. sub
# #  3. div
# #  4. multiplication
# #  5. exit
# # enter any button--:5