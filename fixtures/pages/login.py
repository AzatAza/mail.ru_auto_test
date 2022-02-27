import logging
import time

from fixtures.locators.login import LoginLocators
from fixtures.models.login import LoginData
from fixtures.pages.base_page import BasePage


logger = logging.getLogger("test")


class LoginPage(BasePage):

    def auth(self, data: LoginData):
        """
        Auth function
        If account login → logout → login
        """
        logger.info(f"Login with email {data.email}, password {data.password}")
        if self.is_element_present(locator=LoginLocators.LOGOUT_BTN):
            self.click_element(locator=LoginLocators.LOGOUT_BTN)
        self.click_element(locator=LoginLocators.LOGIN_BTN)
        self.frame_switch(locator=LoginLocators.POPUP_WINDOW)
        self.click_element(locator=LoginLocators.EMAIL_INPUT)
        self.fill_element(data=data.email, locator=LoginLocators.EMAIL_INPUT)
        self.click_element(locator=LoginLocators.ENTER_PASSWORD_BTN)
        time.sleep(3)  # We get the ElementNotInteractableException, if it doesn't use time.sleep
        self.fill_element(data=data.password, locator=LoginLocators.PASSWORD_INPUT)
        self.click_element(locator=LoginLocators.SIGN_IN_BTN)
        self.frame_return()

    def send_letter(self):
        """
        Click "Compose a letter"
        Fill in recipient and letter text
        Send it
        """
        self.click_element(locator=LoginLocators.NEW_LETTER_BTN)
        self.fill_element(LoginData.random_text().recipient, locator=LoginLocators.RECIPIENT_FIELD)
        self.fill_element(LoginData.random_text().lorem_ipsum, locator=LoginLocators.INPUT_LETTER_FIELD)
        self.click_element(locator=LoginLocators.SEND_BTN)
