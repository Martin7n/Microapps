import tabula
from vars import path_to_file, paths_to_pdf

#preview only
def pdf_to_excel(pdf_file_path, excel_file_path):
    tables = tabula.read_pdf(pdf_file_path, pages="all", multiple_tables=True)
    print(tables)




if __name__ == "__main__":
    for pdf_file_path in paths_to_pdf:
        pdf_to_excel(pdf_file_path, path_to_file)