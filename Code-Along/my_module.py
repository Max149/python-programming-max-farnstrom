import math

def main():
    print(square(2))
    print(square(3))
    print(square(-3))
    print(square(0))
    print(square(1.2))



def square(n):
    return n * n

def sqrt(n):
    return math.sqrt(n)

if __name__ == "__main__":
    main()
