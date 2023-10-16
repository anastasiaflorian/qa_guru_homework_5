from selene import browser, be, have, command
import os.path



def test_fill__registration_form():
    browser.open("/automation-practice-form")
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Петров')
    browser.element('#userEmail').type('petrov@gmail.com')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').type('9001010800')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="0"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1998"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    browser.element('#subjectsInput').type('Chemistry').press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    # browser.element('#uploadPicture').send_keys(os.path.abspath('img/img.png'))
    browser.element('#currentAddress').type('12 street')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'Иван Петров',
        'petrov@gmail.com',
        'Male',
        '9001010800',
        '08 January,1998',
        'Chemistry',
        'Sports',
        '12 street',
        'Haryana Karnal'))