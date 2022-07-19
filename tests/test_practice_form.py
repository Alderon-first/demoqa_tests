from selene import have, be, command
from selene.support.shared import browser
import os



def test_practice_form():
    browser.open('/automation-practice-form')
    #
    browser.element('#firstName').type('Имя') #заполнить текстовое поле
    browser.element('#lastName').type('Отчество')
    browser.element('#userEmail').type('test@test.ru')
    browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text('Other')).click()
    browser.element('#userNumber').type('7777777777')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1990"]').click()
    browser.element('.react-datepicker__month-select [value="11"]').click()
    browser.element('.react-datepicker__day--002').click()

    browser.element('#subjectsInput').type('Arts').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('C:/Users/Alderon/MSP/test/4.jpg'))

    browser.element('#currentAddress').type('currentAddress')

    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()
    #
    browser.all('.table-responsive').all('tr').element(1).should(have.text('Имя Отчество'))
    browser.all('.table-responsive').all('tr').element(2).should(have.text('test@test.ru'))
    browser.all('.table-responsive').all('tr').element(3).should(have.text('Other'))
    browser.all('.table-responsive').all('tr').element(4).should(have.text('7777777777'))
    browser.all('.table-responsive').all('tr').element(5).should(have.text('02 December,1990'))
    browser.all('.table-responsive').all('tr').element(6).should(have.text('Arts'))
    browser.all('.table-responsive').all('tr').element(7).should(have.text('Sports'))
    browser.all('.table-responsive').all('tr').element(8).should(have.text('4.jpg'))
    browser.all('.table-responsive').all('tr').element(9).should(have.text('currentAddress'))
    browser.all('.table-responsive').all('tr').element(10).should(have.text('NCR Delhi'))

