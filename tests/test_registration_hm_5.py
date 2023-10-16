from selene import browser, be, have, command
import os.path


def test_success_registration():
    browser.open('/automation-practice-form')

    # Ввод личных данных
    browser.element('#firstName').should(be.blank).type('Anastasia')
    browser.element('#lastName').should(be.blank).type('Flo')
    browser.element('#userEmail').should(be.blank).type('test@gmail.com')
    browser.element('label[for=gender-radio-2]').click()
    browser.element('#userNumber').should(be.blank).type('9999999999')
    browser.element('#dateOfBirthInput').should(be.not_.blank).click()
    browser.element('.react-datepicker__year-select').click().element('[value="1995"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
    browser.element('.react-datepicker__day--004').click()

    browser.element('label[for=hobbies-checkbox-1]').perform(command.js.scroll_into_view)

    # Выбор предмета и хобби
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()

    # Выбор картинки
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/pngwing.com (1).png'))

    # Ввод адреса
    browser.element('#currentAddress').should(be.blank).type('LS')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    # Кнопка Submit
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').execute_script('element.click()')

    # Проверка появления модального окна об успешной регистрации
    browser.element('.modal-content').element('.modal-header').should(have.text('Thanks for submitting the form'))

    # Проверка данных
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
        'Anastasia Flo',
        'test@gmail.com',
        'Female',
        '9999999999',
        '04 December,1995',
        'Computer Science',
        'Sports',
        'pngwing.com (1).png',
        'LS',
        'Uttar Pradesh Lucknow'))
