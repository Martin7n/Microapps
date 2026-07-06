import re

from esg_vehicles.brand_model import brand_model_extraction
from esg_vehicles.data_id import BADGE_PATTERN, BRAND_ALIASES
from esg_vehicles.fuel_check import  classify_fuel
from esg_vehicles.weight_check import weight_normalization, classify_by_weight


def car_data(vin, model, brand, description, weight, measure_unit):
    weight = weight_normalization(weight, measure_unit)
    model, brand, description, measure_unit = model.lower(), brand.lower(), description.lower(), measure_unit.lower()
    vehicle_category = classify_by_weight(weight)
    # fuel = fuel_check(description)
    fuel = classify_fuel(description)

    updated_brand = brand_model_extraction(brand, model, description)


    car = {
        "appendix": appendix,
        "vin": vin,
        "brand_raw": brand,
        "model_raw": model,
        "description": description,
        "weight": weight,
        "measure_unit_kg": "kg",
        "vehicle_category": vehicle_category,
        "fuel": fuel,
    }
    return car

def all_in_one(appendix, brand, model, description, weight, measure_unit, asset_type, vin):
    vehicle_info = car_data(vin,brand, model, description, weight, measure_unit)
    print(vehicle_info)



if __name__ == '__main__':
    appendix = "0012353ZZ"
    brand = "Audi"
    model = "A4 2.0 TDI quattro"
    weight = "2500.00"
    measure_unit = "T"
    description = "Audi A4 2.0 tfsi  quattro"
    asset_type = "Truck, ..."
    vin = "WNDB..."
    all_in_one(appendix, brand, model, description, weight, measure_unit, asset_type, vin)

    # brand_model_extraction(brand, model, description, weight)