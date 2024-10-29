numb=int(input("Enter a number: "))
if numb%2==0:
    print("Even")
else:
    print("Odd")

numb2=int(input("Enter a number: "))
numb3=int(input("Enter a number: "))
numb4=int(input("Enter a number: "))

if numb2>numb3 and numb2>numb4:
    print(f"{numb2} numb2 is the greatest number")
elif numb3>numb2 and numb3>numb4:
    print(f"{numb3} numb3 is the greatest number")
else:
    print(f'{numb4} numb4 is the greatest number')