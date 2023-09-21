def input_int(prompt = ""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("my_int is not an integer.")
        

    
age = input_int("Input age: ")
length = input_int("Input length: ")
weight = input_int("Input weight: ")
print(f"age = {age}, length = {length}, weight = {weight}")

