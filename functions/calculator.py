while(True):
    # print('hellooooo.....')
    
    print("Please Enter \n 1. For Addition\n 2. For Subtraction\n 3. For Multiplication\n 4. For Divison \n 5. For Exit")
    n=int(input("enter any button--:"))
    if n in (1,2,3,4,5):  

        if n in (1,2,3,4):

            if n==1:
                num=int(input("You selected addition\n Enter the number of variables for addition:- ")) 

                l=[]
                for i in range(1,num +1):
                    value=eval(input(f'enter {i} number:-'))
                    l.append(value)

                sum=0
                for i in l:
                    sum=sum+i
                print('sum = ',sum)
            
            if n==2:
                num=int(input(" You selected subtraction\n Enter the number of variables for subtraction-:")) 
                l=[]

                for i in range(1,num +1):
                    value=eval(input(f'enter {i} number:-'))
                    l.append(value)
                result= l[0]
                for i in l:
                 
                 result=result-l[i]
                print(result)

            if n==3:
             num=int(input(" You selected Multiplication\n Enter the number of variables for multiplication-:")) 
             l=[]

             for i in range(1,num +1):
                 value=eval(input(f'enter {i} number:-'))
                 l.append(value)
             result=1
             for i in l:
              
              result=result*i
             print(result)

            if n==4:
            
             nominator=int(input(" You selected divison \n Enter the nominator-:")) 
             denominator=int(input(" Enter the denominator-:")) 
            #  l=[]

            #  for i in range(1,num +1):
            #      value=eval(input(f'enter {i} number:-'))
            #      l.append(value)
            #  result=1
            #  for i in l:
              
             result=(nominator/denominator)
             modulo=(nominator%denominator)
             print('Ans.= ', result) 
             print('Remainder = ', modulo)



        else:
            break  
        
    else:
        print('Please enter valid value!\n hit the code again and be careful...')
        break
    
#  1. add
#  2. sub
#  3. div
#  4. multiplication
#  5. exit
# enter any button--:5