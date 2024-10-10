from pprint import pprint

from patterns import *
from PyPDF2 import PdfReader
import re
import json

import pandas as pd

from vars import paths_to_pdf, path_to_file

def pdf_to_excel(pdf_file_path, excel_file_path):
    reader = PdfReader(pdf_file_path)
    page = reader.pages[0]
    text_origin = page.extract_text()
    total_length = len(text_origin)
    short = total_length-50
    text = text_origin[30:short]

    reg_check = re.findall(pattern_reg, text)
    vin_1_check = re.findall(reg_pattern2, text)
    vin_2_check = re.findall(pattern3, text)
    vin_3_check = re.findall(pattern4, text)
    vin_4_check = re.findall(vin_convention_pattern, text)

    print(f"{reg_check}, {vin_4_check} ")

    result = {
        pdf_file_path:[reg_check, vin_1_check,vin_3_check, vin_4_check]
    }
    test_result = []
    test_result.append(result)

    with open("new.txt", "a") as file:
        file.writelines(text)
    with open("matched.txt", "a") as file:
        file.write(json.dumps(test_result))
    print(text)
 


if __name__ == "__main__":
    for pdf_file_path in paths_to_pdf:
        pdf_to_excel(pdf_file_path, path_to_file)



