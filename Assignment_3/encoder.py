from PIL import ImageDraw, Image

def encode(msg: str):

    msg = msg.lower()

    width_of_chars = {
        " ": 1,
        "a": 2,
        "b": 3,
        "c": 4,
        "d": 5,
        "e": 6,
        "f": 7,
        "g": 8,
        "h": 9,
        "i": 10,
        "j": 11,
        "k": 12,
        "l": 13,
        "m": 14,
        "n": 15,
        "o": 16,
        "p": 17,
        "q": 18,
        "r": 19,
        "s": 20,
        "t": 21,
        "u": 22,
        "v": 23,
        "w": 24,
        "x": 25,
        "y": 26,
        "z": 27
    }

    step = 9

    size = (800, 400)

    im = Image.new(mode="1", size=size, color=1)

    x = 9

    y0 = 10

    y1 = 350

    y2 = 150

    y3 = 250

    draw = ImageDraw.Draw(im)

    for i in msg:

        if i == " ":
            draw.rectangle([(x, y2), (x + width_of_chars[str(i)] - 1, y3)], fill=0)
            x += step + width_of_chars[" "]
        else:
            draw.rectangle([(x, y0), (x + width_of_chars[str(i)] - 1, y1)], fill=0)
            x += step + width_of_chars[str(i)]

    im.save("output.png")

def main():
    encode("ABBAS CHEDDAD")

if __name__ == "__main__":
    main()
