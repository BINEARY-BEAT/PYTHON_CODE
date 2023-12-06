import time
import os

def CALCULATOR():

    def ADDATION(a,b):
        return a+b

    def SUBTRACTION(a,b):
        return a-b

    def MULTIPLICATION(a,b):
        return a*b
    try:
        def DIVISION(a,b):
            return a/b
    except ZeroDivisionError:
        print("ERROR")

    def FIND_MAX(a,b,c):
        if a >=b  and a>c:
            return("\nA is maximum!\n")
        elif b>=a and b>=c:
            return("\nB is maximum \n")
        else:
            return("\nC is  maximum\n")

    def EVEN(a,b):
        if a%2==0 and b%2==0:
            return ("\nA and B boath are Even\n")
        elif a%2 != 0 and b%2 !=0:
            return ("\n A and B boath are Odd\n")
        elif a%2==0:
            return ("\nA is Even and B is Odd\n")
        else:
            return ("\nB is Odd and A is Even\n")

    def FACTORIAL (a):
        if a == 0:
            return 1
        else:
            fictorial=1
            for i in range (1,a+1):
                fictorial=fictorial*i
        return fictorial

    def SRAURE(a):
        return a**2

    def CUBE(a):
        return a**3

    def POWER(Base,Exponent):
        return Base** Exponent

    while True:
        try:
            CHOICE=int(input('''Enter index of any Operation To Do...\n\n
            1-ADDATION 
            2-SUBTRACTION
            3-MULTIPLICATION
            4-DIVISION
            5-MAXIMUM NUMBER CALCULATE
            6-EVEN ODD CHECK
            7-FACTORIAL
            8-SQAURE
            9-CUBE
            10-POWER
            :\n   
            '''))
        
            
        

            if CHOICE ==1:
                    a=int(input("\nEnter The Value Of A\n:"))
                    b=int(input("\nEnter The Value Of B\n:"))
                    result=ADDATION(a,b)
                    print("\nSum Of Given numbers is : ",result)

            elif CHOICE ==2:
                a=int(input("\nEnter The Value Of A\n:"))
                b=int(input("\nEnter The Value Of B\n:"))
                result=SUBTRACTION(a,b)
                print(f"\n{a}-{b} is ={result}")
                
            elif CHOICE ==3:
                a=int(input("\nEnter The Value Of A\n:"))
                b=int(input("\nEnter The Value Of B\n:"))
                result=MULTIPLICATION(a,b)
                print(f"\n {a}x{b}={result} ")
                
            elif CHOICE==4:
                a=int(input("\nEnter The Value Of A\n:"))
                b=int(input("\nEnter The Value Of B\n:"))
                result=DIVISION(a,b)
                print(f"{a}/{b}={result}")

            elif CHOICE==5:
                a=int(input("\nEnter The Value Of B\n:"))
                b=int(input("\nEnter The Value Of B\n:"))
                c=int(input("\nEnter The Value Of C\n:"))
                result=FIND_MAX(a,b,c)
                print("The Maximum Number is ",result)

            elif CHOICE==6:
                a=int(input("\nEnter The Value Of A\n:"))
                b=int(input("\nEnter The Value Of B\n:"))
                result=EVEN(a,b)
                print(result)

            elif CHOICE==7:
                a=int(input("\nEnter The Value Of A\n:"))
                result=FACTORIAL(a)
                print("\nFactorial of Given Number is : ",result)

            elif CHOICE ==8:
                a=int(input("\nEnter The Value Of A\n:"))
                result=SRAURE(a)
                print("\nThe Sqaure Of Given Number is : ",result)

            elif CHOICE ==9:
                a=int(input("\nEnter The Value Of A\n:"))
                result=CUBE(a)
                print("\nThe Cube Of Given Number is :",result)

            elif CHOICE ==10:
                Base=int(input("\nEnter The Value Of Base\n:"))
                Exponent=int(input("\nEnter The Value Of Exponent\n:"))
                result=POWER(Base,Exponent)
                print(f"{Base} To The Power Of {Exponent} is : {result}")

            Choice = input("\nDo You Want Make another Calculation[Y/N]\n:")
            if Choice == 'y' or Choice=='Y':
                CALCULATOR()
            else:
                print("\nExiting The Calculator....\n")
                time.sleep(3)
                os.system("cls")
                exit()
        except Exception:
            print("\SOME THING WENTS WRONG!\n")
            time.sleep(2)
            os.system("cls")
            continue
            
        
if __name__== '__main__':
    CALCULATOR()
