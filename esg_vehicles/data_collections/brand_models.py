''''
1. exact model match
2. brand + technology
3. technology alone
4. generic fuel keyword
'''


BRAND_ALIASES = {
    "bmw": ["bmw", "бмв"],
    "audi": ["audi", "ауди"],
    "forthing": ["forthing", "фортинг"],
    "joyor": ["joyor", "джойер"],
    "mhero": ["mhero", "мхеро", "мхиро"],
    "geely": ["geely", "джиили"],
    "lynk&co": ["lynk", "линк", "линк енд ко", "линк&ко", "линк & ко"],
    "suzuki": ["suzuki", "сузуки"],
    "dodge": ["dodge", "додж"],
    "haval":["haval", "хавал"],
    "dfsk":["dfsk", "дфск"],
    "lexus":["lexus","лексус", "лексъс"],
    "dacia": ["dacia","дачия", "дачиа"],
    "ineos": ["ineos", "инеос"],
    "mercedes-benz": ["mercedes-benz", "mercedes", "мерцедес", "мерцедес-бенц"],
    "volkswagen": ["volkswagen", "vw", "фолксваген", "фв"],
    "skoda": ["skoda", "škoda", "шкода"],
    "peugeot": ["peugeot", "пежо"],
    "renault": ["renault", "рено"],
    "citroen": ["citroen", "citröen", "ситроен"],
    "opel": ["opel", "опел"],
    "ford": ["ford", "форд"],
    "toyota": ["toyota", "тоyота", "тойота"],
    "nissan": ["nissan", "нисан"],
    "hyundai": ["hyundai", "хюндай", "hyunday"],
    "kia": ["kia", "киа"],
    "mazda": ["mazda", "мазда"],
    "honda": ["honda", "хонда"],
    "fiat": ["fiat", "фиат"],
    "alfa romeo": ["alfa romeo", "алфа ромео"],
    "volvo": ["volvo", "волво"],
    "seat": ["seat", "сеат"],
    "cupra": ["cupra", "купрa", "купра"],
    "tesla": ["tesla", "тесла"],
    "byd": ["byd", "бийд"],
    "daf": ["daf"],
    "iveco": ["iveco", "ивеко"],
    "man": ["man", "ман"],
    "mercedes": [
        "mercedes",
        "mercedes-benz",
        "mercedes benz",
        "mb",
        "мерцедес",
        "мерцедес-бенц",
    ],
    "scania": ["scania", "скания"],
    "isuzu": ["isuzu", "исузу"],
    "fuso": ["fuso", "mitsubishi fuso", "фусо"],
    "hino": ["hino", "хино"],
    "kamaz": ["kamaz", "камаз", "камаз"],
    "maz": ["maz", "маз"],
    "gaz": ["gaz", "газ"],
    "ural": ["ural", "урал"],
    "tatra": ["tatra", "татра"],
    "kenworth": ["kenworth"],
    "peterbilt": ["peterbilt"],
    "mack": ["mack"],
    "freightliner": ["freightliner"],
    "western star": ["western star"],
    "international": ["international", "international trucks", "navistar"],
    "sterling": ["sterling"],
    "faw": ["faw"],

    "jac": ["jac"],
    "ashok leyland": ["ashok leyland"],
    "bharatbenz": ["bharatbenz"],
    "subaru": ["subaru", "субару", "субаро", "собару"],
    "bentley": ["bentley", "бентли"],
    "porsche": ["porsche", "порше", "porshe", "porche"],
    "piaggio": ["piaggio", "пиаджио"],
    "mini": ["mini", "mini cooper", "мини куупър", "мини купър", ],
    "lamborghini": ["lamborghini", "ламборгини", "лаборджини"],
    "rolls-royce": ["rolls-royce", "ролс ройс", "ролс роис"],

    "mitsubishi": ["mitsubishi", "мицубиши", "мицoбиши", "мицубиши"],
    "jeep": ["jeep", "джип", "джиип"],
    "aston martin": ["aston martin", "астон мартин", "астън мартин", "aston"],
    "mg": ["mg", "мг", "мг3", "mg3"],
    "ds": ["ds", "диез", "диес", "дс"],

    "wey": ["wey", "уей", "вей", "way"],
    "baik": ["baik", "баик", "байк", "байц"],
    "voyah": ["voyah", "войах", "войа", "воя", "воиуах"],
    "foton": ["foton", "фотон"],
    "shacman": ["shacman", "shaanxi"],
    "sinotruk": ["sinotruk", "howo"],
    "dongfeng": ["dongfeng", "донгфенг"],

    "mclaren": ["mclaren", "макларън", "макларен"],
    "ssang yong": ["ssang yong", "санг йонг", "сангйонг", "ссанг йонг", "ссангйонг", "ssangyong", "санг"],
    "ferrari": ["ferrari", "ферари", "ferari"],
    "fisker": ["fisker", "фискер", "фискър"],
    "kgm": ["kgm", "кгм", "кей джи ем"],

    "cadillac": ["cadillac", "cadilac", "кадилак"],
    "maserati": ["maserati", "мазерати", "масерати"],
    "infiniti": ["infiniti", "инфинити"],
    "omoda": ["omoda", "омода"],
    "venucia": ["venucia", "венуция", "венуциа"],
    "jaguar": ["jaguar", "jagoar", "ягуар", "джагуар"],
    "baw": ["baw", "бау", "бал"],
    "leapmotor": ["leapmotor", "липмотор", "лийпмотор", "лиипмотор", "леапмотор"],
    "baic": ["baic", "баик", "баиц"],
    "aeolus": ["aeolus", "аеолус", "аеолос"],
    "jaecoo": ["jaecoo", "jaeco", "жаеко", "джаико", "жаесо", "джейко", "джейку"],
    "gwm": ["gwm", "гвм"],
    "zeekr": ["zeekr", "зийкър", "зиикр", "зеекр", "зикр"],

    "land rover": [
        "rover",
        "land rover",
        "range rover",
        "ланд ровър",
        "ланд роувър",
        "ленд ровър",
        "ленд роувър"
        "рейндж роувър",
        "рейндж ровър"
        "ланд ровер рейндж ровер"
    ],
    "great wall":["great wall", "греат уол", "грейт уол", "греит лоу"],

    "schwarzmuller": ["schwarzmuller", "шварцмюлер", "schwarzm?ller", "schwarzmueller", "schwarzmüller"],
    "spitzer": ["spitzer", "шпицер", "шпитцер", "шпитсер"],

    "ozgul": ["ozgul", "озгул", "озгъл"],
    "berger": ["berger", "бергер"],
    "solaris": ["solaris", "соларис"],
    "bergerecotrail": ["bergerecotrail"],
    "zaslaw": ['zaslaw'],
    "kassbohrer": ["kassbohrer", "кесборер", "kasborer", "касборер"],
    "wielton": ["wielton", "виелтон", "виелтън", "вйелтон"],
    "kogel": ["kogel", "koegel", "кьогел"],
    "krone": ["krone", "кроне"],
    "schmitz": ["schmitz", "шмиц", "шмитц"],
    "lohr": ["lohr", "лор", "лохр", "евролор", "eurolohr"],
    "lamberet": ["lamberet", "ламбере"],
    "chereau": ["chereau", "шеро"],
    "feldbinder": ["feldbinder", "фелдбиндер"],
    "komatsu": ["komatsu", "комацу"],
    "liebherr": ["liebherr", "либхер"],
    "caterpillar": ["caterpillar", "катърпилър", "катърпилър", "катърпилар", "катърпилер"]
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



BRAND_ALIASES_2 = {
    "mercedes-benz": {
        "mercedes",
        "mercedes-benz",
        "мерцедес",
        "мерцедес-бенц",
        "мерцедес бенц",
        "mеrcedes-benz",
        "mercdes-benz",
        "mercedes-maybach",
        "maybach",
    },

    "renault": {
        "renault",
        "рено",
        "renaul",
        "renaut",
        "ренo",
    },

    "dacia": {
        "dacia",
        "дачия",
        "daciа",
    },

    "toyota": {
        "toyota",
        "тойота",
        "toyotа",
        "тoyota",
    },

    "kia": {
        "kia",
        "киа",
        "кia",
        "кiа",
    },

    "hyundai": {
        "hyundai",
        "хюндай",
        "hyunday",
        "huyndai",
        "хюндаи",
    },

    "peugeot": {
        "peugeot",
        "пежо",
        "реugeot",
        "пeжо",
    },

    "citroen": {
        "citroen",
        "ситроен",
    },

    "volkswagen": {
        "volkswagen",
        "vw",
        "фолксваген",
        "vokswagen",
        "volkwagen",
        "volswagen",
    },

    "skoda": {
        "skoda",
        "skoda",
        "шкода",
        "scoda",
    },

    "bmw": {
        "bmw",
        "бмв",
    },

    "audi": {
        "audi",
        "аudi",
    },

    "mazda": {
        "mazda",
        "мазда",
        "mаzda",
    },

    "nissan": {
        "nissan",
        "нисан",
        "nisssan",
    },

    "opel": {
        "opel",
        "опел",
    },

    "suzuki": {
        "suzuki",
        "сузуки",
    },

    "ford": {
        "ford",
        "форд",
    },

    "honda": {
        "honda",
        "хонда",
    },

    "volvo": {
        "volvo",
        "волво",
    },

    "lexus": {
        "lexus",
        "лексус",
    },

    "porsche": {
        "porsche",
        "порше",
        "porshe",
    },

    "fiat": {
        "fiat",
        "фиат",
    },

    "geely": {
        "geely",
        "джийли",
    },

    "byd": {
        "byd",
    },

    "dongfeng": {
        "dongfeng",
        "донгфенг",
        "donfeng",
        "dongeng",
        "dongfenh",
    },

    "haval": {
        "haval",
        "хавал",
    },

    "mg": {
        "mg",
    },

    "tesla": {
        "tesla",
        "тесла",
    },

    "subaru": {
        "subaru",
        "субару",
    },

    "mitsubishi": {
        "mitsubishi",
    },

    "jeep": {
        "jeep",
    },

    "land rover": {
        "rover",
        "land rover",
        "range rover",
    },

    "mini": {
        "mini",
    },

    "cupra": {
        "cupra",
    },

    "seat": {
        "seat",
        "сеат",
    },

    "lynk & co": {
        "lynk&co",
        "lynk",
        "lync&co",
    },

    "smart": {
        "smart",
    },
}



TRUCK_MODELS = {
    "daf": [
        "95",
        "95xf",
        "xf",
        "cf",
        "lf",
        "xf95",
        "xf105",
        "xf106",
        "xf480",
        "xf530",
        "cf75",
        "cf85",
        "cf410",
        "lf45",
        "lf55",
    ],

    "iveco": [
        "daily",
        "eurocargo",
        "eurotech",
        "eurostar",
        "stralis",
        "trakker",
        "s-way",
        "x-way",
        "t-way",
        "190e",
        "440e",
        "440s",
        "480",
        "500",
        "560",
        "40.10",
        "44.10",
        "44.12",
        "44.13",
        "44.14",
        "44.17",
        "44.20",
        "44.24",
        "44.32",
        "44.35",
        "44.36",
        "44.38",
        "44.42",
        "44.44",
        "44.46",
        "44.48",
        "44.52",
        "44.56",
        "44.60",
    ],

    "man": [
        "f90",
        "f2000",
        "tga",
        "tgx",
        "tgs",
        "tgl",
        "tgm",
        "tgm",
        "tgs",
        "18.440",
        "18.460",
        "18.480",
        "18.500",
        "18.510",
        "18.540",
        "26.320",
        "26.360",
        "26.400",
        "26.440",
    ],

    "mercedes": [
        "atego",
        "actros",
        "arocs",
        "axor",
        "econic",
        "unimog",
        "1622",
        "1824",
        "1831",
        "1835",
        "1840",
        "1844",
        "1845",
        "1846",
        "1848",
        "1851",
        "1853",
        "2544",
        "2644",
        "3340",
        "4140",
    ],

    "scania": [
        "p",
        "g",
        "r",
        "s",
        "l",
        "t",
        "4-series",
        "r420",
        "r440",
        "r450",
        "r470",
        "r480",
        "r500",
        "r520",
        "r560",
        "r580",
        "r620",
        "r650",
        "g410",
        "g450",
        "p360",
        "p380",
    ],

    "volvo": [
        "f10",
        "f12",
        "fh",
        "fh12",
        "fh13",
        "fh16",
        "fm",
        "fmx",
        "fe",
        "fl",
        "nh12",
        "fh420",
        "fh440",
        "fh460",
        "fh480",
        "fh500",
        "fh520",
        "fh540",
        "fh750",
        "fm380",
        "fm420",
        "fm440",
        "fm460",
    ],

    "renault": [
        "premium",
        "magnum",
        "kerax",
        "c",
        "d",
        "t",
        "k",
        "midlum",
        "midliner",
        "gamme t",
    ],

    "ford": [
        "cargo",
        "f-max",
        "fmax",
    ],

    "isuzu": [
        "n-series",
        "f-series",
        "giga",
        "elf",
        "forward",
    ],

    "fuso": [
        "canter",
        "fighter",
        "super great",
    ],

    "hino": [
        "300",
        "500",
        "700",
        "profia",
        "ranger",
    ],

    "kamaz": [
        "4310",
        "43118",
        "5320",
        "53212",
        "5410",
        "54115",
        "5490",
        "6520",
        "6522",
        "65225",
        "6540",
    ],

    "maz": [
        "4370",
        "5336",
        "5432",
        "5440",
        "6312",
        "6422",
        "6501",
    ],

    "gaz": [
        "gazelle",
        "gazon",
        "sadko",
        "3307",
        "3308",
        "3309",
    ],

    "ural": [
        "4320",
        "5557",
        "6370",
        "next",
    ],

    "tatra": [
        "815",
        "phoenix",
        "force",
        "terrno",
    ],

    "kenworth": [
        "t2000",
        "t600",
        "t660",
        "t680",
        "t800",
        "w900",
        "c500",
    ],

    "peterbilt": [
        "357",
        "367",
        "379",
        "389",
        "520",
        "567",
        "579",
    ],

    "mack": [
        "anthem",
        "granite",
        "pinnacle",
        "lr",
        "md",
    ],

    "freightliner": [
        "cascadia",
        "century",
        "columbia",
        "coronado",
        "m2",
        "114sd",
        "122sd",
    ],

    "western star": [
        "4700",
        "4800",
        "4900",
        "5700",
        "57x",
        "49x",
    ],

    "international": [
        "lt",
        "rh",
        "hx",
        "lonestar",
        "prostar",
        "transtar",
        "9900i",
    ],

    "sterling": [
        "a9500",
        "lt9500",
        "acter",
    ],

    "faw": [
        "j5",
        "j6",
        "j7",
    ],

    "shacman": [
        "f2000",
        "f3000",
        "x3000",
        "x5000",
        "m3000",
    ],

    "sinotruk": [
        "howo",
        "howo a7",
        "sitrak",
        "c7h",
    ],

    "dongfeng": [
        "kl",
        "kc",
        "kr",
        "dfh",
    ],

    "jac": [
        "n-series",
        "k7",
        "gallop",
    ],

    "ashok leyland": [
        "captain",
        "boss",
        "partner",
        "4825",
    ],

    "bharatbenz": [
        "1217",
        "1617",
        "2523",
        "2823",
        "3123",
        "3523",
        "4023",
    ],
}

SORTED_BRAND_LOOKUP = sorted(
        BRAND_ALIASES_2.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )




