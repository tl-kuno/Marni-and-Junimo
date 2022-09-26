# ASCII Cartoon Generator
# Author: Taylor Kuno
# Adapted From: https://www.youtube.com/watch?v=v_raWlX7tZY
#               https://github.com/kiteco/python-youtube-code/blob/master/ascii/ascii_convert.py
# Description:  Takes an image of a drawing and returns a ASCII cartoon
#               The cartoon is both displayed in console and saved to file

import os
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", " ", " ", " ", " "]


def resize_image(image, new_width):
    width, height = image.size
    new_height = int(new_width * (height/width))
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def to_grayscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=100):

    path = input("Enter the pathname of the image: \n")
    try:
        image = Image.open(path)
        filename = os.path.basename(path)
        basename = os.path.splitext(filename)[0]

    except FileNotFoundError:
        print("Pathname is invalid")
        exit()

    # transform to string of ascii chars
    new_image_data = pixel_to_ascii(to_grayscale(
        resize_image(image, new_width)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                             for index in range(0, pixel_count, new_width)])

    # display
    print(ascii_image)

    # create new filepath
    base_path = "C:/dev/marni-and-junimo/Marni-and-Junimo/Utilities/AsciiGenerator/image_result/"
    new_filepath = base_path + "ascii_" + basename + ".txt"

    # save
    with open(new_filepath, "w+", encoding="utf-8") as file:
        file.write(ascii_image)


if __name__ == '__main__':
    main()
