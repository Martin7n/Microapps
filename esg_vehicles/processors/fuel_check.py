from esg_vehicles.data_collections.data_id2 import ELECTRIC_VINS
from esg_vehicles.data_collections.fuels_propulsions.ev import ELECTRIC_KEYWORDS
from esg_vehicles.data_collections.fuels_propulsions.fuel_propulsion import HYBRID_KWORDS, TECHNOLOGY_FUEL_MAP, BEV_MODELS, HYBRID_MODELS, \
    FUEL_SIGNALS,  PETROL_KEYWORDS, GAS_KEYWORDS, \
    DIESEL_KEYWORDS, HYBRID_KEYWORDS
from esg_vehicles.processors.data_helpers import keywords_list_exraction_desc


def normalize(text):
    return (text or "").lower().replace(".", " ").replace("-", " ")

#Todo test the different variants with at least 5k
def get_fuel_type(brand, technology):
    fuel1 = HYBRID_KWORDS.get(("toyota", "hybrid synergy drive"))
    fuel2 = TECHNOLOGY_FUEL_MAP.get(brand, {}).get(technology)

    return TECHNOLOGY_FUEL_MAP.get(brand, {}).get(technology)

def detect_fuel(model_name):
    model = model_name.lower()

    if any(x in model for x in BEV_MODELS):
        return "bev"

    if any(x in model for x in HYBRID_MODELS):
        return "hybrid"

    if any(x in model for x in DIESEL_KEYWORDS):
        return "diesel"

    return None


def find_fuel_signals(text):
    text = normalize(text)
    words = set(text.split())

    signals = set()

    for fuel, keywords in FUEL_SIGNALS.items():
        for k in keywords:
            if k in words:   # SAFE exact match
                signals.add(fuel)
                break

    return signals

def classify_fuel(text):
    signals = find_fuel_signals(text)
    # print(signals)
    # return reduce_signals(signals)
    if "electric" in signals:
        if "petrol" in signals or "diesel" in signals:
            return "hybrid"
        return "electric"

    if "hybrid" in signals:
        return "hybrid"

    if "diesel" in signals:
        return "diesel"

    if "petrol" in signals:
        return "petrol"

    return "unknown"


# def classify_fuel_by_key(text):
#     text = (text or "").lower()
#
#     for fuel_type, keywords in FUEL_SIGNALS.items():
#         if any(k in text for k in keywords):
#             return fuel_type
#
#     return "unknown"



def check_for_fuel(check_for_fuel:list):
    normalized_text = keywords_list_exraction_desc(check_for_fuel)

    for word in normalized_text:
        if word in PETROL_KEYWORDS:
            return "petrol"
        if word in HYBRID_KEYWORDS:
            return "hybrid"
        if word in DIESEL_KEYWORDS:
            return "diesel"
        if word in GAS_KEYWORDS:
            return "gas/alternative"

        # if word in ELECTRIC_VINS:
        #     return "EV"
        # if word in ELECTRIC_KEYWORDS:
        #     return  "EV"
        # if word in ELECTRIC_CODES:
        #     return "EV"
        # if word in ELECTRIC_BRANDS:

            # return "EV"

    return f"no fuel ide"


def check_for_fuel_rev(check_for_fuel:list):
    normalized_text = keywords_list_exraction_desc(check_for_fuel)
    full_text_string = " " + " ".join(normalized_text) + " "

    if any(f" {keyword} " in full_text_string for keyword in ELECTRIC_KEYWORDS):
        return "ev"
    if any(f" {keyword} " in full_text_string for keyword in HYBRID_KEYWORDS):
        return "hybrid"
    if any(f" {keyword} " in full_text_string for keyword in PETROL_KEYWORDS):
        return "petrol"
    if any(f" {keyword} " in full_text_string for keyword in DIESEL_KEYWORDS):
        return "diesel"

        #
        #
        # if word in GAS_KEYWORDS:
        #     return "gas/alternative"
        #
        # if word in ELECTRIC_VINS:
        #     return "EV"
        # if word in ELECTRIC_KEYWORDS:
        #     return  "EV"
        # if word in ELECTRIC_CODES:
        #     return "EV"
        # if word in ELECTRIC_BRANDS:
        #
        #     return "EV"

    return f"no fuel ide"



if __name__ == '__main__':
    data = "aasfd electric diesel lkmsd V6"
    print(classify_fuel(data))