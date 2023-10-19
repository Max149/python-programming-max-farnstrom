

def heltal(n): 
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i in [2, 4]:
                print("x o x o x", end=' ')
                break
            else:
                print("x", end=' ')
        print(" ")

heltal(5)

# x x x x x
# x o x o x
# x x x x x
# x o x o x
# x x x x x
