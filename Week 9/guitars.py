class Guitar(object):
    def __init__(self, name='', year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return"{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False


def main():
    guitars = []
    # name = '.'
    name = input("Name:")
    while name != '':
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(new_guitar)
        guitars.append(new_guitar)
        name = input("Name:")

    for i, guitar in enumerate(guitars):
        if not guitar.is_vintage():
            vintage_string = ""
        else:
            vintage_string = "(Vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

if __name__ == "__main__":
    main()