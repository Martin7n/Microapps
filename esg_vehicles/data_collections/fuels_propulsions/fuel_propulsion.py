import re

from esg_vehicles.data_collections.fuels_propulsions.diesel import DIESEL_KEYWORDS
from esg_vehicles.data_collections.fuels_propulsions.ev import ELECTRIC_KEYWORDS
from esg_vehicles.data_collections.fuels_propulsions.hybrid import HYBRID_KEYWORDS
from esg_vehicles.data_collections.fuels_propulsions.petrol import PETROL_KEYWORDS

FUEL_ID = {
            "бензин/електричество/внг":	"hybrid",
            "дизел/биодизел":	"diesel",
            "дизел/електричество":	"hybrid",
            "diesel":"diesel",
            "electric":	"EV",
            "gas":	"gas",
            "petrol":	"petrol",
            "petrol/electric":	"hybrid",
            "petrol/gas":	"petrol/gas",
            "PHEV (plug-in)":	"hybrid",
}


PETROL_KWORD = {

    "generic": {
        # English
        "petrol",
        "gasoline",
        "gasolina",
        "benzine",
        "otto",

        # Bulgarian
        "бензин",
        "бензинов",
        "бензинов двигател",
        "безнин",
        "-бензин",
        "(бензин)",

        # Mixed fuel
        "petrol/gas",
        "бензин/газ",
    },

    "Volkswagen Group": {
        "tsi",
        "e-tsi",
        "etsi",
        "еtsi",
        "tfsi",
        "tfsie",      # PHEV variant handled separately
        "fsi",
        "mpi",
        "fsi turbo",
        "ea111",
        "ea211",
        "ea888",
    },

    "Audi": {
        "tfsi",
        "fsi",
    },

    "Skoda": {
        "tsi",
        "mpi",
        "fsi",
    },

    "SEAT": {
        "tsi",
        "fsi",
        "mpi",
    },

    "Cupra": {
        "tsi",
    },

    "Ford": {
        "ecoboost",
        "eco boost",
        "duratec",
        "dragon",
    },

    "PSA": {
        "puretech",
        "pure tech",
        "vti",
        "e-vti",
        "thp",
        "e-thp",
    },

    "Renault": {
        "tce",
        "tcе",
        "тce",
        "7tce",
        "sce",
        "energy tce",
    },

    "Dacia": {
        "sce",
        "tce",
    },

    "Hyundai": {
        "gdi",
        "tgdi",
        "t-gdi",
        "turbo-gdi",
        "kappa",
        "smartstream g",
    },

    "Kia": {
        "gdi",
        "tgdi",
        "t-gdi",
        "turbo-gdi",
        "smartstream g",
    },

    "Toyota": {
        "vvt",
        "vvt-i",
        "vvti",
        "dual vvt",
        "dual vvt-i",
        "valvematic",
    },

    "Honda": {
        "vtec",
        "i-vtec",
        "ivtec",
        "earth dreams",
    },

    "Mazda": {
        "skyactiv-g",
        "skyactiv",
        "skyactive",
        "skyaktiv",
        "e-skyactiv",
        "eskyactiv",
    },

    "Nissan": {
        "dig-t",
        "digt",
        "hr",
    },

    "Mitsubishi": {
        "mivec",
    },

    "Suzuki": {
        "dualjet",
        "dual jet",
        "boosterjet",
        "booster jet",
    },

    "Subaru": {
        "boxer",
    },

    "BMW": {
        "twinpower turbo",
        "twinpower",
    },

    "Mercedes": {
        "cgi",
        "kompressor",
    },

    "Fiat": {
        "fire",
        "firefly",
        "multiair",
        "t-jet",
        "jet",
    },

    "Alfa Romeo": {
        "tbi",
        "multiair",
    },

    "Volvo": {
        "t2",
        "t3",
        "t4",
        "t5",
        "t6",   # PHEV ще се филтрира отделно
        "t8",   # PHEV ще се филтрира отделно
    },

    "Jaguar Land Rover": {
        "ingenium petrol",
        "p200",
        "p250",
        "p300",
        "p400",
    },

    "General Motors": {
        "ecotec",
        "ecotec turbo",
    },

    "Chevrolet": {
        "ecotec",
    },

    "Opel": {
        "ecotec",
        "turbo ecotec",
    },

    "Peugeot": {
        "puretech",
        "vti",
        "thp",
    },

    "Citroen": {
        "puretech",
        "vti",
        "thp",
    },

    "Mini": {
        "cooper",
        "cooper s",
        "john cooper works",
    },

    "Lexus": {
        "vvt-i",
        "vvti",
    },

    "Infiniti": {
        "vc-t",
    },

    "Chery": {
        "acteco",
    },

    "MG": {
        "gdi",
    }
}


DIESEL_KWORDS = {

    "generic": {
        # English
        "diesel",
        "disel",
        "dsl",
        "tdci"
        "diesel engine",
        "diesel/electric",

        # Bulgarian
        "дизел",
        "дизелов",
        "дизелов двигател",
        "(дизел)",
        "дизел/електричество",
    },

    "Volkswagen Group": {
        "tdi",
        "tdi,",
        "tdi-cr",
        "tdicr",
        "tdiscr",
        "cr tdi",
        "common rail tdi",
        "sdi",
        "sdi diesel",
    },

    "Audi": {
        "tdi",
        "ultra tdi",
        "clean diesel",
    },

    "Skoda": {
        "tdi",
        "sdi",
    },

    "SEAT": {
        "tdi",
        "sdi",
    },

    "Cupra": {
        "tdi",
    },

    "Ford": {
        "tdci",
        "тdci",
        "tddi",
        "ecoblue",
        "eco blue",
        "duratorq",
        "powerstroke",
    },

    "PSA": {
        "hdi",
        "e-hdi",
        "ehdi",
        "bluehdi",
        "blue hdi",
    },

    "Peugeot": {
        "hdi",
        "bluehdi",
    },

    "Citroen": {
        "hdi",
        "bluehdi",
    },

    "DS": {
        "bluehdi",
    },

    "Renault": {
        "dci",
        "energy dci",
        "blue dci",
        "dti",
    },

    "Dacia": {
        "dci",
        "blue dci",
    },

    "Mercedes-Benz": {
        "cdi",
        "bluetec",
        "blue tec",
        "om",
    },

    "BMW": {
        "turbodiesel",
        "twinpower diesel",
    },

    "Fiat": {
        "jtd",
        "jtdm",
        "multijet",
        "multi jet",
        "multijet ii",
        "mjet",
    },

    "Alfa Romeo": {
        "jtd",
        "jtdm",
        "multijet",
    },

    "Jeep": {
        "multijet",
    },

    "Opel": {
        "cdti",
        "ecotec diesel",
    },

    "Vauxhall": {
        "cdti",
    },

    "Toyota": {
        "d-4d",
        "d4d",
        "dd-4d",
    },

    "Honda": {
        "i-dtec",
        "idtec",
        "i-ctdi",
        "ictdi",
    },

    "Hyundai": {
        "crdi",
        "u2 crdi",
        "smartstream d",
    },

    "Kia": {
        "crdi",
        "u2 crdi",
        "smartstream d",
    },

    "Mazda": {
        "skyactiv-d",
        "skyactiv d",
    },

    "Mitsubishi": {
        "di-d",
        "did",
    },

    "Nissan": {
        "dci",
        "yd",
    },

    "Subaru": {
        "boxer diesel",
    },

    "Volvo": {
        "drive-e diesel",
        "diesel drive-e",
    },

    "Jaguar Land Rover": {
        "ingenium diesel",
        "ingenium d",
        "td4",
        "sd4",
        "sdv6",
        "tdv6",
        "tdv8",
    },

    "Land Rover": {
        "td4",
        "td5",
        "sd4",
        "sdv6",
        "tdv6",
        "tdv8",
    },

    "Isuzu": {
        "ddi",
    },

    "Chevrolet": {
        "vcdi",
    },

    "Daewoo": {
        "vcdi",
    },

    "Suzuki": {
        "ddis",
        "ddis",
    },

    "IVECO": {
        "hpi",
        "hpt",
        "cursor",
    },

    "MAN": {
        "d20",
        "d26",
        "common rail",
    },

    "Scania": {
        "dc09",
        "dc13",
        "super",
    },

    "DAF": {
        "paccar",
        "mx11",
        "mx13",
    },

    "Renault Trucks": {
        "dxi",
    },

    "Cummins": {
        "isb",
        "isc",
        "isl",
        "isx",
        "x12",
        "x15",
    },

    "Perkins": {
        "perkins diesel",
    },

    "Deutz": {
        "deutz diesel",
    },

    "Kubota": {
        "kubota diesel",
    },

    "Yanmar": {
        "yanmar diesel",
    }
}

HYBRID_KWORDS = {

    "HEV": {

        "generic": {
            "hybrid",
            "hybrid,",
            "хибрид",
            "hev",
            "hev-",
            "(hev)",

            "petrol/electric",
            "diesel/electric",
            "бензин/електричество",
            "дизел/електричество",
            "електричество/бензин",
        },

        "Toyota": {
            "hsd",
            "hybrid synergy drive",
            "toyota hybrid",
            "toyota hybrid system",
            "ths",
        },

        "Honda": {
            "e:hev",
            "ehev",
            "i-mmd",
            "immd",
            "sport hybrid",
        },

        "Hyundai": {
            "hybrid blue drive",
            "smartstream hybrid",
        },

        "Kia": {
            "eco hybrid",
            "smartstream hybrid",
        },

        "Renault": {
            "e-tech hybrid",
            "etech hybrid",
            "e-tech",
            "etech",
        },

        "Nissan": {
            "e-power",
            "epower",
        },

        "Lexus": {
            "self charging hybrid",
            "lexus hybrid",
        },

        "Ford": {
            "full hybrid",
        },

        "Suzuki": {
            "strong hybrid",
        }
    },

    "MHEV": {

        "generic": {
            "mhev",
            "m-hev",
            "mild hybrid",
            "mild-hybrid",

            "48v",
            "48 volt",
            "48v hybrid",
            "48v-hybrid",
            "48v-hibrid",
            "48v/mild",
        },

        "Mercedes": {
            "eq boost",
            "eq-boost",
            "boost",
        },

        "Audi": {
            "mhev plus",
        },

        "Volkswagen Group": {
            "etsi",
            "e-tsi",
            "mild tsi",
        },

        "Hyundai": {
            "48v diesel",
            "48v petrol",
        },

        "Kia": {
            "48v diesel",
            "48v petrol",
        },

        "Suzuki": {
            "smart hybrid",
        },

        "Mazda": {
            "m hybrid",
            "m-hybrid",
        },

        "Ford": {
            "ecoboost hybrid",
        }
    },

    "PHEV": {

        "generic": {

            "phev",
            "рhev",

            "plugin",
            "plug in",
            "plug-in",
            "plug",

            "plug-in hybrid",
            "plugin hybrid",

            "(plug-in)",

            "p-hev",
        },

        "Volkswagen": {
            "gte",
        },

        "Audi": {
            "tfsie",
            "tfsi e",
        },

        "Skoda": {
            "iv",
        },

        "Cupra": {
            "e-hybrid",
        },

        "SEAT": {
            "e-hybrid",
        },

        "Mercedes": {
            "eq power",
        },

        "BMW": {
            "edrive",
            "xdrive30e",
            "330e",
            "530e",
            "745e",
        },

        "Peugeot": {
            "hybrid4",
        },

        "Citroen": {
            "hybrid4",
        },

        "DS": {
            "e-tense",
        },

        "Jeep": {
            "4xe",
        },

        "Land Rover": {
            "p400e",
            "p300e",
        },

        "Volvo": {
            "recharge",
        },

        "Honda": {
            "e:phev",
        },

        "Renault": {
            "e-tech plug-in",
        },

        "Hyundai": {
            "plug-in hybrid",
        },

        "Kia": {
            "plug-in hybrid",
        }
    },

    "REEV": {

        "generic": {

            "reev",
            "erev",
            "rev",

            "range extender",
            "range-extender",
        },

        "Mazda": {
            "r-ev",
        },

        "Leapmotor": {
            "reev",
        },

        "Li Auto": {
            "erev",
        }
    }
}

#Other brand specific i.e. not technologies, but engines:

BMW = [
    {"hybrid":[
"330e",
"530e",
"545e",
"745e",
"225xe",
"x5 xDrive45e"]},

    {"petrol":[
"330e",
"530e",
"545e",
"745e",
"225xe",
"x5 xDrive45e"]},

]



TECH = {
    "tdi":        {"fuel": "diesel", "brand": "Volkswagen Group"},
    "crdi":       {"fuel": "diesel", "brand": "Hyundai/Kia"},
    "ecoboost":   {"fuel": "petrol", "brand": "Ford"},
    "bluehdi":    {"fuel": "diesel", "brand": "PSA"},
    "e:hev":      {"fuel": "hev", "brand": "Honda"},
    "e-power":    {"fuel": "hev", "brand": "Nissan"},
    "tfsie":      {"fuel": "phev", "brand": "Audi"},
}


TECHNOLOGY_FUEL_MAP = {

    # =========================
    # PHEV
    # =========================

    "BYD": {
        "dm": "phev",
        "dm-i": "phev",
        "dm-p": "phev",
        "super dm": "phev",
        "blade battery": "electric",
        "e-platform": "electric",
    },

    "Lynk & Co": {
        "em-p": "phev",
    },

    "Audi": {
        "tfsie": "phev",
        "tfsi e": "phev",
        "e-tron": "electric",

    },

    "Jeep": {
        "4xe": "phev",
    },

    "Peugeot": {
        "hybrid4": "phev",
    },

    "Citroen": {
        "hybrid4": "phev",
    },

    "DS": {
        "e-tense": "phev",
    },

    # =========================
    # HEV (full hybrid)
    # =========================

    "Toyota": {
        "hsd": "hev",
        "hybrid synergy drive": "hev",
        "ths": "hev",
        "toyota hybrid": "hev",
    },

    "Honda": {
        "e:hev": "hev",
        "ehev": "hev",
        "i-mmd": "hev",
        "immd": "hev",
    },

    "Renault": {
        "e-tech hybrid": "hev",
        "e-tech": "hev",
    },

    "Hyundai": {
        "hybrid blue drive": "hev",
        "smartstream hybrid": "hev",
        "e-gmp": "electric",

    },



    # =========================
    # MHEV
    # =========================

    "Mercedes-Benz": {
        "eq boost": "mhev",
        "eq-boost": "mhev",
        "eq power": "phev",
        "eq": "electric",
        "eqs": "electric",
        "eqe": "electric",
        "eqb": "electric",

    },

    "Volkswagen": {
        "e-tsi": "mhev",
        "etsi": "mhev",
        "gte": "phev",
        "ecofuel": "cng",
        "g-tec": "cng",
        "tgi": "cng",
        "id": "electric",
        "id.3": "electric",
        "id.4": "electric",
        "id.5": "electric",
        "id.7": "electric",

    },


    "Suzuki": {
        "smart hybrid": "mhev",
    },

    # =========================
    # REEV / EREV
    # =========================

    "Nissan": {
        "e-power": "hev",   # series hybrid, not plug-in
    },

    "Mazda": {
        "r-ev": "reev",
        "reev": "reev",
        "m hybrid": "mhev",
        "m-hybrid": "mhev",
    },

    "Leapmotor": {
        "reev": "reev",
        "erev": "reev",
    },
    "Li Auto": {
        "erev": "reev",
    },

    "Voyah": {
        "evr": "reev",
    },

    # =========================
    # BEV
    # =========================
    "BMW": {
        "edrive": "electric",   # ambiguous, check model
        "i": "electric",
        "330e": "phev",
        "530e": "phev",
        "545e": "phev",
        "745e": "phev",
        "xdrive30e": "phev",
    },

    "Kia": {
        "e-gmp": "electric",
        "smartstream hybrid": "hev",

    },

    "Ford": {
        "mach-e": "electric",
        "ecoboost hybrid": "mhev",
    },

    "Zeekr": {
        "800v": "electric",
    },

    "XPeng": {
        "800v": "electric",
    },

    # =========================
    # LPG / CNG
    # =========================

    "Dacia": {
        "eco-g": "lpg",
        "eco g": "lpg",
    },

    "Skoda": {
        "g-tec": "cng",
    },
}




bev_models = {

    # =========================
    # Tesla
    # =========================
    "tesla": {
        "model 3",
        "model y",
        "model s",
        "model x",
        "cybertruck",
    },

    # =========================
    # BYD
    # =========================
    "byd": {
        "dolphin",
        "dolphin mini",
        "seagull",
        "atto 3",
        "yuan plus ev",
        # "seal",
        "sealion 7",
        "han ev",
        "tang ev",
        "e2",
        "e3",
    },

    # =========================
    # NIO
    # =========================
    "nio": {
        "es6",
        "es7",
        "es8",
        "et5",
        "et5 touring",
        "et7",
        "ec6",
        "ec7",
        "et9",
    },

    # =========================
    # xpeng
    # =========================
    "xpeng": {
        "g3",
        "g6",
        "g9",
        "p5",
        "p7",
        "p7i",
        "mona m03",
    },

    # =========================
    # zeekr
    # =========================
    "zeekr": {
        "001",
        "007",
        "009",
        "x",
        "7x",
    },

    # =========================
    # li auto
    # =========================
    "li auto": {
        "mega",
        "i8",
    },

    # =========================
    # xiaomi
    # =========================
    "xiaomi": {
        "su7",
        "yu7",
    },

    # =========================
    # leapmotor
    # =========================
    "leapmotor": {
        "t03",
        "c10",
        "c11",
        "c16",
    },

    # =========================
    # mg
    # =========================
    "mg": {
        "mg4 electric",
        "mg5 electric",
        "zs ev",
        "marvel r",
        "cyberster",
    },

    # =========================
    # volkswagen group
    # =========================
    "volkswagen": {
        "id.3",
        "id.4",
        "id.5",
        "id.6",
        "id.7",
        "id.buzz",

    },

    "skoda": {
        "enyaq",
        "enyaq coupe",
        "elroq",
    },

    "audi": {
        "q4 e-tron",
        "q6 e-tron",
        "e-tron",
        "e-tron gt",
    },

    "porsche": {
        "taycan",
        "macan electric",
    },

    # =========================
    # bmw / mini
    # =========================
    "bmw": {
        "i3",
        "i4",
        "i5",
        "i7",
        "ix",
        "ix1",
        "ix2",
        "ix3",
    },

    "mini": {
        "cooper electric",
        "aceman electric",
    },

    # =========================
    # mercedes
    # =========================
    "mercedes": {
        "eqa",
        "eqb",
        "eqe",
        "eqs",
        "eqe suv",
        "eqs suv",
        "eqv",
    },

    # =========================
    # hyundai / kia
    # =========================
    "hyundai": {
        "ioniq 5",
        "ioniq 6",
        "ioniq 9",
        "kona electric",
        "inster",
    },

    "kia": {
        "ev3",
        "ev5",
        "ev6",
        "ev9",
        "niro ev",
    },

    # =========================
    # stellantis
    # =========================
    "peugeot": {
        "e-208",
        "e-2008",
        "e-3008",
        "e-308",
        "e-5008",
    },

    "citroen": {
        "e-c3",
        "e-c4",
        "e-berlingo",
        "e-jumpy",
    },

    "opel": {
        "corsa electric",
        "mokka electric",
        "astra electric",
        "combo electric",
        "vivaro electric",
    },

    "fiat": {
        "500e",
        "600e",
        "e-doblo",
        "doblo electric",
    },

    # =========================
    # chinese additions
    # =========================
    "aion": {
        "s",
        "y",
        "v",
        "hyper gt",
        "hyper ht",
    },

    "avatr": {
        "11",
        "12",
    },

    "im motors": {
        "l6",
        "l7",
        "ls6",
        "ls7",
    },

    "neta": {
        "v",
        "aya",
        "x",
    },

    "gwm ora": {
        "ora 03",
        "ora 07",
    },

    "geely": {
        "geometry c",
        "geometry e",
        "galaxy e5",
    },
}



BEV_MODELS = {
    "model 3",
    "model y",
    "model s",
    "model x",

    "dolphin",
    "atto 3",
    "seal",
    "seagull",

    "es6",
    "es7",
    "es8",
    "et5",
    "et7",

    "g6",
    "g9",
    "p7",

    "id.3",
    "id.4",
    "id.5",
    "id.7",
    "id.buzz",

    "enyaq",
    "taycan",

    "ioniq 3"
    "ioniq 5",
    "ioniq 6",
    "ioniq 9",
    "айоник 3",
    "айоник 5",
    "айоник 6",
    "айоник 9",

    "ev3",
    "ev5",
    "ev6",
    "ev9",

    "e-208",
    "e-2008",
    "e-3008",
    "e-308",
    "e-5008",

    "e-berlingo",
    "e-jumpy",
    "e-expert",

    "mg4 electric",
    "zs ev",

    "su7",
    "yu7",
}


HYBRID_MODELS = {
    "prius",
    "corolla hybrid",
    "yaris hybrid",
    "rav4 hybrid",
    "great all wey 05",

    "camry hybrid",
    "highlander hybrid",

    "ioniq hybrid",
    "kona hybrid",

    "niro hybrid",
    "sportage hybrid",
    "sorento hybrid",

    "tucson hybrid",

    "c-hr hybrid",

    "x5 xdrive45e",
    "x5 xdrive50e",

    "e:hev",
    "hsd",
    "ths",
    "hybrid synergy drive",
}


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



GAS_KEYWORDS = [
    "cng",
    "tgi",
    "g-tec",
    "lpg",
    "gas",
    "внг",
    "eco-g",
]


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






BMW_REGEX = r"\b(?:116|118|120|218|220|320|330|420|520|530|540|740|750|840)i\b"

FUEL_SIGNALS = {
    "electric": ELECTRIC_KEYWORDS,
    "hybrid": HYBRID_KEYWORDS,
    "diesel": DIESEL_KEYWORDS,
    "petrol": PETROL_KEYWORDS
}

