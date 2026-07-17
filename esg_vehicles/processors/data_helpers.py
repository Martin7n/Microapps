from datetime import datetime, date


def text_normalization(text):
    return (str(text).strip() or "").lower()


def keyword_extract_list(text_list:list):
    return [text_normalization(item) for item in text_list]


def keywords_list_exraction_desc(text_list:list):
    combined_text = (" ".join(text_list)
                     .replace("  ", " ")
                     .split(" "))
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