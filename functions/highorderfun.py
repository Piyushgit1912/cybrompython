#high order functions

# map() syntax
# only map() accepts multiple iterable 

# iterable 1,iterable 2, iterable 3

# def fun_name(parameter1,2,3):
#     code for function

# res= map(fun_name, iterable1,2,3)
# print(list(res))

# l1= [1,2,3,4]
# l2=[5,6,7,4]
# l3=[11,22,33,44]

# def add(x,y,z):
#     return x+y+z
# res=map(add, l1,l2,l3)
# print(res)
# # print(tuple(res))
# print(list(res))

# l1= [1,2,3,4]
# # l2=[5,6,7,4]
# # l3=[11,22,33,44]

# def squar(n):
#     return n**2
# res=map(squar,l1)
# print(res)
# # print(tuple(res))
# print(list(res))

# l1= [1,2,3,4]
# # l2=[5,6,7,4]
# # l3=[11,22,33,44]

# def sqroot(n):
#     return n**.5
# res=map(sqroot,l1)
# print(res)
# # print(tuple(res))
# print(list(res))

# filter()

# iterable
# def fun_name(parameter):
#     Code 
#     return
# res= filter(fun_name,iterable)
# print(list(res))

# l=[1,2,3,4]
# def even(n):
   
#     return  n%2!=0, n%2==0
    

    
    
# res=filter(even,l)
# print(res)
# print(list(res))


# reduce()
# syntax:-
# iterable
# def fun_name():
#     Code 
#     return
# res=reduce((fuun_name, iterable, initial value(optional value)))
# print(res)

# import functools
# l1=[1,2,3,4,5]
# def sum(x,y):
#     return x+y
# res=functools.reduce(sum, l1)
# print(res)

# from functools import reduce
# l1=[-111,-111,-111,-111,00,-111]
# def maximum(x,y):
#     if x>y:
#         return x
#     else :
#         return y
# res=reduce(max,l1)
# print(res)

# 
# from functools import reduce
# l1=[5,2,3,4]
# def sum_max(x,y):
#     return x+(y*y)
# res=reduce(sum_max,l1,0)
# print(res)

# from functools import reduce
# l1=[5,2,3,4]
# def factorial(x,y):
#     fact=1
#     for i in range (1,y+1):
#         fact= fact*i
#     return x+fact
# res=reduce(factorial,l1,0)
# print(res)

