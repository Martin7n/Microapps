import re

from esg_vehicles.brand_model import brand_model_extraction, extract_brand
from esg_vehicles.fuel_check import  classify_fuel
from esg_vehicles.weight_check import weight_normalization, classify_by_weight


def car_data(vin, model, brand, description, weight, measure_unit):
    updated_weight = weight_normalization(weight, measure_unit)
    model, brand, description, measure_unit = model.lower(), brand.lower(), description.lower(), measure_unit.lower()
    updated_vehicle_category = classify_by_weight(weight)


    updated_brand = brand_model_extraction(brand, model, description)

    return updated_weight, updated_brand, updated_vehicle_category


def object_data_update(obj):
    for key, val in obj.items():
        if isinstance(val, str):
            val = val.lower()
    obj["u_weight"] = weight_normalization(obj["weight"], obj["measure_unit"])
    obj["u_vehicle_category"] = classify_by_weight(obj["u_weight"])
    obj["u_fuel"] = classify_fuel(obj["description"])
    obj["u_brand"] = extract_brand(obj["brand"], obj["model"], obj["description"])
    # obj["u_model"] = extract_model(obj["description"], obj["u_brand"])

    # obj["u_brand"], obj["u_model"] = brand_model_extraction(obj["brand"], obj["model"], obj["description"])

    print(obj)

if __name__ == '__main__':
    pass
    # brand_model_extraction(brand, model, description, weight)