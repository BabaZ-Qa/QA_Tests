import pytest
from Tests_Pages.Loginpage import LoginPage


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_verify_logins(self):
        loginpage = LoginPage(self.driver)
        loginpage.login_page("student", "Password123")
        mesaj = loginpage.login_messages()
        assert mesaj == "Logged In Successfully"
