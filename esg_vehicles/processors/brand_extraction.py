from esg_vehicles.models.main_class import ESGRecord


def test1(ss:list[ESGRecord]):
    cleaned_brand = None
    cleaned_weight = None

    for obj in ss:
        print(obj.equipment_id)


# def extract_brand(record: ESGRecord):
#
#     if record.brand:
#         record.detected_brand = record.brand.upper()
#     else:
#         record.errors.append("Brand missing")
#
#     return record


if __name__ == "__main__":
    pass