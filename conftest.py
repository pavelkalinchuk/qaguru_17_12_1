from selene import browser
import pytest
from selenium import webdriver
from allure_attach import *


@pytest.fixture(scope="session", autouse=True)
def browser_start():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    selenoid_capabilities = {
        "browserName": "chrome",  # тип браузера
        "browserVersion": "125",  # версия браузера
        "selenoid:options": {  # установка разрешения на запись видео во время теста
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver_options.capabilities.update(selenoid_capabilities)

    selenoid_url = 'https://user1:1234@selenoid.autotests.cloud/wd/hub'
    driver = webdriver.Remote(command_executor=selenoid_url, options=driver_options)

    browser.config.driver = driver
    browser.open('https://demoqa.com/automation-practice-form')

    yield browser

    # прикрепляем скриншоты, логи браузера, html-код страницы, видеозапись теста
    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
