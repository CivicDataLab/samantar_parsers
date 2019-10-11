import pdftotree
import os

# html = pdftotree.parse('data/pdfs/2008_-_2009_.pdf', html_path="data/2008_-_2009_.html", model_type=None,
# model_path=None, favor_figures=True, visualize=False)

data_dir = 'data'
pdf_src = '{}/pdf'.format(data_dir)
html_src = '{}/html/'.format(data_dir)
directory = os.fsencode("%s" % pdf_src)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    try:
        budget_doc = os.path.splitext(filename)[0]
        if filename.endswith(".pdf") and not os.path.exists('{}{}.html'.format(html_src, budget_doc)):
            print(filename)
            pdftotree.parse('{}/{}'.format(pdf_src, filename), html_path=html_src,
                            model_type=None, model_path=None, favor_figures=True, visualize=False)
    except:
        print(filename)
