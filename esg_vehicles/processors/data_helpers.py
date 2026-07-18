from datetime import datetime, date
import re

def text_normalization(text):
    return (str(text).strip() or "").lower()


def keyword_extract_list(text_list:list):
    return [text_normalization(item) for item in text_list]


def keywords_list_exraction_desc(text_list:list):
    raw_joined = " ".join(text_list)
    cleaned_text = re.sub(r'[,/()]', ' ', raw_joined)
    combined_text = cleaned_text.split()

    # combined_text = (" ".join(text_list)
    #                  .replace(",", "")
    #                  .replace("  ", " ")
    #                  .split(" "))
    return keyword_extract_list(combined_text)



def prepare_excel_value(value):
    if value is None:
        return None

    if isinstance(value, (datetime, date)):
        return value

    if isinstance(value, str):
        value = value.strip()

        try:
            if value.isdigit():
                return int(value)
        except Exception:
            pass

        try:
            return float(value)
        except ValueError:
            pass

    return value

if __name__ == "__main__":
    a = "Ford e Transit VAN"
    b = text_normalization(a)
    # print(b)
    # print(keyword_extract_list(b))