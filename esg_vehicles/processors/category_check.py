from esg_vehicles.data_collections.data_id2 import LCV_VIN, HGV_VIN, CAR_VIN, MEDDUTYTRUCK
from esg_vehicles.data_collections.categories_vehicles import CATEGORIES_BY_SOURCE, MAIN_CATEGORIES, \
    VEHICLE_WEIGHT_CLASSES
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

    #FIXME - eq_type column is currently off.

    ''''
    
    A) Brand - Models:
        1. extract B&M from brand and model fields (EqAlloc)
        2. extract B&M from brand and model fields (Equipment(description))
        3. extract matched B&M by description
        *** bonus: brand origin / country
        Result: B&M + modification data & id "tokens"
    B) Types/Categories: 
        1. extract labeled category by equipment type(EqAlloc) *** partial match of types.
        2. extract keyword category by description field (kw extract)
        3. if exist: extract weight and measuring units && normalize it.
        4. extract similarities based on VIN and mark/model
        Result:
        [best case: 1 & 1 steps results combined with 3rd block are final ] 
        Fail-safe: 1st step results into Category, buildup with 4th block results.   
    
    C) Fuels-Propulsion (FP)
        1. extract and map by EquipAlloc field /if exists
        2. match with Brand & Model(A) - only EV -> to result. 
        3. extract by Equipment field(description)
        4. extract by VIN
        [fail-safe] by 4.
        Result: fuel/propulsion 
    D) Emission 
        1. By EquipAlloc emission field
        2. By A), B) and C)
        3. By Q2 rep.
        *** bonus - by previous data 
        
        Check missmatch.
        Result:...obvious. 
    
    E) Labels update, UUID 

    *** bonus:
        - DB log
        - TWG metrics
        - DB-check - field per field log with previous data
        - EAA DB implementation - additional layer in A to D, after data cleaning.
        - APC TWG 
    '''

    check_by_exact_type = ""
    if eq_type is not None or eq_type!="-":
        check_by_exact_type = category_check_by_type_id_match(eq_type)
    if eq_weight is not None or eq_weight!="-":
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
