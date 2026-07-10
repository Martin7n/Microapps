from esg_vehicles.data_collections.data_id import VEHICLE_WEIGHT_CLASSES
from esg_vehicles.data_collections.data_id2 import LCV_VIN, HGV_VIN, CAR_VIN, MEDDUTYTRUCK
from esg_vehicles.data_collections.data_id4 import CATEGORIES_BY_SOURCE, MAIN_CATEGORIES
from esg_vehicles.processors.data_helpers import text_normalization

from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.weight_check import weight_normalization


#1st stage

def category_handler(record: ESGRecord):
    eq_type = record.equipment_type
    eq_vin = record.vin
    eq_description = record.equipment
    eq_weight = record.weight
    eq_weight_measure = record.weight_measure

    check_by_exact_type = ""
    if eq_type is not None and eq_type!="-":
        check_by_exact_type = category_check_by_type_id_match(eq_type)
    if eq_weight is not None and eq_weight!="-":
        weight = weight_normalization(eq_weight, eq_weight_measure)
        record.weight_measure_update = "kg"
        record.detected_weight = weight



def category_check_by_type_id_match(eq_type):
    if eq_type in CATEGORIES_BY_SOURCE:
        return CATEGORIES_BY_SOURCE[eq_type]



def category_check_by_type_search(eq_type):
    category_text = text_normalization(eq_type)
    if "Motorcycle" in category_text:
        return MAIN_CATEGORIES["Motorcycle"]
    # if "trailer" in vehicle_type.lower():
    #     return "Trailer"
    if "СЂРµРјР°СЂРєРµ" in category_text:
        return MAIN_CATEGORIES["Trailer"]
    if "semi truck" in category_text:
        return MAIN_CATEGORIES["HvyDutyTruk"]

#2nd stage
def classify_by_weight(weight):
# def classify_by_weight(weight, measure_unit):

    # weight = weight_normalization(weight, measure_unit)
    if weight is None:
        return "unknown"

    for category, (low, high) in VEHICLE_WEIGHT_CLASSES.items():
        if low <= weight <= high:
            return category

    return "unknown"


#3rd stage

def category_check_3rd_stage():
    pass



def check_by_partial_vin(safe_vin):
    vin_partial = safe_vin[:7]
    if vin_partial in LCV_VIN:
        return "LgtComrclVeh"
    if vin_partial in HGV_VIN:
        return "HvyDutyTruk"
    if vin_partial in CAR_VIN:
        return "Car"
    if vin_partial in MEDDUTYTRUCK:
        return "MedDutyTruk"
    return "NoCat"

def check_by_category(text, safe_vin, measure, weight, vehicle_type):
    category_text = text.split(" ")
    category_text = [x.lower() for x in category_text]
    vin_partial = safe_vin[:7]
    if "Motorcycle" in vehicle_type:
        return "Motorcycle"
    if "trailer" in vehicle_type.lower():
        return "Trailer"
    if "СЂРµРјР°СЂРєРµ" in vehicle_type.lower():
        return "Trailer"
    if "semi truck" in vehicle_type.lower():
        return "HvyDutyTruk"
    #None or NoCat
    return "NoCat"

if __name__ == '__main__':
    pass
