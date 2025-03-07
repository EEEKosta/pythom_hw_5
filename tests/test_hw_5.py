from selene import browser, have, be
import os

def test_submitting_form():
    browser.open('/automation-practice-form')
    browser.element('[class=practice-form-wrapper]').element('[class=text-center]').should(have.text('Practice Form'))
    # Заполняем firstName, lastName, Email
    browser.element('#userName-wrapper').element('#firstName').should(be.blank).type('Kostya')
    browser.element('#userName-wrapper').element('#lastName').should(be.blank).type('Egorov')
    browser.element('#userEmail').should(be.blank).type('email@example.com')
    # Выбираем пол
    browser.element('#genterWrapper').all('.custom-control-label').should(have.exact_texts('Male', 'Female', 'Other'))
    browser.element('#genterWrapper').element('[for=gender-radio-1]').click()
    # заполняем номер
    browser.element('#userNumber').should(be.blank).type('1234567890')
    # заполняем дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click().element('option[value="2"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1993"]').click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').type('Magic')
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').type(os.path.abspath('screen.png'))
    browser.element('#currentAddress').type('Rostov, Lenina 1')
    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-2').click()
    # сохраняем форму
    browser.element('#submit').click()
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    # проверяем данные в таблице
    browser.element(".table-dark").should(have.text('Kostya Egorov'))
    browser.element(".table-dark").should(have.text('email@example.com'))
    browser.element(".table-dark").should(have.text('Male'))
    browser.element(".table-dark").should(have.text('1234567890'))
    browser.element(".table-dark").should(have.text('14 March,1993'))
    browser.element(".table-dark").should(have.text('Magic'))
    browser.element(".table-dark").should(have.text('Sports'))
    browser.element(".table-dark").should(have.text('screen.png'))
    browser.element(".table-dark").should(have.text('Rostov, Lenina 1'))
    browser.element(".table-dark").should(have.text('Uttar Pradesh Merrut'))
    # закрываем таблицу
    browser.element('.modal-content').element('#closeLargeModal').click()