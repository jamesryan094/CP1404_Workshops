# constants
TARIFF_01 = 35
TARIFF_02 = 30

print("Electricity Bill Estimator")

# input
# cents_per_kwh= float(input("Cents per kilowatt hour(kWh):"))
tariff = int(input("please enter your tariff:"))
while tariff != 1 and tariff != 2:
    print("Please enter a valid tariff value")
    tariff = int(input("please enter your tariff:"))

daily_use_kwh = float(input("Enter your daily usage in kWh:"))
billing_peroid_days = int(input("Enter the length of your billing period, in days:"))

# processing
# estimated_bill=cents_per_kwh*daily_use_kwh*billing_peroid_days/100
if tariff == 1:
    cost = TARIFF_01
elif tariff == 2:
    cost = TARIFF_02

estimated_bill = cost * daily_use_kwh * billing_peroid_days / 100

# output
print(estimated_bill)
