import re

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
    },

    "Lynk & Co": {
        "em-p": "phev",
    },

    "Audi": {
        "tfsie": "phev",
        "tfsi e": "phev",
    },

    "Volkswagen": {
        "gte": "phev",
    },

    "Mercedes-Benz": {
        "eq power": "phev",
    },

    "BMW": {
        "330e": "phev",
        "530e": "phev",
        "545e": "phev",
        "745e": "phev",
        "xdrive30e": "phev",
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

    "Nissan": {
        "e-power": "hev",
        "epower": "hev",
    },

    "Hyundai": {
        "hybrid blue drive": "hev",
        "smartstream hybrid": "hev",
    },

    "Kia": {
        "smartstream hybrid": "hev",
    },


    # =========================
    # MHEV
    # =========================

    "Mercedes-Benz": {
        "eq boost": "mhev",
        "eq-boost": "mhev",
    },

    "Volkswagen Group": {
        "e-tsi": "mhev",
        "etsi": "mhev",
    },

    "Ford": {
        "ecoboost hybrid": "mhev",
    },

    "Mazda": {
        "m hybrid": "mhev",
        "m-hybrid": "mhev",
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

    "Audi": {
        "e-tron": "electric",
    },

    "Volkswagen": {
        "id": "electric",
        "id.3": "electric",
        "id.4": "electric",
        "id.5": "electric",
        "id.7": "electric",
    },

    "BMW": {
        "edrive": "electric",   # ambiguous, check model
        "i": "electric",
    },

    "Mercedes-Benz": {
        "eq": "electric",
        "eqs": "electric",
        "eqe": "electric",
        "eqb": "electric",
    },

    "Hyundai": {
        "e-gmp": "electric",
    },

    "Kia": {
        "e-gmp": "electric",
    },

    "Ford": {
        "mach-e": "electric",
    },

    "BYD": {
        "blade battery": "electric",
        "e-platform": "electric",
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

    "Volkswagen": {
        "ecofuel": "cng",
        "g-tec": "cng",
        "tgi": "cng",
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
        "seal",
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

    "ioniq 5",
    "ioniq 6",
    "ioniq 9",

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


DIESEL_MODELS = {
    "tdi",
    "tdci",
    "dci",
    "hdi",
    "bluehdi",

    "d4d",
    "d-cat",

    "cdi",
    "om654",
    "om656",

    "multijet",
    "jtd",

    "skyactiv-d",
}


ELECTRIC_CODES  = ["ev", "bev", "eq", "i4", "i5", "ix", "id.4", "i3", "ix1", "ix2", "ix3","eqa", "eqb", "eqc", "eqe", "eqs", "eqv",  "enyaq", "elroq", "epiq", "taycan", "r1t", "r1s", "r2",
                   "model 3", "model y", "model s", "model x", "cybertruck",
                   "ioniq 5", "ioniq 6", "ioniq 9", "ev 3", "ev 4", "ev 5", "ev 6", "ev 9",
                   "atto 3", "dolphin", "byd seal", "seal", "bydseal",
                   "macanelectric", "enyaq", "elroq", "epiq", "peaq", "ex30", "ex90", "ex60", "es90", "c40",
                   "atto3", "atto", "bydseal", "byd han", "byd tang", "tang", "dolphin", "sealion",
                   "leapmotor", "t03", "c10", "zeekr", "zeekr001", "zeekrx", "xpeng", "g6", "g9", "p7", "nio", "el6",
                   "et5", "et7", "zoe",
                   "omoda", "e5", "changan", "skywell", "aion", "maxus", "eDeliver", "seres", "voyah", "free", "lucid",
                   "rivian", "r1t", "r1s", "e-rifter"
                   ]

ELECTRIC_BRANDS = ["electric", "e-tron", "etron", "e-tech", "etech", "tesla", "ioniq", "bz4x",
                   "aiways",  "fisker" , "ev2", "lucid motors", "nio" , "polaris" , "rimac" ,  "seres" , "tesla" , "xpeng", "jiayuan",
                   "elaris" , "e.go", "spring", "zoe",
                   "id.3", "id3", "id.4", "id4", "id.5", "id5", "id.6", "id6", "id.7", "id7",
                   "id.buzz", "idbuzz", "id.unyx", "idunyx", "e-up!", "eup!", "gtx",
                   ]




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



HYBRID_KEYWORDS = [
    "hybrid",
    "reev",
    "zr-v",
    "hsd",
    "hev",
    "phev",
    "mhev",
    "бензин/електричество",
    "бензин/електричество/внг",
    "хибрид",
    "petrol/electric",
    "phev (plug-in)",
    "erev",
    "boost",
    "e:hev",
    "i-mmd",
    "plug-in",
    "дизел/електричество",
]

ELECTRIC_KEYWORDS = [
    "electric",
    "електродвигател",
    "електромотор",
    "електрически",
    "ev",
    "bev",
    "e-tron",
    "eq",
    "tesla",
    "e-tech",
    "i4",
    "i5",
    "ix",
    "ioniq",
    "bz4x",
    "eqs",
    "eqb",
]

DIESEL_KEYWORDS = [
    "diesel",
    "дизел",
    "дизел/биодизел",
    "ecoblue",
    "scania",
    "tgx",
    "man",
    "cdi",
    "dci",
    "hdi",
    "bluehdi",
    "d-4d",
    "tdi",
    "2.8d",
]

PETROL_KEYWORDS1 = [
    "petrol",
    "sandero",
    "shine",
    "шайн",
    "ситирей",
    "1,5t",
    "gasolina",
    "puretech",
    "tgdi",
    "tsi",
    "tfsi",
    "ecoboost",
    "бензин",
    "petrol/gas",
    "eco-g",
]

GAS_KEYWORDS = [
    "cng",
    "tgi",
    "g-tec",
    "lpg",
    "gas",
    "внг",
    "eco-g",
]


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

EV_KEYWORDS = [
    # generic
    "ev", "electric", "bev", "battery electric",

    # bulgarian
    "електрически",
    "електромобил",
    "електро",

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

HYBRID_KEYWORDS1 = [
    # generic
    "hybrid", "full hybrid", "mild hybrid",
    "phev", "plug-in", "plugin hybrid",

    # bulgarian
    "хибрид",
    "пълен хибрид",
    "мек хибрид",
    "плъгин хибрид",
    "плъг-ин хибрид",
    "зареждащ се хибрид",
    "хибриден",
    "меко хибриден",

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

DIESEL_KEYWORDS1 = [
    # generic
    "diesel", "diesel engine",

    # bulgarian
    "дизел",
    "дизелов",
    "дизелов",
    "дизелов двигател",

    # vw group
    "tdi", "sdi",

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
     "xdrive d",

    # mazda
    "skyactiv-d",

    # opel
    "cdti"
]

PETROL_KEYWORDS = [
    # generic
    "petrol", "gasoline", "gas", "benzine",

    # bulgarian
    "бензин",
    "бензинов",
    "бензинов двигател",

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
    "vvt-i", "vvt i", "vvti", "dual vvt-i", "dual vvt i",

    # mazda
    "skyactiv-g",

    # honda
    "vtec", "i-vtec", "ivtec",

    # fiat
    "fire",

    # bmw
    # DO NOT use "i" as a keyword—it creates many false positives.

    # mercedes
    "cgi", "kompressor"
]

BMW_REGEX = r"\b(?:116|118|120|218|220|320|330|420|520|530|540|740|750|840)i\b"

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