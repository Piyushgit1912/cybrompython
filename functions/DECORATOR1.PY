# kiis bhi func k response ko change krne k liye decorator ka use karte hai
# @ represent krta hai decorator fun ko 
# decoration ek special type ka  higher oreder fun hai jo argu me fun lega aur return me bhi ek function hi dega 
# def decore(fun_name)
def decore(fun):
    def inner():
        print('hello')
    return inner 
x=decore(10)
# print(x)
# print(decore)
x()
# def add():
#     print('hello')
# def decore (fun):
#     def inner():
#         fun()
#     return inner
# res= decore(add)
# res()


# def decore (fun):
#     def inner(p,q):
#         p=p+5
#         q=q*2
#         fun(p,q)
#     return inner
# @ decore
# def  add (x,y):
#     print(x+y)
# # res = decore(add)
# # res(10,20)
# add(20,20)

# def first(fun):
#     def inner():
#         print('welcome')
#     return inner
# @first
# def greet():
#     print('hello')
# greet()

# n=int(input('print the number:'))
# def decore(fun):
#     def inner(x):
#         for i in range(1,x+1):
#             print(2*i-1)
#     return inner

# @decore
# def even(n):
#     for i in range(1,n+1):
#         print(2*i)

# x=even(n)
# # print(x)




