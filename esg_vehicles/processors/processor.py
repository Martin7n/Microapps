from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_extraction import test1
from esg_vehicles.processors.brand_model import extract_brand, extract_model, brand_model
from esg_vehicles.processors.category_check import  category_handler


def process_records(records:[ESGRecord], type_processing):
    if type_processing == "esg_main":
        # test1(records)
        count = 0
        for record in records:

            record.detected_weight = category_handler(record)
            record.weight_measure_update = "kg"

            description_brand_model = [record.equipment, record.brand, record.model]
            [new_brand, new_model] = brand_model(description_brand_model)
            if new_brand:
                record.detected_manufacturer = new_brand

    else:
        print(records)


if __name__ == '__main__':
    pass