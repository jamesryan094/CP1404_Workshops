HEX_COLOUR_CODES = {"Alice Blue": "#f0f8ff", "Black": "#000000", "Blue": "#0000ff",
                    "Brown": "#a52a2a", "Firebrick": "#b22222", "Gray": "#bebebe",
                    "Green1": "#00ff00", "HotPink": "#ff69b4", "Red1": "#ff0000",
                    "Orange1": "#ffa500"}

colour = input("Input colour name(eg,'Firebrick'): ")
while colour != "":
    if colour in HEX_COLOUR_CODES.keys():
        print(HEX_COLOUR_CODES[colour])
    else:
        print("Invalid input, try again")
    colour = input("Input colour name(eg,'Firebrick': ")
