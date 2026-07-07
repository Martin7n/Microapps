from esg_vehicles.data_id import VEHICLE_WEIGHT_CLASSES


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