import csv




''''
ID	Country	VFN	Mp	Mh	Man	MMS	Tan	T	Va	Ve	Mk	Cn	Ct	Cr	r	m (kg)	Mt	Enedc (g/km)	Ewltp (g/km)	Ft	Fm	ec (cm3)	ep (KW)	z (Wh/km)	IT	Ernedc (g/km)	Erwltp (g/km)	De	Vf	Status	year	Date of registration	Fuel consumption	ech	RLFI	Electric range (km)

'''
def file_read(filename):
    count = 0
    approval_types = {}
    with open(filename, newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            type, mark,model,cat, fuel = row[7], row[11], row[12], row[13], row[20]
            if type not in approval_types:
                approval_types[type] = []
            approval_types[type].append([type, mark,model,cat, fuel ])
            count += 1
            # for x in row:
            #     print(x)
            # type = row[7]
            # # type = "aa"
            # if type not in approval_types:
            #     approval_types[type] = []
            # approval_types[type].append(row)
            # count += 1
            # print(', '.join(row))
            if count == 15:
                break
    print(approval_types)

def field_list():
    label_list = []
    lst = ["/", "(", ")"]
    idx = 0
    while True:

        text = input()
        if text == "exit":
            break
        label_value = "".join([z for z in text if z not in lst])
        label_value = label_value.replace(" ", "")
        label_list.append(f"{label_value.lower()}={idx}")
        idx += 1
    [print(x) for x in label_list]

if __name__=='__main__':
    file_read("C:\\Users\\M\\Downloads\\data.csv")
    # field_list()