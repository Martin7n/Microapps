from esg_vehicles.data_collections.data_id import BRAND_ALIASES
from esg_vehicles.data_collections.data_id3 import SORTED_BRAND_LOOKUP
from esg_vehicles.processors.data_helpers import keyword_extract_list, text_normalization


def norm(x):
    return (str(x) or "").lower()

def extract_brand(combined_text:[]):
    # strongest signal first
    normalized_text = keyword_extract_list(combined_text)
    for text in normalized_text:
        for alias, canonical in BRAND_ALIASES.items():
            if alias in text:
                return canonical[0]

    return None

def extract_model(text, brand):
    if not brand:
        return None

    text = text_normalization(text)
    text = text.replace(brand.lower(), "")
    #not very useful, too many "parasite words"

    return " ".join(text.split()).strip() or None

def brand_model(brand, model, description):
    text = keyword_extract_list([brand, model, description])
    all_text = " ".join([brand, model, description])
    extracted_brand = extract_brand(text)
    extracted_model = extract_model(all_text, extracted_brand)
    return extracted_brand, extracted_model

def brand_model_extraction(brand, model, description):
    all_text = ",".join([brand,str(model), description])
    # print(all_text)
    BRAND_LOOKUP = {}

    for brand, aliases in BRAND_ALIASES.items():
        for a in aliases:
            BRAND_LOOKUP[a] = brand

    return BRAND_LOOKUP

def brands_t(descriptions):
    res = {}
    for record in descriptions:
        dsc = record.replace(", ", " ")
        data = [str(x.lower()) for x in dsc.split(' ')]
        for rec in data:
            if rec not in res:
                res[rec] = 0
            res[rec] +=1
    # for k, v in res.items():
    #     print(f'{k}-{v}')
    return res


def model_ext(brand, model, description):
    texts = [
        norm(brand),
        norm(model),
        norm(description)
    ]

    for text in texts:
        for alias, canonical in SORTED_BRAND_LOOKUP:
            if alias in text:
                return canonical

    return None

if __name__ == '__main__':
    #test_data
    brand = "Audi"
    model = "A4 2.0 TDI quattro"
    description = "Audi A4 2.0 TDI quattro"

    print(extract_brand([brand, model, description]))
    print(extract_model(description, brand))