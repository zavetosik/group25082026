from app.project.utils import calculate_discount, is_even, get_full_name


def test_calculate_discount_1():
    price = 500
    discount = 20
    expected = 400
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_2():
    price = 500
    discount = 50
    expected = 250
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_3():
    price = 500
    discount = 0
    expected = 500
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_4():
    price = 0
    discount = 20
    expected = 0
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_5():
    price = 500
    discount = 60
    expected = 200
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_is_even_1():
    number = 4
    expected = True
    actual = is_even(number)
    assert expected == actual


def test_is_even_2():
    number = 5
    expected = False
    actual = is_even(number)
    assert expected == actual


def test_is_even_3():
    number = -6
    expected = True
    actual = is_even(number)
    assert expected == actual


def test_is_even_4():
    number = -7
    expected = False
    actual = is_even(number)
    assert expected == actual


def test_is_even_5():
    number = 0
    expected = True
    actual = is_even(number)
    assert expected == actual


def test_get_full_name_1():
    first_name = "Oleksandr"
    last_name = "Chykota"
    expected = "Oleksandr Chykota"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_2():
    first_name = "Sasha"
    last_name = "Chykota"
    expected = "Sasha Chykota"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_3():
    first_name = "Oleksandrionn"
    last_name = "Chykota"
    expected = "Oleksandrionn Chykota"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_4():
    first_name = "Oleksandr!"
    last_name = "Chykota!"
    expected = "Oleksandr! Chykota!"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_5():
    first_name = "Volodimyr"
    last_name = "Zelensky"
    expected = "Volodimyr Zelensky"
    actual = get_full_name(first_name, last_name)
    assert expected == actual