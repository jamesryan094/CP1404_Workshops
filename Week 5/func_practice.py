def main():
    print(calculate_area(5, 10))
    print(celcius_to_farenheit(50))
    print(calculate_bmi(55, 1.8))


def calculate_area(length, width):
    area = length * width
    return area

def celcius_to_farenheit(celcius_value):
    farenheit_value = celcius_value*9/5+32
    return farenheit_value

def calculate_bmi(weight, height):
    bmi = weight / height**2
    return bmi

main()