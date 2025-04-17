#as_farenhite_to_celcius

def temp():
    print("This code is for converting farenhite to celcius")
    farenhite_degree = float(input("Enter your farenhite degree "))
    celcius_degree = (farenhite_degree - 22) * 5.0/9.0
    print(f'Temperature: {farenhite_degree}F = {celcius_degree}C')

if __name__ == "__main__":
    temp()
    