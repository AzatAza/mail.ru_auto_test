from selenium.webdriver.common.by import By


class LoginLocators:
    LOGOUT_BTN = (By.XPATH, '//*[@id="mailbox"]/div[1]/div/a[4]/svg')
    LOGIN_BTN = (By.XPATH, '//*[@id="mailbox"]/div[1]/button')
    POPUP_WINDOW = (By.XPATH, "//iframe[@class='ag-popup__frame__layout__iframe']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='username']")
    ENTER_PASSWORD_BTN = (By.XPATH, "//button[@type='submit']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SIGN_IN_BTN = (By.XPATH, "//button[@type='submit']")
    NEW_LETTER_BTN = (By.XPATH, '//a[contains(@href, "compose")]')
    RECIPIENT_FIELD = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]'
                                 '/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')
    INPUT_LETTER_FIELD = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]'
                                    '/div[2]/div[3]/div[5]/div/div/div[2]/div[1]')
    SEND_BTN = (By.CLASS_NAME, 'button2__txt')
    LETTER_SENT = (By.CLASS_NAME, 'layer__link')
