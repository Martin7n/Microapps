import os
from pprint import pprint
import FreeSimpleGUI as sg
import openpyxl
from openpyxl import Workbook

def file_rename(filepaths,  reg_file):

    try:

        files_in_directory = os.listdir(filepaths)
        reg_file = reg_file
        wb_obj = openpyxl.load_workbook(reg_file)
        sheet_obj = wb_obj.active
        max_row = sheet_obj.max_row
        register = {}
        for row in sheet_obj.iter_rows(min_row=2, max_col=4, max_row=max_row):
            # appendix = str(row[0].value) + row[1].value + str(row[2].value)
            appendix = str(row[1].value)
            reg = row[3].value
            register[reg] = appendix

        names = []
        for file in files_in_directory:
            names.append(file)

        count = 0
        #updated for short regs
        for name in names:
            search_pattern = name[:8]
            if search_pattern[-1]=="_":
                search_pattern= search_pattern[:7]
                # print(search_pattern)
                if search_pattern in register:
                    new_name = register[search_pattern] + "_" + name
                    count += 1
                    # print(new_name)
                    # old_file = os.path.join(directory_path, name)
                    # new_file = os.path.join(directory_path, new_name)

                    old_file = filepaths + "//" + name
                    new_file = filepaths + "//" + new_name

                    os.rename(old_file, new_file)
                    with open("work_done.txt", "a") as file:
                        file.writelines(f"{name}, {new_name}")
        return count
    except Exception:
        exit()


if __name__ == "__main__":
    pass














