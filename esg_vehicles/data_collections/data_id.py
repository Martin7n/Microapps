import re

BRAND_ALIASES = {
    "bmw": ["bmw", "бмв"],
    "audi": ["audi", "ауди"],
    "mercedes-benz": ["mercedes-benz", "mercedes", "мерцедес", "мерцедес-бенц"],
    "volkswagen": ["volkswagen", "vw", "фолксваген", "фв"],
    "skoda": ["skoda", "škoda", "шкода"],
    "peugeot": ["peugeot", "пежо"],
    "renault": ["renault", "рено"],
    "citroen": ["citroen", "citröen", "ситроен"],
    "opel": ["opel", "опел"],
    "ford": ["ford", "форд"],
    "toyota": ["toyota", "тоyота"],
    "nissan": ["nissan", "нисан"],
    "hyundai": ["hyundai", "хюндай", "hyunday"],
    "kia": ["kia", "киа"],
    "mazda": ["mazda", "мазда"],
    "honda": ["honda", "хонда"],
    "fiat": ["fiat", "фиат"],
    "alfa romeo": ["alfa romeo", "алфа ромео"],
    "volvo": ["volvo", "вольво"],
    "seat": ["seat", "сеат"],
    "cupra": ["cupra", "купрa"],
    "tesla": ["tesla", "тесла"],
    "byd": ["byd", "бийд"],
}


ev_models_dict = [
    # Abarth
    "Abarth 500e",

    # Acura
    "Acura ZDX",

    # Alfa Romeo
    "Alfa Romeo Junior Elettrica",

    # Audi
    "Audi e-tron",
    "Audi e-tron GT",
    "Audi Q4 e-tron",
    "Audi Q6 e-tron",
    "Audi Q8 e-tron",
    "Audi SQ6 e-tron",
    "Audi SQ8 e-tron",
    "Audi RS e-tron GT",
    "Audi A6 e-tron",

    # BMW
    "BMW i3",
    "BMW i4",
    "BMW i5",
    "BMW i7",
    "BMW iX",
    "BMW iX1",
    "BMW iX2",

    # BYD
    "BYD Atto 2",
    "BYD Atto 3",
    "BYD Dolphin",
    "BYD Dolphin Mini",
    "BYD Han",
    "BYD Seal",
    "BYD Seal U",
    "BYD Sealion 7",
    "BYD Tang",
    "BYD Yuan Plus",
    "BYD Seagull",
    "BYD Qin EV",
    "BYD Song Plus EV",

    # Cadillac
    "Cadillac Lyriq",
    "Cadillac Celestiq",
    "Cadillac Escalade IQ",
    "Cadillac Optiq",
    "Cadillac Vistiq",

    # Chevrolet
    "Chevrolet Bolt EV",
    "Chevrolet Bolt EUV",
    "Chevrolet Blazer EV",
    "Chevrolet Equinox EV",
    "Chevrolet Silverado EV",

    # Citroen
    "Citroen e-C3",
    "Citroen e-C3 Aircross",
    "Citroen e-C4",
    "Citroen e-C4 X",
    "Citroen e-Berlingo",
    "Citroen e-SpaceTourer",

    # Cupra
    "Cupra Born",
    "Cupra Tavascan",

    # Dacia
    "Dacia Spring",

    # Dodge
    "Dodge Charger Daytona EV",

    # Fiat
    "Fiat 500e",
    "Fiat 600e",

    # Fisker
    "Fisker Ocean",

    # Ford
    "Ford Mustang Mach-E",
    "Ford Explorer EV",
    "Ford Capri EV",
    "Ford F-150 Lightning",
    "Ford E-Transit",

    # Genesis
    "Genesis GV60",
    "Genesis Electrified G80",
    "Genesis Electrified GV70",

    # GMC
    "GMC Hummer EV Pickup",
    "GMC Hummer EV SUV",
    "GMC Sierra EV",

    # Honda
    "Honda Prologue",
    "Honda e",
    "Honda N-Van e",

    # Hyundai
    "Hyundai Ioniq Electric",
    "Hyundai Ioniq 5",
    "Hyundai Ioniq 6",
    "Hyundai Kona Electric",
    "Hyundai Inster",
    "Hyundai Casper Electric",

    # Jeep
    "Jeep Wagoneer S",
    "Jeep Avenger Electric",

    # Kia
    "Kia EV3",
    "Kia EV4",
    "Kia EV5",
    "Kia EV6",
    "Kia EV9",
    "Kia Niro EV",
    "Kia Soul EV",

    # Lexus
    "Lexus RZ",

    # Lotus
    "Lotus Eletre",
    "Lotus Emeya",

    # Lucid
    "Lucid Air",
    "Lucid Gravity",

    # Maserati
    "Maserati GranTurismo Folgore",
    "Maserati Grecale Folgore",
    "Maserati GranCabrio Folgore",

    # Mazda
    "Mazda MX-30 EV",
    "Mazda EZ-6 EV",

    # Mercedes-Benz
    "Mercedes-Benz EQA",
    "Mercedes-Benz EQB",
    "Mercedes-Benz EQE",
    "Mercedes-Benz EQE SUV",
    "Mercedes-Benz EQS",
    "Mercedes-Benz EQS SUV",
    "Mercedes-Benz G 580 with EQ Technology",
    "Mercedes-Benz eSprinter",

    # MG
    "MG4",
    "MG5 EV",
    "MG ZS EV",
    "MG Cyberster",
    "MG Marvel R",

    # Mini
    "Mini Cooper Electric",
    "Mini Aceman",
    "Mini Countryman Electric",

    # Nissan
    "Nissan Leaf",
    "Nissan Ariya",

    # Opel / Vauxhall
    "Opel Corsa Electric",
    "Opel Astra Electric",
    "Opel Mokka Electric",
    "Opel Frontera Electric",
    "Opel Grandland Electric",

    # Peugeot
    "Peugeot e-208",
    "Peugeot e-2008",
    "Peugeot e-308",
    "Peugeot e-3008",
    "Peugeot e-408",
    "Peugeot e-5008",
    "Peugeot e-Rifter",

    # Polestar
    "Polestar 2",
    "Polestar 3",
    "Polestar 4",
    "Porsche Taycan",
    "Porsche Macan Electric",

    # Renault
    "Renault Zoe",
    "Renault Megane E-Tech Electric",
    "Renault Scenic E-Tech Electric",
    "Renault 5 E-Tech",
    "Renault 4 E-Tech",
    "Renault Twingo Electric",

    # Rivian
    "Rivian R1T",
    "Rivian R1S",
    "Rivian R2",
    "Rivian R3",
    "Rivian R3X",

    # Rolls-Royce
    "Rolls-Royce Spectre",

    # Skoda
    "Skoda Citigo-e iV",
    "Skoda Enyaq",
    "Skoda Elroq",

    # Smart
    "Smart #1",
    "Smart #3",
    "Smart #5",

    # Subaru
    "Subaru Solterra",

    # Tesla
    "Tesla Roadster",
    "Tesla Model S",
    "Tesla Model 3",
    "Tesla Model X",
    "Tesla Model Y",
    "Tesla Cybertruck",
    "Tesla Semi",

    # Toyota
    "Toyota bZ4X",
    "Toyota Urban Cruiser EV",
    "Toyota C-HR+",

    # Volkswagen
    "Volkswagen ID.3",
    "Volkswagen ID.4",
    "Volkswagen ID.5",
    "Volkswagen ID.6",
    "Volkswagen ID.7",
    "Volkswagen ID. Buzz",
    "Volkswagen e-Golf",
    "Volkswagen e-Up!",

    # Volvo
    "Volvo EX30",
    "Volvo EX40",
    "Volvo EC40",
    "Volvo EX90",
    "Volvo EM90",

    # XPeng
    "XPeng G6",
    "XPeng G9",
    "XPeng P5",
    "XPeng P7",
    "XPeng X9",

    # Zeekr
    "Zeekr 001",
    "Zeekr 007",
    "Zeekr X",
    "Zeekr 009",
    "Zeekr 7X"
]


ev_models = {
    "Abarth": [
        "500e"
    ],
    "Acura": [
        "ZDX"
    ],
    "Alfa Romeo": [
        "Junior Elettrica"
    ],
    "Audi": [
        "e-tron",
        "e-tron GT",
        "Q4 e-tron",
        "Q6 e-tron",
        "Q8 e-tron",
        "SQ6 e-tron",
        "SQ8 e-tron",
        "RS e-tron GT",
        "A6 e-tron"
    ],
    "BMW": [
        "i3",
        "i4",
        "i5",
        "i7",
        "iX",
        "iX1",
        "iX2"
    ],
    "BYD": [
        "Atto 2",
        "Atto 3",
        "Dolphin",
        "Dolphin Mini",
        "Han",
        "Seal",
        "Seal U",
        "Sealion 7",
        "Tang",
        "Yuan Plus",
        "Seagull",
        "Qin EV",
        "Song Plus EV"
    ],
    "Cadillac": [
        "Lyriq",
        "Celestiq",
        "Escalade IQ",
        "Optiq",
        "Vistiq"
    ],
    "Chevrolet": [
        "Bolt EV",
        "Bolt EUV",
        "Blazer EV",
        "Equinox EV",
        "Silverado EV"
    ],
    "Citroen": [
        "e-C3",
        "e-C3 Aircross",
        "e-C4",
        "e-C4 X",
        "e-Berlingo",
        "e-SpaceTourer"
    ],
    "Cupra": [
        "Born",
        "Tavascan"
    ],
    "Dacia": [
        "Spring"
    ],
    "Dodge": [
        "Charger Daytona EV"
    ],
    "Fiat": [
        "500e",
        "600e"
    ],
    "Fisker": [
        "Ocean"
    ],
    "Ford": [
        "Mustang Mach-E",
        "Explorer EV",
        "Capri EV",
        "F-150 Lightning",
        "E-Transit"
    ],
    "Genesis": [
        "GV60",
        "Electrified G80",
        "Electrified GV70"
    ],
    "GMC": [
        "Hummer EV Pickup",
        "Hummer EV SUV",
        "Sierra EV"
    ],
    "Honda": [
        "Prologue",
        "e",
        "N-Van e"
    ],
    "Hyundai": [
        "Ioniq Electric",
        "Ioniq 5",
        "Ioniq 6",
        "Kona Electric",
        "Inster",
        "Casper Electric"
    ],
    "Jeep": [
        "Wagoneer S",
        "Avenger Electric"
    ],
    "Kia": [
        "EV3",
        "EV4",
        "EV5",
        "EV6",
        "EV9",
        "Niro EV",
        "Soul EV"
    ],
    "Lexus": [
        "RZ"
    ],
    "Lotus": [
        "Eletre",
        "Emeya"
    ],
    "Lucid": [
        "Air",
        "Gravity"
    ],
    "Maserati": [
        "GranTurismo Folgore",
        "Grecale Folgore",
        "GranCabrio Folgore"
    ],
    "Mazda": [
        "MX-30 EV",
        "EZ-6 EV"
    ],
    "Mercedes-Benz": [
        "EQA",
        "EQB",
        "EQE",
        "EQE SUV",
        "EQS",
        "EQS SUV",
        "G 580 with EQ Technology",
        "eSprinter"
    ],
    "MG": [
        "MG4",
        "MG5 EV",
        "ZS EV",
        "Cyberster",
        "Marvel R"
    ],
    "Mini": [
        "Cooper Electric",
        "Aceman",
        "Countryman Electric"
    ],
    "Nissan": [
        "Leaf",
        "Ariya"
    ],
    "Opel": [
        "Corsa Electric",
        "Astra Electric",
        "Mokka Electric",
        "Frontera Electric",
        "Grandland Electric"
    ],
    "Peugeot": [
        "e-208",
        "e-2008",
        "e-308",
        "e-3008",
        "e-408",
        "e-5008",
        "e-Rifter"
    ],
    "Polestar": [
        "2",
        "3",
        "4"
    ],
    "Porsche": [
        "Taycan",
        "Macan Electric"
    ],
    "Renault": [
        "Zoe",
        "Megane E-Tech Electric",
        "Scenic E-Tech Electric",
        "5 E-Tech",
        "4 E-Tech",
        "Twingo Electric"
    ],
    "Rivian": [
        "R1T",
        "R1S",
        "R2",
        "R3",
        "R3X"
    ],
    "Rolls-Royce": [
        "Spectre"
    ],
    "Skoda": [
        "Citigo-e iV",
        "Enyaq",
        "Elroq"
    ],
    "Smart": [
        "#1",
        "#3",
        "#5"
    ],
    "Subaru": [
        "Solterra"
    ],
    "Tesla": [
        "Roadster",
        "Model S",
        "Model 3",
        "Model X",
        "Model Y",
        "Cybertruck",
        "Semi"
    ],
    "Toyota": [
        "bZ4X",
        "Urban Cruiser EV",
        "C-HR+"
    ],
    "Volkswagen": [
        "ID.3",
        "ID.4",
        "ID.5",
        "ID.6",
        "ID.7",
        "ID. Buzz",
        "e-Golf",
        "e-Up!"
    ],
    "Volvo": [
        "EX30",
        "EX40",
        "EC40",
        "EX90",
        "EM90"
    ],
    "XPeng": [
        "G6",
        "G9",
        "P5",
        "P7",
        "X9"
    ],
    "Zeekr": [
        "001",
        "007",
        "X",
        "009",
        "7X"
    ]
}

ev_models = {
    brand.lower(): [model.lower() for model in models]
    for brand, models in ev_models.items()
}

if "model 3" in ev_models["tesla"]:
    print("It's an EV!")

# Iterate over all models
# for brand, models in ev_models.items():
#     for model in models:
#         print(f"{brand} {model}")


fuel_identifiers = {
    "electric": [
        "ev", "bev", "electric", "e-tron", "eq", "edrive",
        "ioniq", "id.", "id ", "model s", "model 3",
        "model x", "model y", "leaf", "zoe", "taycan",
        "bz4x", "ex30", "ex40", "ev3", "ev4", "ev5",
        "ev6", "ev9", "mg4", "atto", "seal", "dolphin"
    ],

    "diesel": [
        "tdi",      # VW Group
        "hdi",      # PSA
        "bluehdi",  # PSA
        "dci",      # Renault/Nissan
        "cdi",      # Mercedes
        "crdi",     # Hyundai/Kia
        "mjet", "multijet", "jtm",  # Fiat/Alfa
        "d4d",      # Toyota
        "ddis",     # Suzuki
        "td", "tddi",
        "tdci",     # Ford
        "sdi",
        "d",
        "xdrive20d",
        "xdrive30d",
        "sdrive18d",
        "20d",
        "25d",
        "30d",
        "35d",
        "40d",
        "50d",
        "220d",
        "320d",
        "520d"
    ],

    "petrol": [
        "tsi",
        "tfsi",
        "fsi",
        "mpi",
        "gdi",
        "tgdi",
        "ecoboost",
        "ecotec",
        "skyactiv-g",
        "vti",
        "puretech",
        "tce",
        "tsi evo",
        "turbo",
        "v6",
        "v8",
        "v10",
        "v12"
    ],

    "hybrid": [
        "hev",
        "hybrid",
        "phev",
        "plug-in",
        "plugin",
        "e-hybrid",
        "gte",
        "etech",
        "e-tech",
        "iprime",
        "prime",
        "4xe",
        "xdrive30e",
        "330e",
        "530e",
        "e-power",
        "full hybrid",
        "mhev",
        "mild hybrid"
    ]
}



ENGINE_PATTERN = re.compile(
    r"\b\d(?:\.\d)?\s*(?:"
    r"tdi|tdci|tddi|hdi|bluehdi|dci|cdi|crdi|"
    r"d-4d|d4d|ddi|ddis|multijet|mjet|jtd|jtdm|"
    r"tsi|tfsi|fsi|gdi|tgdi|mpi|"
    r"ecoboost|ecotec|puretech|tce|"
    r"skyactiv-d|skyactiv-g"
    r")\b",
    re.IGNORECASE,
)




DIESEL = {
    "tdi", "tdci", "tddi",
    "hdi", "bluehdi",
    "dci",
    "cdi",
    "crdi",
    "d4d", "d-4d",
    "ddi", "ddis",
    "jtd", "jtdm",
    "multijet", "mjet",
    "skyactiv-d",
}

PETROL = {
    "tsi", "tfsi", "fsi",
    "mpi",
    "gdi", "tgdi",
    "ecoboost",
    "ecotec",
    "puretech",
    "tce",
    "skyactiv-g",
}


BADGE_PATTERN = re.compile(
    r"\b("
    r"tdi|tdci|tddi|"
    r"hdi|bluehdi|"
    r"dci|"
    r"cdi|"
    r"crdi|"
    r"d-4d|d4d|"
    r"ddi|ddis|"
    r"jtdm?|"
    r"multijet|mjet|"
    r"tsi|tfsi|fsi|"
    r"gdi|tgdi|mpi|"
    r"ecoboost|ecotec|"
    r"puretech|tce|"
    r"skyactiv-d|skyactiv-g"
    
    r")\b",
    re.I
)



VEHICLE_WEIGHT_CLASSES = {
    "motorcycle": (50, 500),
    "car": (800, 2500),
    "large_car_suv": (1500, 3500),
    "lcv": (1800, 4500),          # vans, pickups, light commercial
    "medium_duty": (3500, 12000), # trucks, box trucks, small rigids
    "heavy_duty": (12000, 40000),  # heavy trucks, articulated tractors
    "extra_heavy": (40000, 90000)  # special trucks, dumpers, etc.
}


EV_MODELS = [
    # tesla
    "model 3",
    "model y",
    "model s",
    "model x",
    "cybertruck",
    "semi",
    "roadster",

    # volkswagen group
    "id.3",
    "id.4",
    "id.5",
    "id.7",
    "id. buzz",
    "e-golf",
    "e-up",

    # audi
    "e-tron",
    "q4 e-tron",
    "q6 e-tron",
    "q8 e-tron",
    "e-tron gt",

    # bmw
    "i3",
    "i4",
    "i5",
    "i7",
    "ix",
    "ix1",
    "ix2",
    "ix3",

    # mercedes-benz
    "eqb",
    "eqc",
    "eqe",
    "eqs",
    "eqe suv",
    "eqs suv",
    "eqa",

    # hyundai
    "ioniq 5",
    "ioniq 6",
    "kona electric",
    "inster",

    # kia
    "ev3",
    "ev4",
    "ev5",
    "ev6",
    "ev9",
    "niro ev",

    # peugeot
    "e-208",
    "e-2008",
    "e-308",
    "e-3008",
    "e-5008",

    # renault
    "zoe",
    "megane e-tech",
    "scenic e-tech",
    "renault 5 e-tech",

    # opel
    "corsa-e",
    "astra-e",
    "mokka-e",

    # citroen
    "e-c4",
    "e-c4 x",
    "e-c3",

    # skoda
    "enyaq",
    "elroq",

    # volvo
    "ex30",
    "ex40",
    "ex90",
    "ec40",

    # polestar
    "polestar 2",
    "polestar 3",
    "polestar 4",

    # ford
    "mustang mach-e",
    "f-150 lightning",

    # nissan
    "leaf",
    "ariya",

    # mg
    "mg4",
    "mg zs ev",

    # byd
    "atto 3",
    "seal",
    "dolphin",
    "seagull",

    # xpeng
    "g6",
    "g9",
    "p7",

    # zeekr
    "001",
    "x",
    "009",
    # rivian
    "r1t",
    "r1s",

    # lucid
    "air"
]


EV_KEYWORDS = [
    # generic
    "ev", "electric", "bev", "battery electric",
    # bulgarian
    "електрически", "електромобил", "електро",
    # tesla
    "tesla", "model 3", "model y", "model s", "model x", "cybertruck",
    # vw group
    "id.3", "id.4", "id.5", "id.7", "id buzz", "id. buzz",
    "e-golf", "e up", "e-up",
    # audi
    "e-tron", "etron", "q4 e-tron", "q6 e-tron", "q8 e-tron",
    # bmw
    "i3", "i4", "i5", "i7", "ix", "ix1", "ix2", "ix3",
    # mercedes
    "eqb", "eqc", "eqe", "eqs", "eqa",
    # hyundai/kia
    "ioniq 5", "ioniq 6", "kona electric", "ev6", "ev9",
    "niro ev",
    # renault
    "zoe", "megane e-tech", "scenic e-tech", "renault 5 e-tech",
    # peugeot/citroen/opel
    "e-208", "e-2008", "e-308", "e-3008",
    "e-c4", "e-c4 x",
    "corsa-e", "astra-e",
    # skoda
    "enyaq", "elroq",
    # ford
    "mustang mach-e", "mach e", "f-150 lightning",
    # nissan
    "leaf", "ariya",
    # others
    "mg4", "mg zs ev", "byd", "seal", "atto 3", "dolphin",
    "xpeng", "zeekr", "rivian", "lucid"
]
HYBRID_KEYWORDS = [
    # generic
    "hybrid", "full hybrid", "mild hybrid",
    "phev", "plug-in", "plugin hybrid",

    # bulgarian
    "хибрид", "пълен хибрид", "мек хибрид", "плъгин хибрид",

    # toyota systems (VERY important)
    "hsd", "hybrid synergy drive", "ths", "toyota hybrid",

    # vw group
    "gte", "tsi hybrid",

    # mercedes
    "eq boost", "eq-boost", "eq power",

    # bmw
    "xdrive hybrid", "active hybrid",

    # renault
    "e-tech hybrid", "e tech",

    # stellantis
    "4xe", "hybrid4", "e-hybrid", "plug-in hybrid",

    # hyundai/kia
    "tmhev", "hev", "k-hybrid",

    # honda
    "i-mmd", "immd", "ehev",

    # ford
    "ecoboost hybrid", "mhev"
]
DIESEL_KEYWORDS = [
    # generic
    "diesel", "diesel engine",

    # bulgarian
    "дизел", "дизелов",

    # vw group
    "tdi", "sd i", "sd- i",

    # ford
    "tdci", "tddi",

    # psa
    "hdi", "bluehdi",

    # renault
    "dci",

    # mercedes
    "cdi", "bluetec",

    # fiat/alfa
    "jtd", "multijet", "mjet",

    # toyota
    "d-4d", "d4d",

    # kia/hyundai
    "crdi", "crdi diesel", "u2 crdi",

    # bmw
    "d", "xdrive d",

    # mazda
    "skyactiv-d",

    # opel
    "cdti"
]

PETROL_KEYWORDS = [
    # generic
    "petrol", "gasoline", "benzine",

    # bulgarian
    "бензин", "бензинов",

    # vw group
    "tsi", "tfsi", "fsi", "mpi",

    # ford
    "ecoboost",

    # psa
    "vti", "puretech",

    # renault
    "tce",

    # hyundai/kia
    "gdi", "tgdi", "mpi",

    # toyota
    "vvt i", "vvti", "dual vvt i",

    # mazda
    "skyactiv-g",

    # honda
    "vtec", "ivtec",

    # fiat
    "fire",

    # bmw
    "i",  # (careful, weak signal but sometimes used)

    # mercedes
    "cgi", "kompressor"
]

FUEL_SIGNALS = {
    "electric": EV_KEYWORDS,
    "hybrid": HYBRID_KEYWORDS,
    "diesel": DIESEL_KEYWORDS,
    "petrol": PETROL_KEYWORDS
}

MOTORCYCLE = []
Car = []
LCV = []
MEDIUM_DUTY_VEHICLES = []
HEAVY_DUTY_VEHICLES = []
