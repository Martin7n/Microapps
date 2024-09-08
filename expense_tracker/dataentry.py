from  datetime import datetime

DATEFORMAT = "%d-%m-%Y"
CATEGORIES = {'I': "income", "E": "expense"}
def get_date(prompt, allow_default=True):
    date_entry = input(prompt)
    if allow_default and not date_entry:
        return datetime.today().strftime(DATEFORMAT)
    try:
        valid_date = datetime.strptime(date_entry, DATEFORMAT)
        return valid_date.strftime(DATEFORMAT)
    except ValueError:
        print("Invalid date")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        expense = float(input("Enter the amount: "))
        if expense < 0:
            raise ValueError("Please enter correct amount")
    except ValueError as e:
        print(e)
        return get_amount()
    return expense


def get_category():
    category = input("Enter the category 'i' for income, 'e' for expense: ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Enter a valid category")
    return get_category()


def get_description():
    description = input("Enter the description: ")
    return  description if description else " "

if __name__ == "__main__":
    pass