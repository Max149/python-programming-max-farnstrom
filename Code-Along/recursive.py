def main():
    print("start of main")
    func_b
    func_a()
    func_b()
    
    print("end of main")

    

def func_a():
    print("start of func_a()")
    
    func_b()


def func_b():
    print("start of func_b()")
    print("end of func_b")



def print_hello(n):
    for i in range(n):
        print("Hello")

def print_hello_recursive(n):
    print("Hello")
    if n > 1: print_hello_recursive(n-1)
    return

print_hello_recursive(4)
#main()