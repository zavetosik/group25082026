def concatenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    return result


def is_number_positive(number: int | float) -> bool:
    result = number > 0
    # print('look here', number, result)
    return result


def is_password_safe(password: str) -> bool:
    has_8letters = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_symbols = any(not char.isalnum() for char in password)
    has_space = any(char.isspace() for char in password)
    if has_8letters and has_digit and has_letter and has_symbols and not has_space:
        return True
    else:
        return False
