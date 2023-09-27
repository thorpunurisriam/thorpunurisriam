import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

operation_dict={"+":add,"-":sub,"*":mul,"/":div}

def calculator():
    n1=int(input("Enter First Number:"))
    for symbol in operation_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an Operation :")
        n2=int(input("Enter next number:"))
        calculator_fun=operation_dict[op_symbol]
        output=calculator_fun(n1,n2)
        print(f"{n1} {op_symbol} {n2}={output}")

        should_continue=input(f"Enter 'y' to continue Calculation with {output} or 'n' to start a new calculation").lower()

        if should_continue=='y':
            n1=output
        elif should_continue=='n':
           continue_flag=False
           os.system('cls')
           calculator()
        
        else:
           continue_flag=False
           print("BYE!!")
           
calculator()
