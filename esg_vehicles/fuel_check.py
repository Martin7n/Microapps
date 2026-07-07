from esg_vehicles.data_id import DIESEL, PETROL, BADGE_PATTERN, FUEL_SIGNALS


import re


def normalize(text):
    return (text or "").lower().replace(".", " ").replace("-", " ")
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





if __name__ == '__main__':
    data = "aasfd electric diesel lkmsd V6"
    print(classify_fuel(data))