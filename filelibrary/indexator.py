import os
import openpyxl

def file_index(path_to_dir, filetypes:bool):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(row=1, column=1).value = "Path"
    sheet.cell(row=1, column=2).value = "Full Path"
    sheet.cell(row=1, column=3).value = "Name"
    sheet.cell(row=1, column=4).value = "Size"
    sheet.cell(row=1, column=5).value = "Type"
    sheet.cell(row=1, column=6).value = "Direct link"
    wb.save('files_found.xlsx')

    files_in_directory = os.listdir(path_to_dir)
    count = 0
    for path, subdirs, files in os.walk(path_to_dir):
        for row, name in enumerate(files, start=2):
            found = os.path.join(path, name)
            size = os.path.getsize(found)
            created =   os.path.getctime(found)
            type = f"<{name.split(".")[-1]}>"
            docs_and_others = ["pdf", "doc", "docx", "jpg", "jpeg", "png", "gif", "webp", "xls", "xlsx", "eml"]

            if not filetypes:
                if name.split(".")[-1] in docs_and_others:
                    sheet.cell(row=row, column=1).value = path
                    sheet.cell(row=row, column=2).value = found
                    sheet.cell(row=row, column=3).value = name
                    sheet.cell(row=row, column=4).value = size
                    sheet.cell(row=row, column=5).value = type
                    sheet.cell(row=row, column=6).value = name
                    sheet.cell(row=row, column=6).hyperlink = found
                    sheet.cell(row=row, column=6).style = "Hyperlink"
                    count += 1
            else:
                sheet.cell(row=row, column=1).value = path
                sheet.cell(row=row, column=2).value = found
                sheet.cell(row=row, column=3).value = name
                sheet.cell(row=row, column=4).value = size
                sheet.cell(row=row, column=5).value = type
                sheet.cell(row=row, column=6).value = name
                sheet.cell(row=row, column=6).hyperlink = found
                sheet.cell(row=row, column=6).style = "Hyperlink"
                count += 1


    wb.save('files_found.xlsx')
    wb.close()
    return count


def file_writer(path, found, name, size, type):
    pass

if __name__ == '__main__':
    pass
