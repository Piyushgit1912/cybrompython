# abstraction
#     abstract class 
#     abstract method
#     concrete method 

# encapsulation
#     access specifier/ modifier
#     public variable /method
#     protected 
#     private variable /method
# -
# inheritance
#     types
#     single 
#      parent to child

# multi level inheritance
    # grand parent to parent to child

#     multiple 
# parent1 and parent 2 to child



#     method overriding 
#     M.R.O. (method resolution order )
#     super()

# polymorphism
#     typess
#         compile time  xxxx
#         run time
#     overload

#inheritence

        # single level inheritancwe
# class parent:
#     x=10
#     def home(self):
#         print('from parent class')
# class child(parent):
#     def home(self):
#         print('from child class')
        
# obj=child()
# # print(obj.x)
# obj.home()

# class parent:
#     x=10
#     def home(self):
#         print('from parent class')
# class child(parent):
#     def home(self):
#         print('from child class')
#         super().home()
# super() method ki help dse child class me parent class ki method ko call kar sakte h agar method ka nam same ho aur inheritence use hua ho is scenerio ko method overriding kahteh h 

# obj=child()
# # print(obj.x)
# obj.home()

# PS C:\Users\hp\Desktop\oops> py pillars.py
# from child class
# from parent class
# PS C:\Users\hp\Desktop\oops> 

# class grandparent :
#     def home(self):
#         print('from grand parent class')

# class parent(grandparent):
#     x=10
#     def home(self):
#         print('from parent class')
#         super().home()
# class child(parent):
#     def home(self):
#         print('from child class')
#         super().home()
# obj=child()
# # print(obj.x)
# obj.home()

# ers\hp\Desktop\oops> py pillars.py
# from child class
# from parent class
# from grand parent class

# multiple inheritence 

# class grandparent :
#     def home(self):
#         print('from grand parent class')

# class parent(grandparent):
#     x=10
#     def home(self):
#         print('from parent class')
#         super().home()
# class child(parent):
#     def home(self):
#         print('from child class')
#         super().home()

# obj=child()
# # print(obj.x)
# obj.home()
# class father:
#     def home(self):
#         print('this is fathers class')
   

# class mother:
#     def home(self):
#         print('this is mothers class')

# class child(father,mother):
#     def home(self):
#         print('this is child class')
#         super().home()

# # mro( method resolution order) ye batata h ki agar multiple inheritence me same method name h to konsa method pehle call hoga
# obj=child()
# obj.home()
# PS C:\Users\hp\Desktop\oops> py pillars.py
# this is child class
# this is fathers class

# class father:
#     def home(self):
#         print('this is fathers class')
#         # mother().home()
#         mother.home(self)

# class mother:
#     def home(self):
#         print('this is mothers class')

# class child(father,mother):
#     def home(self):
#         print('this is child class')
#         super().home()
        

# # mro( method resolution order) ye batata h ki agar multiple inheritence me same method name h to konsa method pehle call hoga
# obj=child()
# obj.home()

# PS C:\Users\hp\Desktop\oops> py pillars.py
# this is child class
# this is fathers class
# this is mothers class


# hybrid inheritence
# one parent multiple child 

# class a :
#     def home(self):
#         print ('this is parent ckass a')

# class b(a):
#     def home (self):
#         print('this is child class b')
#         super().home()
#         c().home()

# class c(a):
#     def home (self):
#         print('this is child class c')
#         super().home()

# class d (b,c):
#     pass

# obj=d()
# obj.home()

# PS C:\Users\hp\Desktop\oops> py pillars.py
# this is child class b
# this is child class c
# this is parent ckass a
# this is child class c
# this is parent ckass a
# PS C:\Users\hp\Desktop\oops> 


