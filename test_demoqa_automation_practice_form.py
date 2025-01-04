import allure
from selene import browser, be, have
import os


@allure.title("Тестирование формы регистрации")
def test_practice_form():
    with allure.step("Заполняем поля 'First Name' и 'Last Name' в блоке 'Name'"):
        browser.element('[id="firstName"]').click().type("Pavel")
        browser.element('[id="lastName"]').click().type("Kalinchuk")

    with allure.step("Заполняем поле с электронной почтой в блоке 'Email'"):
        browser.element('[id="userEmail"]').click().type("pavelkalinchuk@mail.tst")

    with allure.step("Выбираем пол в блоке 'Gender'"):
        browser.element('label[for="gender-radio-1"]').click()

    with allure.step("Заполняем поле номером мобильного телефона в блоке 'Mobile'"):
        browser.element('#userNumber').click().type("8992367011")

    with allure.step("Заполняем поле с днём рождения в блоке 'Date of Birth'"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker-popper').should(be.visible)
        browser.element('.react-datepicker__month-select').should(be.visible).element('[value="0"]').click()
        browser.element('.react-datepicker__year-select').should(be.visible).element('[value="2000"]').click()
        browser.element('.react-datepicker__week').should(be.visible).element('.react-datepicker__day.react'
                                                                              '-datepicker__day--001').click()
    with allure.step("Заполняем поле с предметными областями в блоке 'Subject'"):
        browser.element('#subjectsInput').click().type("computer")
        browser.element('#react-select-2-option-0').click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")

    with allure.step("Выбираем хобби в блоке 'Hobbies'"):
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()

    with allure.step("Добавляем картинку в блоке 'Picture'"):
        browser.element('#uploadPicture').send_keys(os.path.abspath('test_file.png'))

    with allure.step("Заполняем поле 'Current Address'"):
        browser.element('#currentAddress').should(be.visible).click().send_keys("г. Москва, ул. 1-я Строителей, д.1, кв.1")
        browser.driver.execute_script("window.scrollBy(0,400)", "")

    with allure.step("Выбираем  'State' и 'City' в блоке 'State and City'"):
        browser.element('#state').should(be.visible).click().element('#react-select-3-option-3').click()
        browser.element('#city').should(be.visible).click().element('#react-select-4-option-1').click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")

    with allure.step("Кликаем на кнопке 'Submit'"):
        browser.element("#submit").click()

    with allure.step("Выполняем проверку заполненной формы"):
        assert browser.element('.table-responsive').should(have.text("Pavel"))
        assert browser.element('.table-responsive').should(have.text("Kalinchuk"))
        assert browser.element('.table-responsive').should(have.text("pavelkalinchuk@mail.tst"))
        assert browser.element('.table-responsive').should(have.text("8992367011"))
        assert browser.element('.table-responsive').should(have.text("01 January,2000"))
        assert browser.element('.table-responsive').should(have.text("Computer Science"))
        assert browser.element('.table-responsive').should(have.text("Sports"))
        assert browser.element('.table-responsive').should(have.text("Music"))
        assert browser.element('.table-responsive').should(have.text("test_file.png"))
        assert browser.element('.table-responsive').should(have.text("г. Москва, ул. 1-я Строителей, д.1, кв.1"))
        assert browser.element('.table-responsive').should(have.text("Rajasthan"))
        assert browser.element('.table-responsive').should(have.text("Jaiselmer"))

    with allure.step("Закрываем окно с данными по регистрации"):
        browser.element('.modal-footer').click()
