from esg_vehicles.data_collections.brand_models import SORTED_BRAND_LOOKUP, BRAND_ALIASES
from esg_vehicles.models.main_class import ESGRecord
from esg_vehicles.processors.data_helpers import keyword_extract_list, text_normalization, keywords_list_exraction_desc


def norm(x):
    return (str(x) or "").lower()

def extract_brand(description_brand_model:list):


    # strongest signal first
    normalized_text = keywords_list_exraction_desc(description_brand_model)
    normalized_text2 = keyword_extract_list(description_brand_model)
    for text in normalized_text:
        for alias, canonical in BRAND_ALIASES.items():
            if alias in text:
                # print(normalized_text, canonical[0])
                return canonical[0]
            if text in canonical:
                return  canonical[0]
    for text in normalized_text2:
        for alias, canonical in BRAND_ALIASES.items():
            if alias in text:
                # print(normalized_text, canonical[0])
                return canonical[0]


    # print(normalized_text)
    return None

def extract_model(text, brand):
    if not brand:
        return None

    text = text_normalization(text)
    text = text.replace(brand.lower(), "")
    #not very useful, too many "parasite words"

    return " ".join(text.split()).strip() or None

def brand_model(description_brand_model:list):
    text = keyword_extract_list(description_brand_model)
    all_text = " ".join([str(x) for x in description_brand_model])
    extracted_brand = extract_brand(text)
    extracted_model = extract_model(all_text, extracted_brand)
    return extracted_brand, extracted_model

def brand_model_extraction(description_brand_model:list):
    all_text = ",".join([str(x) for x in description_brand_model])
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

    # print(extract_brand([brand, model, description]))
    print(extract_model(description, brand))