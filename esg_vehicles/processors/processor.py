from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.brand_extraction import test1
from esg_vehicles.processors.brand_model import extract_brand, extract_model, brand_model
from esg_vehicles.processors.category_check import  category_handler
from esg_vehicles.processors.fuel_check import check_for_fuel


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
            updated_fuel_cat = check_for_fuel(record.equipment)
            record.detected_fuel = updated_fuel_cat

    else:
        print(records)


if __name__ == '__main__':
    pass