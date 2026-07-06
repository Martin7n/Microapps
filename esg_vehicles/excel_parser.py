import os
import openpyxl

from csv_eea_co.eaa_data_handler import field_list


def xls_parse(file):

    wb = openpyxl.load_workbook(file)
    ws = wb.active
    interval = 10

    car_objects = {}

    for row in ws.iter_rows(min_row=2,
            max_row=ws.max_row,
            # max_row = interval,
            min_col=1,
            max_col=ws.max_column, values_only=True,
    ):
        brand = row[1]
        model = row[2]
        emission = row[3]
        fuel = row[5]
        category = row[7]
        if brand and model and emission and fuel and category:
            mark_model = f"{brand.lower()} {str(model).lower().replace('/', '_').strip()}"
            print(mark_model)
            if mark_model not in car_objects:
                car_objects[mark_model] = []
            car_objects[mark_model].append(fuel)

    # print(car_objects)
    for k,v in car_objects.items():
        print(k, v, len(v))



def data_collection(data):
    pass


def xls_writer(data):
    output_wb = openpyxl.Workbook()
    output_ws = output_wb.active
    output_ws.title = "Results"

    output_wb.save("output.xlsx")


if __name__ == '__main__':
    xls_parse(r"C:\drob\ress.xlsx")