import re

print("\nMinimal Calc")
print("Type 'exit/quit' to exit\n")

previous = ""
eq = "0"

eq = input(eq)

if eq == "exit":
    exit()


eq = re.sub("[^0-9/*\-+] ", "", eq)
previous = eval(re.sub(r'^0+([1-9]\d*|\d)', r'\1', str(previous)+eq))


while True:

    #eq = input("Enter Equation:" if previous == 0 else str(previous))
    
    eq = input(previous)

    if eq == "exit":
        exit()


    eq = re.sub("[^0-9/*\-+] ", "", eq)
    previous = eval(str(previous)+eq)

    #previous = eval(re.sub(r'^0+([1-9]\d*|\d)', r'\1', str(previous)+eq))
    
