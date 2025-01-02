import os
import openpyxl

def file_index(path_to_dir):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(row=1, column=1).value = "Path"
    sheet.cell(row=1, column=2).value = "Full Path"
    sheet.cell(row=1, column=3).value = "Name"
    sheet.cell(row=1, column=4).value = "Size"
    sheet.cell(row=1, column=5).value = "Type"


    wb.save('files_found.xlsx')


    files_in_directory = os.listdir(path_to_dir)
    count = 0
    for path, subdirs, files in os.walk(path_to_dir):
        for row, name in enumerate(files, start=2):
            found = os.path.join(path, name)
            size = os.path.getsize(found)
            created =   os.path.getctime(found)
            type = f"<{name.split(".")[-1]}>"
            sheet.cell(row=row, column=1).value = path
            sheet.cell(row=row, column=2).value = found
            sheet.cell(row=row, column=3).value = name
            sheet.cell(row=row, column=4).value = size
            sheet.cell(row=row, column=5).value = type
            count += 1

    wb.save('files_found.xlsx')
    wb.close()
    return count


if __name__ == '__main__':
    print(file_index('C:\\Users\\'))

