import pandas as pd


def dif_finder():


    # Next: - 1: GUI with file browser/feeder
    # Next: - 2: additional filtering of the dif.file
    # Next: - 3: visualization by cities
    # Next: - 4: timeline statistics


    old_df = pd.read_excel('kat_old.xlsx')
    new_df = pd.read_excel('kat_new.xlsx')

    merged_df = pd.merge(old_df, new_df, on=['ВИД МПС','МАРКА', 'МОДЕЛ'], suffixes=('_old', '_new'))

    cities = [col for col in old_df.columns if 'нови' in col or 'употр.' in col]
    # cities = [col for col in new_df.columns if 'нови' in col or 'употр.' in col]

    diffs = {}

    for city in cities:
        old_col = f"{city}_old"
        new_col = f"{city}_new"

        merged_df[f"{city}_diff"] = merged_df[new_col] - merged_df[old_col]

    print(merged_df[['ВИД МПС', 'МАРКА', 'МОДЕЛ'] + [f"{city}_diff" for city in cities]])

    # merged_df.to_excel('differences.xlsx', index=False)


    filtered_df = merged_df[(merged_df[[f"{city}_diff" for city in cities]] != 0).any(axis=1)]
    filtered_df.to_excel('differences_only.xlsx', index=False)

if __name__ == '__main__':
    dif_finder()