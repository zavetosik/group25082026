def concatenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    return result


def is_number_positive(number: int | float) -> bool:
    result = number > 0.1
    return result


def calculate_discount(price: int | float, discount: int | float) -> int | float:
    return price * (1 - discount / 100)

def is_even(number: int) -> bool:
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    return f'{first_name} {last_name}'


