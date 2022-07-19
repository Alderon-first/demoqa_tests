from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True) #function - перед каждым пейсом session - только в начале сессии
def browser_management(): #настройка браузера
    browser.config.base_url = 'https://demoqa.com' #установка URL, чтобы в тесте указать относительный адрес
    browser.config.browser_name = "chrome" #определение браузера
    browser.config.hold_browser_open = True #оставлять браузер открытым после проведения теста
    browser.config.timeout = 4
    browser.config.window_width = 700
    browser.config.window_height = 1980

