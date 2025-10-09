import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...


@pytest.mark.regression
class TestUserAuthentification:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password(self):
        ...

    def test_logout(self):
        ...


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.registration
def test_user_registration():
    pass


@pytest.mark.smoke
def test_user_login():
    pass


@pytest.mark.registration
@pytest.mark.regression
def test_password_reset():
    pass
