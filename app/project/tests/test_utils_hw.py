import pytest

from utils import is_password_safe


class TestIsPasswordSafe:

    @pytest.mark.parametrize(
        'password, expected',
        [
            ("password!2" , True),
            ("passwo" , False),
            ("1213545435" , False),
            ("1213545435!@" , False),
            ("1213545435!@dedfdedd" , True),
            ("121" , False),
            ("@@@@@@@@!@!@!#$" , False),
            ("arabella123@" , True),
            ("arabella123@!@!@@" , True),
            ("nenenenennenene" , False),
        ]
    )
    def test_is_password_safe(self, password: str, expected: bool):
        actual = is_password_safe(password)
        assert expected is actual

    @pytest.mark.skip(reason="Test is not ready yet")
    def test_is_password_safe_2(self):
        pass
