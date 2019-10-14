"""
Script for parsing pdfs to htmls. Built for parsing budget speeches

Usage:
    pdf2html.py --filename=<f> --path=<p>

Options:
    --filename=<f>      Provide pdf to be converted
    --path=<p>          Specify output path for the html
"""
from docopt import docopt
import pdftotree
import os

def converter(ifile: str, ofile: str):
    """
    convert pdf to html using pdftotree
    :params ifile: input pdf file
    :params ofile: output html file
    """
    pdftotree.parse(ifile, html_path=ofile,
            model_type=None, model_path=None, favor_figures=True, visualize=False)


if __name__ == "__main__":
    args = docopt(__doc__)

    filename = args["--filename"]

    path = args["--path"]

    if not path:
        path = os.path.dirname(os.path.realpath(__file__))

    converter(filename, path)
