def triangle():
    print("This code is about sum of triangle sides")
    side1: float = float(input("Enter your first side no of triangle "))
    side2: float = float(input("Enter your second side no of triangle "))
    side3: float = float(input("Enter your third side no of triangle "))
    total: float = float(side1 + side2 + side3)
    print(f'The sum of {side1} + {side2} and {side3} is {total}')

if __name__ == "__main__":
    triangle()
