from PIL import Image

import numpy as np

def decode(filename: str):

    width_of_chars = {
            1: " ",
            2: "a",
            3: "b",
            4: "c",
            5: "d",
            6: "e",
            7: "f",
            8: "g",
            9: "h",
            10: "i",
            11: "j",
            12: "k",
            13: "l",
            14: "m",
            15: "n",
            16: "o",
            17: "p",
            18: "q",
            19: "r",
            20: "s",
            21: "t",
            22: "u",
            23: "v",
            24: "w",
            25: "x",
            26: "y",
            27: "z"
        }
    
    with Image.open(filename) as im:
        a = np.asarray(im)

    string = ""

    row = a[200, :]

    black_pixels = row == 0

    bars = []

    in_bar = False

    for x, black in enumerate(black_pixels):

        if black and not in_bar:
            start = x
            in_bar = True

        elif not black and in_bar:
            end = x
            bars.append((start, end))
            in_bar = False

    if in_bar:
        bars.append((start, len(row)))

    for element in bars:

        width = element[1] - element[0]

        string += width_of_chars[width]

    return(string)

        
            


def main():
    fn = "Abbas Own Barcode-3.png"
    x = decode(fn)

    print(x)

if __name__ == "__main__":
    main()