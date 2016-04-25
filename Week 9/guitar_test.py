from guitars import Guitar
def main():
    stratcat = Guitar("Fender Stratocaster", 1954, 37500)
    fatcat = Guitar("Gibson Hamburger", 1980, 20)
    print(stratcat)
    print(stratcat.get_age())
    print(stratcat.is_vintage())
    print(fatcat)
    print(fatcat.get_age())
    print(fatcat.is_vintage())

main()
