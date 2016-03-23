num_item = int(input("enter number of items purchased"))
while num_item <0:
    print("Invalid number of items!")
    num_item = int(input("enter number of items purchased"))

total_cost = 0
for i in range(0, num_item):
    shipping_cost = float(input("Enter the shipping cost of item {}".format(i+1)))
    total_cost += shipping_cost

if total_cost >= 100:
    total_cost -= (total_cost *0.1)
print ("$", total_cost, sep="")
