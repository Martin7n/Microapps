from esg_vehicles.processors.brand_extraction import test1


def process_records(records, type_processing):
    if type_processing == "esg_main":
        test1(records)
    else:
        print(records)

    return records


if __name__ == '__main__':
    pass