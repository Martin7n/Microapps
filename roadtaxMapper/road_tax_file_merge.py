import os
import openpyxl

def file_index(filepaths, types:False, all_types:False):
    count = 0
    for path, subdirs, files in os.walk(filepaths):
        for name in files:
            if name.endswith('.xlsx'):
                count+=1
                found = os.path.join(path, name)
                print(found)
                wb_obj = openpyxl.load_workbook(found)
                sheet_obj = wb_obj.active
                max_row = sheet_obj.max_row

                if types and name.startswith('Obliga'):
                    result_name = 'obligation_found.xlsx'
                    maximum_col = 40
                elif name.startswith('DPS_'):
                    result_name = 'dps_found.xlsx'
                    maximum_col = 32

                else:
                    result_name = "files_found.xlsx"
                    maximum_col = 50

                wb = openpyxl.load_workbook(result_name)
                sheet = wb.active

                for row in sheet_obj.iter_rows(min_row=1, max_col=maximum_col, max_row=max_row):
                    # appendix = str(row[0].value) + row[1].value + str(row[2].value)
                    if row[0].value is not None:
                        # print(row[0].value)
                        inf = [x.value for x in row]
                        inf.append(name)
                        inf.append(found)
                        sheet.append(inf)
                wb.save(result_name)

    return count



if __name__ == '__main__':
    print(file_index("c:\\drob\\", False, False))
    # print(walker_xlsx("c:\\drob\\"))



