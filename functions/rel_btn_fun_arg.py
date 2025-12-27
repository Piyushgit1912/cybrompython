# p=int(input('enter p--'))
# q=int(input('enter y--'))
# r=int(input('enter z--'))
# # def sum(x,y,z):
  
#     print(f' {x}, {y}, {z}',x+y+z)

# ans=sum(x=p,y=q,z=r)

# def fun_name(**kword):
#     print(kword)
#     print(type(kword))
#     for i in kword.keys():
#         print(i)
#     for i in kword.values():
#         print(i)

#     for i,j in kword.items():
#         print( 'key=' ,i, 'value=', j )



# fun_name(**eval (input('enter any dict:-')))

# def fun_name(x,y=0,*z,p,**q):
#     print(x,type(x))
#     print(y,type(y))
#     print(z,type(z))
#     print(p,type(p))
#     print(q,type(q))
    
# fun_name(10,20,30,40,50,p=5,r=2,s=1)

# def natural(n):
#     for i in range (1,n+1):
#         print(i)
# count=0
# def sum(n):
#     for i in range (1,n+1):
#         count=count+i
#         print(count)

    

# n=int(input('enter number to print --'))
# natural(n)
# sum(n)

count=0
def prime(n):
   
    for i in range (1,n):
        if n%i==0 :
            count=count+1
            if count>2:
                print('not a prime')
                break
        
n=int(input('enter the num-'))
prime(n)
            