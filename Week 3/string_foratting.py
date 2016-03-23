name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text:
print("My guitar: " + name + ", first made in " + str(year))

# A better way using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency:
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 4560, -25]
names = ["bob", 'jane', "abcd", "jwlefhweu2y44tiewrjghwerut2y5"]
for i in range(len(names)):
 print("Number {0} is ${1:>100}".format(i + 1, names[i]))