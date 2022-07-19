from selene import have, be, command
from selene.support.shared import browser


def test_submit_form():
    browser.open('/text-box') #открыть страницу
    #browser.all('[здесь какой-то селектор]').with_(timeout=10).should(have.size(здесь количесчтво элементов))
    # ждать элементы+ измененный таймаут конкретно для этого = 10 сек

    browser.should(have.title("ToolsQA")) #проверка тайтла
    browser.should(have.title_containing("QA"))  #проверка тайтла на включение текста
    browser.element('[class~=main-header]').should(have.exact_text("Text Box")) #проверка текста в классе.
    # Точное совпадение текста, но не полное совпадение имени класса (css классу)

    browser.element('.main-header').should(have.exact_text("Text Box"))  #сокращение преддущего варианта
    browser.element('[class="main-header"]').should(have.text("Text Box"))  #проверка текста в классе. включение текста
    browser.element("#userName").type('yasha') #заполнить текстовое поле
    browser.element('#userEmail').type('test@test.ru')
    browser.element('#currentAddress').type('currentAddress')
    browser.element('#permanentAddress').type('permanentAddress')
    #browser.element('#submit').perform(command.js.scroll_into_view).click() #нажать на кнопку, проскролив до нее
    #browser.execute_script
     #   '''
      #  document.querySelectorAll("[id^=google_ads]")
      #  .forEach(element->element.remove())
      #  ''' #выполнить скрипт js
    browser.element('#submit').click() #нажать на кнопку без скрола

    browser.all('#output p').should(have.texts( #первый вариант прверки значения
        'yasha',
        'test@test.ru',
        'currentAddress',
        'permanentAddress'
    ))

    browser.all('#currentAddress')[1].should(have.text('currentAddress')) #второй вариант
    browser.element('#output #currentAddress').should(have.text('currentAddress'))  # третий вариант
    browser.element('#output').element('#currentAddress').should(have.text('currentAddress'))  # третий вариант
