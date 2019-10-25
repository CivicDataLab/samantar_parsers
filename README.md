# samantar_parsers

[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://github.com/CivicDataLab/complang/blob/master/LICENSE)

Scrapers and Parsers for Indian Budget Speech Documents


## Installation

### Install tesseract

Arch linux
```
sudo pacman -S tesseract
```

Ubuntu
```
sudo apt-get install tesseract-ocr
```

### Download tesseract-data

Arch linux
```
sudo pacman -S tesseract-data
```

Ubuntu
```
sudo apt-get install tesseract-ocr-all
```

### Install [Tabula](https://github.com/tabulapdf/tabula) or [Tabula extractor](https://github.com/tabulapdf/tabula-extractor)

## Run Scraper
```
python speech_scraper.py [--path]
```

## Parsing

It is recommended to convert pdfs to text files for better text extraction. HTML markups are messy to parse.

```
pdf2txt.py -o output.txt <pdf-file>
```

### If the document is written in legacy font. Try this:

Convert PDF to image
```
python pdf2jpg.py --filename <input-file path> --path <output-file path>
```

For help:
```
python pdf2jpg.py --help
```

Convert the Image to PDF with text layer only
```
tesseract <img-filename> <pdf-filename> -l eng+hin test pdf
```

eg:
```
tesseract page.jpg test -l eng+hin pdf
```

Convert the above PDF to csv

```
tabula <pdf-file> -o <output-csv>
```
