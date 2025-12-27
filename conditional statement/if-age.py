age =  float(input("enter your age: "))
if age ==0:
    print('happy birthday')
elif age< 18:
    print(f'you are child {age}')
elif (18<=age<59):
    print(f'you are adult {age}')
elif  (59<age<100):
    print(f'you are senior citizen {age}')
else:
    print("invalid entry")


hindi=float(input('input hindi number: '))
if 0<hindi<100:
    english=float(input('enter englis nuber '))
    if 0<english<100:
        math = float(input('enter maths numver:'))
        if 0<math<100:
            avg=float ((hindi+english+math)/3)
            if 0<=avg<=34:
                print(f'you are fail with avg {avg}')
            elif 35<=avg<50:
                print(f'you are pass with avg {avg}')
            elif 50<=avg<75:
                print(f'you are good with avg {avg}')
            elif 75<=avg<=100:
                print(f'you are excelent with avg {avg}')
            else:
                print("")
         

