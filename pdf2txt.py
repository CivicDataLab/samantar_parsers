"""
Script for converting pdfs to text files using tesseract.

Usage:
    pdf2txt.py --input-folder-path=<if> [--output-folder-path=<of>]

Options:
    --input-folder-path=<if>            Provide folder path of pdfs to be converted
    --output-folder-path=<op>           Specify output path for the text files
"""
from docopt import docopt
from pdf2image import convert_from_path
import tempfile
from tesserocr import PyTessBaseAPI, PSM
from tqdm import tqdm
import os


## TODO: Add language support. Right now, its defaulted to English and Assamese at the moment.

def converter(ifolder: str, ofolder: str):
    """
    convert pdf to text file using tesseract
    :params ifolder: provide input folder path
    :params ofolder: provide output folder path
    :params langs: provide the languages that you would like to recognise
    """
    for filename in os.listdir(ifolder):
        with tempfile.TemporaryDirectory() as path:
            try:
                images = convert_from_path(ifolder + filename, thread_count=8, output_folder=path)
                ofile = filename.split(".")[0] + ".txt"

                with PyTessBaseAPI(psm=4, lang='eng+asm') as api:
                    with open(ofolder + ofile, "w+") as f:
                        for img in tqdm(images):
                            api.SetImage(img)
                            f.write(api.GetUTF8Text())
            except:
                print(f"{filename} file not converted")


if __name__ == "__main__":
    args = docopt(__doc__)

    ifolder = args["--input-folder-path"]

    ofolder = args["--output-folder-path"]

    if not ofolder:
        ofolder = os.path.dirname(os.path.realpath(__file__))

    converter(ifolder, ofolder)
