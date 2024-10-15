import os

import PyPDF2
import openpyxl
from openpyxl.reader.excel import load_workbook
import re

from patterns import vin_convention_pattern, cert_number_pattern, pattern_reg
from vars import  path_to_file



def registry_convention(reg_file):
    '''convention part - reading the xls register'''
    wb_obj = openpyxl.load_workbook(reg_file)
    sheet_obj = wb_obj.active
    max_row = sheet_obj.max_row
    register = {}
    for row in sheet_obj.iter_rows(min_row=2, max_col=4, max_row=max_row):
        # appendix = str(row[0].value) + row[1].value + str(row[2].value)
        # reg = row[3].value
        appendix, reg, ib = str(row[0].value), row[1].value, str(row[2].value)
        #TODO: ib usage
        register[reg] = appendix

    return register


def ocr_file_renamer(filepaths, reg_file):

    convention_registry = registry_convention(reg_file)
    pdf_registry = {}

    filenames = os.listdir(filepaths)
    names = []

    for file_name in filenames:
        if file_name.endswith(".pdf"):
            names.append(file_name)
            pdf_file_path = filepaths + "/" + file_name
            print(pdf_file_path)

            pdfFileObj = open(pdf_file_path, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            pageObj = pdfReader.pages[0]
            page_text = pageObj.extract_text()
            txt = page_text[200:5000]
            pdfFileObj.close()

            reg_num = re.findall(pattern_reg, txt)
            num_reg_cert = re.findall(cert_number_pattern, txt)
            certificate = re.finditer(cert_number_pattern, txt)
            vin_number = re.findall(vin_convention_pattern, txt[0:(len(txt) - 100)])
            convention_registry[pdf_file_path] = reg_num[0]
            rr = reg_num[0]
            certificate_no = "_".join([x[2] for x in certificate])

            old_file = filepaths + "/" + file_name
            new_file = filepaths + "/" + reg_num[0] + "_" + certificate_no + ".pdf"
            if rr in convention_registry:
                appendix = convention_registry[rr]
                new_file = filepaths + "/" + appendix+ "_" + reg_num[0] + "_" + certificate_no + ".pdf"
            print(new_file, old_file)
            os.rename(old_file, new_file)


    # return f"{filepaths},  {path_to_file}"

if __name__ == '__main__':
    pass
