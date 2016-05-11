"""Program takes height and weight in ms and kgs respectively
and calculates BMI"""

print("Body-mass-index calculator, by James")

weight=float(input("Please enter weight in kgs"))
height=float(input("Please enter height in m"))

bmi= weight / height**2

print("Therefore, your BMI value is:", bmi, "\nThank you!")