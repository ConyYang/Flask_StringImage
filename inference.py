import requests
from PIL import Image

input_width = 100
input_height = 100


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
print(len(ascii_char))


def get_char(r, g, b, a=256):
    if a == 0:
        return ' '

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # map the length of string to rgb 256
    unit = (265.0 + 1.0) / len(ascii_char)
    index = int(gray / unit)
    return ascii_char[index]


def get_txt(input_img_path):
    img = Image.open(input_img_path)
    img = img.resize((input_width, input_height), Image.NEAREST)

    # initialize the string
    txt = ""

    # Traverse Every RGB Elements
    for i in range(input_height):
        for j in range(input_width):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'
    print(txt)

    return txt

