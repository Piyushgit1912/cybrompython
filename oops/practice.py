# # class student:
# #     name='karan'
# # s1=student()
# # print(student.name)

# class student:
#     grade='10th'
#     def __init__(self):
#         print('default constructor')
#     def __init__(self,name):
#         self.n=name
#         print('consructor called adding object...')
#     def update(self,fees):
#         self.fees=fees
       
# s1=student('rahul')
# s1.update(10000)
# print(s1.n, s1.grade ,s1.fees)
# class student:
#     def __init__(self, name,m1,m2,m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
# def avg(self):
#      return ((self.m1+self.m2+self.m3)/3)
# s1=student('piyush',80,90,70)
# s2=student('karan',85,95,80)
# s3=student('rahul',75,65,55)
# avg(s3)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avg(self):
#         sum =0
#         for i in self.marks:
#             sum = sum+i
#         print(f' hii {self.name} your avg score is',sum/len(self.marks))
# s1=student('piyush',[80,20,1000])
# s2=student('naveen',[300,100,2,2.555,99])
# s2.avg()

import math 
from turtle import *
# speed(2)
# for i in range(10):
#     forward(200)
#     right(100) 
# done()
def hearta(k):
    return 12 *math.cos(k) -5 * math.cos(2*k) -2*math.cos(3*k) -math.cos(4*k)

 
