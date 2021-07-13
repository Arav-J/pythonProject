import pytest
import requests
import json

"""
https://www.youtube.com/watch?v=byaxg00Gf9I
"""
# @pytest.mark.one
# def test_method():
#     x = 5
#     y = 10
#     assert x == y
#
#
# @pytest.mark.two
# def test_method2():
#     a = 15
#     b = 20
#     assert a+5 == b

# @pytest.fixture
# def numbers():
#     a = 10
#     b = 20
#     c = 25
#     return [a, b, c]
#
#
# def test_method1(numbers):
#     x = 15
#     assert numbers[0] == x
#
#
# def test_method2(numbers):
#     y = 20
#     assert numbers[1] == y
#
#
# def test_method3(numbers):
#     z = 25
#     assert numbers[2] == z


def main_url():
    return "https://reqres.in"


def test_valid_login(main_url):
    url = main_url + "/api/login/"
    data = {'email': 'abc@xyz.com', 'password': 'qwerty'}
    response = requests.get(url, data=data)
    t = json.loads(response.text)
    assert response.status_code == 200
    assert t['token'] == "QpwL5tke4Pnpja7X4"
