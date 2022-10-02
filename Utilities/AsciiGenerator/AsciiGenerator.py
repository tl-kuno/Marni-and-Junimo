# ASCII Cartoon Generator
# Author: Taylor Kuno
# Adapted From: https://www.youtube.com/watch?v=v_raWlX7tZY
#               https://github.com/kiteco/python-youtube-code/blob/master/ascii/ascii_convert.py
# Description:  Takes an image of a drawing and returns a ASCII cartoon
#               The cartoon is both displayed in console and saved to file

import os
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", " ", " ", " ", " "]

# resize image according to a new width
def resize_image(image, new_width=100):
    """Resizes an image to the given width, maintaining aspect ratio.

    Args:
        image (PIL Image object): the image to be resized
        new_width (int, optional): the width to which the image will be resized. Defaults to 100.

    Returns:
        PIL Image object: the resized image
    """
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# switch the photo to grayscale
def to_grayscale(image):
    """Converts a given image to grayscale

    Args:
        image (PIL Image object): the image to be converted

    Returns:
        PIL Image object: the given image converted to grayscale
    """
    return image.convert("L")


def pixel_to_ascii(image):
    """Interprets the intensity of each pixel and assigns an ASCII char with similar intensity.
        Concatenates to an array of all ASCII chars.

    Args:
        image (PIL Image object): The image to be converted to ASCII characters

    Returns:
        array: array of ASCII chars corresponding to the pixels in the image
    """
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(new_width=100):
    """Requests a filepath to an image from the user and converts the image to ASCII art.

    Args:
        new_width (int, optional): the desired width of the new image. Defaults to 100.
    """

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
    # print(ascii_image)

    # create new filepath
    base_path = "C:/dev/marni-and-junimo/Marni-and-Junimo/Utilities/AsciiGenerator/image_result/"
    new_filepath = base_path + "ascii_" + basename + ".txt"

    # save
    with open(new_filepath, "w+", encoding="utf-8") as file:
        file.write(ascii_image)


if __name__ == '__main__':
    main()
