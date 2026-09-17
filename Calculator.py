def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("What operation do you want to preform:")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")
choice=input("Please enter a/b/c/d:")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if choice==("a"):
    print("The solution is ",add(num1,num2))
elif choice==("b"):
    print("The solution is ",subtract(num1,num2))
elif choice==("c"):
    print("The solution is",multiply(num1,num2))
elif choice==("d"):
    print("The solution is",divide(num1,num2))
else:
    print("Invalid input")