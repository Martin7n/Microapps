from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_extraction import test1
from esg_vehicles.processors.category_check import  category_handler


def process_records(records:[ESGRecord], type_processing):
    if type_processing == "esg_main":
        # test1(records)
        for record in records:
            category_handler(record)
    else:
        print(records)


if __name__ == '__main__':
    pass