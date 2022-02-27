from fixtures.constans import Constants
from fixtures.locators.login import LoginLocators


class TestLogin:
    def test_send_letter(self, app, user_data):
        """
        Steps:
        1. Open auth page
        2. Auth with valid data
        3. Write and send letter
        4. Check result
        """
        app.open_login_page()
        app.login.auth(data=user_data)
        app.login.send_letter()
        assert app.login.get_text(locator=LoginLocators.LETTER_SENT) == Constants.LETTER_SENT
