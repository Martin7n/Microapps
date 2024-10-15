import PyPDF2
from openpyxl.reader.excel import load_workbook
import re

from file_feeder import file_read
from patterns import vin_convention_pattern, cert_number_pattern, pattern_reg
from vars import  path_to_file


#ocr, read and write all/optimal data
def pdf_to_excel_min(filelist, excel_file_path):

    for pdf_file_path in filelist:

        pdfFileObj = open(pdf_file_path, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        wb = load_workbook(excel_file_path)
        ws = wb.active

        pageObj = pdfReader.pages[0]
        # page_text = pageObj.extract_text().split('\n')
        page_text = pageObj.extract_text()

        #Scaned-search area limitation
        txt = page_text[200:5000]

        reg_num = re.findall(pattern_reg, txt)
        num_reg_cert = re.findall(cert_number_pattern, txt)
        certificate = re.finditer(cert_number_pattern, txt)

        vin_number = re.findall(vin_convention_pattern, txt[0:(len(txt) - 100)])
        print(reg_num, num_reg_cert, vin_number)

        certificate_no = [x[2] for x in certificate]

        list_item = [f"{reg_num}"] + [f"{certificate_no}"] + [f"{vin_number}"]
        ws.append(list_item)

    # All info, reg, vin and etc.

    # for item in txt.split('\n'):
    #     list_item = [item] + [f"{reg_num}"] + [f"{num_reg_cert}"] + [f"{shassi}"]
    #     ws.append(list_item)
    #     if len(item) <=40:
    #         list_item = [item]+[f"{reg_num}"]+[f"{num_reg_cert}"] + [f"{shassi}"]
    #         # list_item = [f"{reg_num}"]+[f"{num_reg_cert}"] + [f"{shassi}"]
    #         ws.append(list_item)
    #
        wb.save(filename=excel_file_path)


if __name__ == "__main__":
    filelist = file_read()
    pdf_to_excel_min(filelist, path_to_file)