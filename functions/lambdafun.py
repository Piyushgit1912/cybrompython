# x=lambda parameters : expression    lambda is a keyword
# x(argument)
# print(x(parameter))
# x=lambda x,y,z :2*x+y+z
# # print(x(1,2,3))
# x=lambda x,y : x if x>y else y
# # lambda x,y: if_result if cdn else  (if_result if cdn else( ))
# print(x(5,10))

# age=int(input('print the age'))
# x= lambda age: 'child' if 0<age<18 else ('adult' if 17<age<59 else ('senior' if 59<age else 'invalid age'))
# print(x(age))

# n=int(input('input number'))
# x=lambda n: 'even' if n%2==0 else None
# print(x(n))
 
# x= lambda n: n**2
# print(x(n))

# natural= lambda n: [i for i in range (1,n+1)]
# print(natural(n))

# x= lambda n : [i for i in range (1, n+1) if i%2==0]
# print(x(n))

# l= [1,2,3,4]
# # print(list(map(lambda l: l**2,l)))
# l2=[2,3,4,5]
# l3=[5,6,7,8]
# print(list(map(lambda x,y,z: x**.5+y**.5+z**.5,l,l2,l3)))

# l=[1,2,3,4,5,6,7]
# print(list(filter(lambda x: x if x%2==0 else None,l )))
import functools

# l=[1,2,3,4,5,6,7]
# print(functools.reduce (lambda x,y: x+y ,l))


# to return greatest nuber 
# l=[1,2,3,4,5,6,7]
# print(functools.reduce (lambda x,y: x if x>y else y,l))
