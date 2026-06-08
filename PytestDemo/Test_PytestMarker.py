import pytest 

@pytest.mark.smoke
def test_homepage_loads():
    assert True

@pytest.mark.regression
def test_login_successful():
    assert True

@pytest.mark.regression
def test_user_profile_update():
    assert True


@pytest.mark.skip(reason="Intentionally skip")
def test_skip():
    print("Fail")

@pytest.mark.xfail(reason="Intentional fail")
def test_ffail():
    print("Failed")

@pytest.mark.parametrize("test_input, expected", [(1,3),(3,6),(5,7)])
def test_addition(test_input, expected):
    assert test_input+2 == expected