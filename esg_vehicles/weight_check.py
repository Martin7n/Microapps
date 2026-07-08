from esg_vehicles.data_id import VEHICLE_WEIGHT_CLASSES
from esg_vehicles.data_id2 import LCV_VIN, HGV_VIN, CAR_VIN, MEDDUTYTRUCK


def weight_normalization(weight, unit):
    if weight in [None, "", "-"]:
        return None

    if unit in [None, "", "-"]:
        unit = "kg"

    try:
        weight = float(str(weight).replace(",", "."))
    except (TypeError, ValueError):
        return None

    unit = unit.lower().strip()
    if unit.lower() == "t":
        weight = weight * 1000
    elif unit == "kg":
        pass

    else:
        return None

    if weight < 500:
        weight = weight * 1000
    elif weight > 85000:
        weight = weight / 1000

    return round(weight, 1)


def classify_by_weight(weight):
# def classify_by_weight(weight, measure_unit):

    # weight = weight_normalization(weight, measure_unit)
    if weight is None:
        return "unknown"

    for category, (low, high) in VEHICLE_WEIGHT_CLASSES.items():
        if low <= weight <= high:
            return category

    return "unknown"



def check_by_partial_vin(safe_vin):
    vin_partial = safe_vin[:7]
    if vin_partial in LCV_VIN:
        return "LgtComrclVeh"
    if vin_partial in HGV_VIN:
        return "HvyDutyTruk"
    if vin_partial in CAR_VIN:
        return "Car"
    if vin_partial in MEDDUTYTRUCK:
        return "MedDutyTruck"
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