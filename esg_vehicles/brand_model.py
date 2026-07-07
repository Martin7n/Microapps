from esg_vehicles.data_id import BRAND_ALIASES, BADGE_PATTERN


def norm(x):
    return (str(x) or "").lower()

def extract_brand(brand, model, description):
    texts = [norm(brand),norm(model),norm(description)]

    # strongest signal first
    for text in texts:
        for alias, canonical in BRAND_ALIASES.items():
            if alias in text:
                return canonical[0]

    return None

def extract_model(text, brand):
    if not brand:
        return None

    text = text.lower()
    text = text.replace(brand.lower(), "")

    return " ".join(text.split()).strip() or None

def brand_model(brand, model, description):
    text = " ".join([brand, model, description]).lower()
    extracted_brand = extract_brand(text)
    extracted_model = extract_model(text, extracted_brand)
    return extracted_brand, extracted_model

def brand_model_extraction(brand, model, description):
    all_text = ",".join([brand,str(model), description])
    # print(all_text)
    BRAND_LOOKUP = {}

    for brand, aliases in BRAND_ALIASES.items():
        for a in aliases:
            BRAND_LOOKUP[a] = brand

    return BRAND_LOOKUP



if __name__ == '__main__':
    #test_data
    brand = "Audi"
    model = "A4 2.0 TDI quattro"
    description = "Audi A4 2.0 TDI quattro"

    print(extract_brand(brand, model, description))
    print(extract_model(description, brand))