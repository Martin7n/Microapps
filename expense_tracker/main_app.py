import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from dataentry import get_date, get_amount, get_description, get_category


# from variables import CSV_FIELDS

class CSV:
    CSV_FIELDS = ["date", "amount", "category", "description"]
    CSV_file = "fin_data.csv"
    DATEFORMAT = "%d-%m-%Y"

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.CSV_FIELDS)
            df.to_csv(cls.CSV_file, index=False)

    @classmethod
    def add_record(cls, date, amount, category, description):
        new_record = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_file, 'a', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.CSV_FIELDS)
            writer.writerow(new_record)
        print("Successfully added .....")


    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_file)
        df["date"] = pd.to_datetime(df["date"], format=CSV.DATEFORMAT)
        start_date = datetime.strptime(start_date, CSV.DATEFORMAT)
        end_date = datetime.strptime(end_date, CSV.DATEFORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No records to display")
        else:
            print(f"Transactions from {start_date.strftime(CSV.DATEFORMAT)} to {end_date.strftime(CSV.DATEFORMAT)}")
            print(filtered_df.to_string(
                index=False, formatters={"date": lambda x: x.strftime(CSV.DATEFORMAT)}
            ))
        total_income = filtered_df[filtered_df["category"]=="income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"]=="expense"]["amount"].sum()
        net_savings = total_income - total_expense
        print(f"Total income: {total_income:.2f}. \nTotal expense: {total_expense:.2f}")
        print(f"Net savings: {net_savings:.2f}")
        return filtered_df




def add():
    CSV.init_csv()
    date = get_date("Enter the date or enter for today: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_record(date, amount, category, description)

def plot_transactions(df):
    df.set_index("date", inplace=True)
    income_df = df[df['category'] == "income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df['category'] == "expense"].resample("D").sum().reindex(df.index, fill_value=0)
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df['amount'], label="income", color="g")
    plt.plot(expense_df.index, expense_df['amount'], label="expense", color="r")
    plt.xlabel("Date")

    plt.ylabel("Amount")
    plt.title("Your balance graph")
    plt.legend()
    plt.grid(True)
    plt.show()

def app_start():
    while True:
        print("\n 1. Add new transaction\n 2. View transactions and summary\n 3.Exit")
        command = input()
        if command == "1":
            add()
        elif command == "2":
            start_date = get_date("Enter a start date: ")
            end_date = get_date("Enter a end date: ")
            df = CSV.get_transactions(start_date, end_date)
            # plot_transactions(df)
            if input("Do you want to see a plot( y/n): ").lower() == "y":
                plot_transactions(df)

        elif command == "3":
            print("Exiting...")

            break

if __name__ == '__main__':
    # add()
    # CSV.get_transactions("01-01-1970", "01-01-2050")
    app_start()
