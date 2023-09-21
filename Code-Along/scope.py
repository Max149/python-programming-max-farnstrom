# in python we have two types of scope, (life-time of variable)
# Local scope: only available locally in a function
# Global scope: available through execution of program

name = "max"

def main():
    global name
    name = "karl oskar"
    print(name)

print(name)
main()
print(name)

# python doesnt have block scope
# if name == ("max"):
#     last_name = "Farnstrom"
    
    
# print(last_name)

# for i in range(3):
#     print(i)

# print(f"i = {i}")

