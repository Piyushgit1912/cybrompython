
# def print1_10():
#     li=[]
#     for i in range(11):
#         li.append(i)
#     return li
# ans = print1_10()
# print(ans)


# def fractorial():
#     num=int(input('enter num'))
#     ans=1
  
#     for i in range(1,num +1):
#         ans=ans*i
#     return ans
   
# ans=fractorial(num)
# print(ans)


#fibonacci series 

num = int(input('enter the number:'))
# first=0
# second=1
# # print(first,second,end=" ")
# for i in range(num):
#     nx=first+second
#     first=second
#     second=nx
#     print(nx,end=" ")

count=0
for i in range(2,num):
     if num%i== 0:
       print('not prime')
       break
     

    #    count=count+1

# if count==2 :
#     print('prime number')
# else:
#     print('not prime')
