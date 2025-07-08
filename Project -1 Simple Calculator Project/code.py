def add():
    a,b=eval(input("Enter the two number seprated by comma to add : "))
    return a+b
def subtract():
    a,b=eval(input("Enter the two number seprated by comma to subtract : "))
    return a-b
def multiply():
    a,b=eval(input("Enter the two number seprated by comma to multiply: "))
    return a*b
def division():
    a,b=eval(input("Enter the two number seprated by comma to divide : "))
    return a/b
def power():
    a,b=eval(input("Enter the subscript then superscipt seprated by comma to perform : "))
    return a**b

def main():
    ch=0
    while ch!=6:
        print("Choose Options to perform Various Simple Calculations. ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Power")
        print("6. EXIT")
        ch=int(input("Enter Your choice :- "))
        if ch==1:
            output=add()
            print("Current output for the operation is : ",output)
        elif ch==2:
            output=subtract()
            print("Current output for the operation is : ",output)
        elif ch==3:
            output=multiply()
            print("Current output for the operation is : ",output)
        elif ch==4:
            output=division()
            print("Current output for the operation is : ",output)
        elif ch==5:
            output=power()
            print("Current output for the operation is : ",output)
        elif ch==6:
            print("THANK YOU ....")
            break
        else:
            print("INVALID ATTEMPT.......")
    
main()