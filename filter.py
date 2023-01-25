from PIL import Image
import argparse

def get_args():
    parser = argparse.ArgumentParser("put an interlacing gilter on a photo")
    parser.add_argument("-i", "-input", type=str, help="path to the image you want to put an interlacing filter on", required=True)
    parser.add_argument("-s", "-show-image", type=str, choices=["y", "n"], default="n", required=False, help="choose if you want to see the photo after the program is done (default is no")
    parser.add_argument("-si", "-save-image", type=str, choices=["y", "n"], default="n", required=False, help="choose if you want to save the image (default is no)")
    parser.add_argument("-dr", "-amt-to-darken-pixels", type=str, default=100, required=True, help="choose the amount to darken each pixel (default is 100)")
    parser.add_argument("-as", "-amt-of-lins-btwn", type=str, default=1, required=False, help="choose the amount")

    parser.add_argument("-size", type=int, default=50, help="Size of the ascii image")
    parser.add_argument(
        "-print",
        type=bool,
        default=False,
        help="Choose if to print the file to the terminal",
    )
    parser.add_argument(
        "-input", type=str, default="should_exit", help="Path to input image"
    )
    parser.add_argument(
        "-output", type=str, default="ascii.txt", help="Path to output text file"
    )
    parser.add_argument(
        "-mode",
        type=str,
        default="simple",
        choices=["simple", "flat"],
        help="basic ascii table, 2 characters that create a flat image",
    )
    parser.add_argument(
        "-add_ascii_table",
        type=str,
        default=".,:;+*?%#@S",
        help="add your own ascii table",
    )

    args = parser.parse_args()
    return args

def interlaceImage(imageName, amtToDarken, lineToDarken, amtOfSpaceBetweenDarkenLine, amtOfLinesToDarkenEachTime):
    with Image.open(imageName) as image:
        image = image.convert('RGB')
        pixels = image.load()

        for width in range(image.size[0]):  # for every pixel:
            for height in range(image.size[1]):
                if lineToDarken == "height" and width % amtOfSpaceBetweenDarkenLine == 0:
                    for dl in range(amtOfLinesToDarkenEachTime):
                        if dl+width >= image.size[0]:
                            break

                        r, g, b = image.getpixel((width+dl, height))
                        pixels[width+dl, height] = (r-amtToDarken, g-amtToDarken, b-amtToDarken)

                if lineToDarken == "width" and height % amtOfSpaceBetweenDarkenLine == 0:
                    for dl in range(amtOfLinesToDarkenEachTime):
                        if dl+height >= image.size[1]:
                            break

                        r, g, b = image.getpixel((width, height + dl))
                        pixels[width, height + dl] = (r - amtToDarken, g - amtToDarken, b - amtToDarken)

        image.show()


def main():
    imageName = input("enter the full path to the image: ")
    amtToDarken = input("enter the amount each pixel should be darkened when interlacing: ")
    lineToDarken = input("""enter line to darken ["width", "height"]: """)
    amtOfSpaceBetweenDarkenLine = input("enter the amount of space between each darkened line ")
    amtOfLinesToDarkenEachTime = input("enter the amount of lines to darken each time: ")

    if lineToDarken not in ["width", "height"]:
        quit("you gotta enter a width or a height")

    try:
        amtToDarken = int(amtToDarken)
        amtOfSpaceBetweenDarkenLine = int(amtOfSpaceBetweenDarkenLine)
        amtOfLinesToDarkenEachTime = int(amtOfLinesToDarkenEachTime)
    except:
        quit("you gotta uyser numbers when i tell you nigga!")

    interlaceImage(imageName, amtToDarken, lineToDarken, amtOfSpaceBetweenDarkenLine, amtOfLinesToDarkenEachTime)

main()
# C:\\Users\\student\\Pictures\\index.jpg
