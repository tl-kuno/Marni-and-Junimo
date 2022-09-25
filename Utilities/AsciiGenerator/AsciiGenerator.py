# ASCII Cartoon Generator
# Author: Taylor Kuno
# Adapted From: https://www.youtube.com/watch?v=v_raWlX7tZY
# Description:  Takes an image of a drawing and returns a ASCII cartoon 
#               The cartoon is printed both to the console and to the 

"""
@ # S %  * +  : 
"""

import PIL


def resize_image(image, size):
    pass
    

def main():
    # Open image
    # Print error if file ivalid
    # Create ASCII char list
    # resize image
    # convert each pixel to greyscale
    # convert pixels to string of ASCII
    path = input("Enter the pathname of the image: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print("Pathname is invalid")
    
    return

if __name__ == '__main__':
    main()
