print("Simple Calculator")
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
print("Choose operation")
print("Addition:+")
print("Subtraction:-")
print("Multiplication:*")
print("Division:/")
operation=input("Enter your operation:")
if operation=="+":
    result=a+b
    print("Result=",result)
elif operation=="-":
    result=a-b
    print("Result=",result)
elif operation=="*":
    result=a*b
    print("Result=",result)
elif operation=="/":
    if b!=0:
        result=a/b
        print("Result=",result)
    else:
        print("Error:Zero Division")
else:
    print("Invalid operation")
