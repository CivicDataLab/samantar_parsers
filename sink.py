import pdftotree
import PyPDF2

# html = pdftotree.parse('data/1947_-_1948_.pdf', html_path="data/1947_-_1948_.html", model_type=None, model_path=None,
#                        favor_figures=True, visualize=False)
# print(html)

# # creating a pdf file object
# pdfFileObj = open('data/1947_-_1948_.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# Open a PDF file.
fp = open('data/1947_-_1948_.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)

# import io
# from pdfminer.converter import HTMLConverter
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfpage import PDFPage
#
#
# def extract_text_from_pdf(pdf_path):
#     resource_manager = PDFResourceManager()
#     # fake_file_handle = io.StringIO()
#     html_file = open("data/as.html", "wb")
#     converter = HTMLConverter(resource_manager, html_file)
#     page_interpreter = PDFPageInterpreter(resource_manager, converter)
#     with open(pdf_path, 'rb') as fh:
#         for page in PDFPage.get_pages(fh,
#                                       caching=True,
#                                       check_extractable=True):
#             page_interpreter.process_page(page)
#         # text = html_file.read()
#     # close open handles
#     converter.close()
#     html_file.close()
#     if text:
#         return text
#
#
# if __name__ == '__main__':
#     print(extract_text_from_pdf('data/1947_-_1948_.pdf'))
