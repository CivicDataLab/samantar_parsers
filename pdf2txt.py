from pdf2image import convert_from_path
import tempfile
from tesserocr import PyTessBaseAPI, PSM
from tqdm import tqdm
import os


for filename in os.listdir("/home/akhilesh/cdl/pf/data/budgets/19-20/as/pdf/"):
    with tempfile.TemporaryDirectory() as path:
        try:
            images = convert_from_path("/home/akhilesh/cdl/pf/data/budgets/19-20/as/pdf/" + filename, thread_count=8, output_folder=path)
            ofile = filename.split(".")[0] + ".txt"

            with PyTessBaseAPI(psm=4, lang='eng+asm') as api:
                with open("/home/akhilesh/cdl/pf/data/budgets/19-20/as/txt/" + ofile, "w+") as f:
                    for img in tqdm(images):
                        api.SetImage(img)
                        f.write(api.GetUTF8Text())
        except:
            print("filename: ", filename)
# for filename in tqdm(os.listdir("/home/akhilesh/cdl/union_budget_suggestions/imgs/")):
#     with tempfile.TemporaryDirectory() as path:
#         print(filename)
#         images = convert_from_path("/home/akhilesh/cdl/union_budget_suggestions/imgs/" + filename, thread_count=8, output_folder=path)

#         ofile = filename.split(".")[0] + ".txt"
#         with PyTessBaseAPI(psm=4, lang='hin+eng') as api:
#             with open("/home/akhilesh/cdl/union_budget_suggestions/txts_imgs/" + ofile, "w+") as f:
#                 for img in images:
#                     api.SetImage(img)
#                     f.write(api.GetUTF8Text())


# images = os.listdir("/home/akhilesh/cdl/union_budget_suggestions/imgs/")
# for img in tqdm(images):
#     ofile = img.split(".")[0] + ".txt"
#     with open("/home/akhilesh/cdl/union_budget_suggestions/txts_imgs/" + ofile, "w+") as f:
#         with PyTessBaseAPI(psm=4, lang='hin+eng') as api:
#             api.SetImageFile(img)
#             f.write(api.GetUTF8Text())
