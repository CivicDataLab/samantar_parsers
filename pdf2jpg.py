"""
Script to convert pdfs to images.

Usage:
    pdf2jpg.py --filename=<f> [--path=<p>]

Options:
    --filename=<f>      Provide pdf to be converted
    --path=<p>          Specify output path for images. (Optional)
"""
from docopt import docopt
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os


if __name__ == "__main__":
    args = docopt(__doc__)

    filename = args["--filename"]

    path = args["--path"]

    if not path:
        path = os.path.dirname(os.path.realpath(__file__))

    pages = convert_from_path(filename, 500)
    print("path: ", path)
    img_count = 1

    # Iterate through all the pages stored above
    for page in pages:
        img_filename = path + "/page_"+str(img_count)+".jpg"

        page.save(img_filename, 'JPEG')

        img_count = img_count + 1
