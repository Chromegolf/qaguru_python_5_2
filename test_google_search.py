from selene.support.shared import browser
from selene import be, have

randomParam = 'qwerty123sdsdsdsskdkadsj'


def test_success_search(set_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_failed_search(set_browser):
    browser.element('[name="q"]').should(be.blank).type(randomParam).press_enter()
    browser.element('[id="cnt"]').should(have.text(f'По запросу {randomParam} ничего не найдено.'))
    print('По данному запросу ничего не найдено')
