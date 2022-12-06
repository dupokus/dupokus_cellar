from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("михайло", "міша", "кусень", "дупокус", "michael", "kusaka", "dupokus" "майкл"):
        return "Метал твердіший за плоть."

    if user_message in ("бот", "апаратус", "апаратус"):
        return "Запущений і готовий служити."

    if user_message in ("бліц"):
        return "Ходячого голема корозія не бере."

    if user_message in ("жарт"):
        return "Заходить жук в аптеку, каже: Добрий день у вас є мазззззззззззззь?\n-Є.\n-Ззззззаєбісь, щазззз намажжжжжусь."

    return "Хтось висрав хуйню в чат. Пум-ба-ба-пум."