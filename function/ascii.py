from PIL import Image
import argparse

parser = argparse.ArgumentParser()
# define input file, output file
parser.add_argument('file')
parser.add_argument('-o', '--output')
# output width & height of photo
parser.add_argument('--width', type=int, default=100)
parser.add_argument('--height', type=int, default=100)

# get arguments from parse
args = parser.parse_args()

input_img_path = args.file
input_width = args.width
input_height = args.height
output_img_path = args.output

# the set of strings we use to plot
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


if __name__ == '__main__':
    img = Image.open(input_img_path)
    img = img.resize((input_width, input_height), Image.NEAREST)

    # initialize the string
    txt = ""

    # Traverse Every RGB Elements
    for i in range(input_height):
        for j in range (input_width):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'
    print(txt)

    if output_img_path:
        with open(output_img_path, 'w') as f:
            f.write(txt)
    else:
        with open("../output.txt", 'w') as f:
            f.write(txt)

