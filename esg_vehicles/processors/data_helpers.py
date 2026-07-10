from datetime import datetime, date


def text_normalization(text):
    return (str(text) or "").lower()


def keyword_extract_list(text_list:list):
    return [text_normalization(item) for item in text_list]



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