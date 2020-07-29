# Imports
import os
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import pytesseract
import pandas as pd
from jobs.tender_profile_extractor import settings


def get_documents(path: str = "../data/Soportes") -> dict:
    results = {}
    for root, dirs, files in os.walk(path):
        root = root.replace('\\', '/')
        if len(files) > 0:
            results[int(root.split('/')[-1:][0])] = files
        else:
            print('The * ' + root + ' * has no files')
            continue
    return results


def documents_data_frame(path: str = "../data/Soportes") -> pd.DataFrame:
    tenders_files = get_documents(path)

    keys = tenders_files.keys()
    final = {}
    for key in keys:
        temp_len = len(tenders_files[key])
        for file_key in range(0, temp_len):
            final[str(key) + '_' + str(file_key)] = tenders_files[key][file_key]

    results = pd.DataFrame(final, index=range(1)).T.reset_index().rename(columns={'index': 'ID', 0: 'FILE_NAME'})
    results['TENDER_ID'] = [i.split('_')[0] for i in results.ID]
    results['DOCUMENT_ID'] = [i.split('_')[1] for i in results.ID]

    return results


def pdf_to_txt(pdf_path: str = None,
               tender_id: int = None,
               document_id: int = None,
               path: str = "../data/Soportes",
               resolution: int = 500,
               bin_path: str = settings.POPPLER_PATH,
               tysseract_path: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
    pytesseract.pytesseract.tesseract_cmd = tysseract_path

    pdf_file = pdf_path

    input_pdf = PdfFileReader(open(pdf_file, "rb"))
    max_pages = input_pdf.numPages

    image_counter = 1

    tender_jpg_dir = r"{}/{}/{}".format(path, tender_id, document_id)
    print(tender_jpg_dir)
    if not os.path.exists(tender_jpg_dir):
        os.makedirs(tender_jpg_dir)

    for pages_ in range(1, max_pages, 10):

        pages = convert_from_path(pdf_file,
                                  resolution,
                                  poppler_path=bin_path,
                                  first_page=pages_,
                                  last_page=min(pages_ + 10 - 1, max_pages))

        for page in pages:
            filename = "page_" + str(image_counter) + ".jpg"

            # To save
            image_path = tender_jpg_dir + "/" + filename
            page.save(image_path, 'JPEG')
            # Creating a text file to write the output
            outfile = tender_jpg_dir + "/" + "page_" + str(image_counter) + ".txt"
            f = open(outfile, "a")
            text = str((pytesseract.image_to_string(Image.open(image_path))))
            text = text.replace('-\n', '')
            f.write(text)
            f.close()

            image_counter += 1

            os.remove(image_path)


def convert_documents_to_txt(path: str = "../data/Soportes",
                             resolution: int = 500):
    documents = documents_data_frame(path=path)

    for index in range(documents.shape[0]):
        temp = documents[documents.index == index]
        tender_id = int(temp.TENDER_ID.values[0])
        document_id = int(temp.DOCUMENT_ID.values[0])
        file_name = temp.FILE_NAME.values[0]

        pdf_file = r"{}/{}/{}".format(path, tender_id, file_name)

        pdf_to_txt(pdf_path=pdf_file,
                   tender_id=tender_id,
                   document_id=document_id,
                   path=path,
                   resolution=resolution)

