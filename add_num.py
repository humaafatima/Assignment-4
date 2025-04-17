#Add two numbers

def add():
    print("This program will add two numbers")
    first_num = int(input("Enter your first number "))
    second_num = int(input("Enter second number "))
    sum = int(first_num + second_num)
    print(f"The sum of first {first_num} and {second_num} is {sum}")

add()