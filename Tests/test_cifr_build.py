import datetime
import os
import sys
import time

sys.path.append(os.path.abspath('/home/gm/PycharmProjects/CifrBuild/'))
from base_page import BasePage as Base
from selectorss import Selectorss as S
from data import Data as D
from loguru import logger


def __init__(self, browser):
    self.browser = browser



@logger.catch
def test_primer(browser):
    global new_page
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ КОМПАНИИ "ЦИФРОВАЯ СТРОЙКА"')

    logger.info('# установили максимальный размер окна браузера')
    browser.maximize_window()

    message_in_log = '# заходим на стартовую страницу' + D.start_url
    logger.info(message_in_log)
    browser.get(D.start_url)

    logger.info('# переходим в "Admin Back-End"')
    Base.element_exists_and_click(browser, S.xpath_admin_backend)

    logger.info('# делаем открывшуюся вкладку основной и активной, закрываем старую вкладку')
    Base.switch_to_current_window(browser)

    logger.info('# сейчас текущий upl:')
    url = browser.current_url
    message_in_log = '# ' + str(url)
    logger.info(message_in_log)

    logger.info('# вводим логин"')
    Base.element_exists_and_send(browser, S.xpath_login, D.login)

    logger.info('# вводим пароль')
    Base.element_exists_and_send(browser, S.xpath_password, D.password)

    logger.info('# нажимаем кнопку "login"')
    Base.element_exists_and_click(browser, S.xpath_autorization_enter)

    logger.info('# вошли и на новой странице нажимаем кнопку "SMS PAGES"')
    Base.element_exists_and_click(browser, S.xpath_sms_pages)

    logger.info('# перешли на страницу с смс и нажимаем на кнопку "ADD"')
    Base.element_exists_and_click(browser, S.xpath_sms_add)

    logger.info('# перешли на страницу создания смс и вводим данные в поле "Page Title"')
    Base.element_exists_and_send(browser, S.xpath_page_title, D.for_Page_Title)

    logger.info('# сначала поле "Status" специально переключаю в "Disable"')
    Base.drop_down_select_value(browser, S.xpath_Status, D.status2)

    logger.info('# смотрю результат')
    time.sleep(2)

    logger.info('# а потом обратно переключаю его ("Status") в "Enable"')
    Base.drop_down_select_value(browser, S.xpath_Status, D.status1)

    logger.info('# сначала поле "Target" специально переключаю в "Blank"')
    Base.drop_down_select_value(browser, S.xpath_Target, D.target2)

    logger.info('# смотрю результат')
    time.sleep(2)

    logger.info('# а потом обратно переключаю его ("Target") в "Self"')
    Base.drop_down_select_value(browser, S.xpath_Target, D.target1)

    logger.info('# в поле "Link" вводим произвольную ссылку')
    Base.element_exists_and_send(browser, S.xpath_Link, D.for_Link)

    logger.info('# в поле "Icon" вводим рандомный текст')
    Base.element_exists_and_send(browser, S.xpath_Icon, D.for_Icon)

    logger.info('# очищаем поле "Permalink"')
    Base.clear_element_input(browser, S.xpath_permalink)

    logger.info('# вводим данные в поле "Permalink"')
    Base.element_exists_and_send(browser, S.xpath_permalink, D.for_Permalink)

    logger.info('# вводим данные в поле "Keywords"')
    Base.element_exists_and_send(browser, S.xpath_Keywords, D.for_Keywords)

    logger.info('# вводим данные в поле "Descrption"')
    Base.element_exists_and_send(browser, S.xpath_Description, D.for_Description)

    logger.info('# кликаем на кнопку "Source"')
    Base.element_exists_and_click(browser, S.xpath_Source)

    logger.info('# вводим данные в поле ввода текста сообщения')
    Base.element_exists_and_send(browser, S.xpath_input_area, D.for_input_area)

    logger.info('# кликаем на кнопку "SUBMIT"')
    Base.element_exists_and_click(browser, S.xpath_Submit_button)

    logger.info('# сейчас текущий upl:')
    url = browser.current_url
    message_in_log = '# ' + str(url)
    logger.info(message_in_log)
    middle_url = url

    logger.info('# находим в списке нашу смс, помещаем значения её полей в список')
    for j in range(100):
        xpath_sms_in_list = '//tr[@class="' + D.class_in_list_sms + str(j) + '"' + ']/td'
        elements_array = Base.element_exists_array(browser, xpath_sms_in_list)
        for i in elements_array:
            if D.for_Page_Title in i.text:
                message_in_log = '# смс с Content Page Title = ' + '"' + D.for_Page_Title + '"' + ' на странице есть'
                logger.info(message_in_log)
                break
        if message_in_log == '# смс с Content Page Title = ' + '"' + D.for_Page_Title + '"' + ' на странице есть':
            break

    url = D.finish_url + D.for_Permalink
    message_in_log = '# заходим на  страницу ' + url
    logger.info(message_in_log)
    browser.get(url)

    logger.info('# делаем открывшуюся вкладку основной и активной, закрываем старую вкладку')
    Base.switch_to_current_window(browser)

    logger.info('# сейчас текущий upl:')
    url = browser.current_url
    message_in_log = '# ' + str(url)
    logger.info(message_in_log)

    logger.info('# проверяем заголовок страницы на соответствие заголовку смс')
    elements_array = Base.element_exists_array(browser, S.xpath_h2)
    message_in_log = '# WARNING! Заголовок страницы НЕ содержит Content Page Title = ' + '"' + D.for_Page_Title + '"'
    for i in elements_array:
        if D.for_Page_Title in i.text:
            message_in_log = '# заголовок страницы содержит Content Page Title = ' + '"' + D.for_Page_Title + '"'
    logger.info(message_in_log)

    logger.info('# проверяем текст страницы на соответствие тексту смс')
    message_in_log = '# WARNING! Текст страницы НЕ содержит Content Text SMS = ' + '"' + D.for_input_area + '"'
    elements_array = Base.element_exists_array(browser, S.xpath_sms_text)
    for i in elements_array:
        if D.for_input_area in i.text:
            message_in_log = '# текст страницы содержит Content Text SMS = ' + '"' + D.for_input_area + '"'
    logger.info(message_in_log)

    message_in_log = '# переходим обратно на  страницу ' + middle_url
    logger.info(message_in_log)
    browser.get(middle_url)

    logger.info('# делаем открывшуюся вкладку основной и активной, закрываем старую вкладку')
    Base.switch_to_current_window(browser)

    logger.info('# находим в списке нашу смс, помещаем значения её полей в список')
    for j in range(100):
        xpath_sms_in_list = '//tr[@class="' + D.class_in_list_sms + str(j) + '"' + ']/td'
        elements_array = Base.element_exists_array(browser, xpath_sms_in_list)
        for i in elements_array:
            if D.for_Page_Title in i.text:
                message_in_log = '# выделяем нашу смс - ставим "галочку" в нужной строке'
                logger.info(message_in_log)
                xpath_checkbox_sms = xpath_sms_in_list + '/input'
                Base.element_exists_and_click(browser, xpath_checkbox_sms)
                logger.info('# удаляем нашу смс - нажимаем кнопку удаления выбранных собщений')
                Base.element_exists_and_click(browser, S.xpath_delete_sms_button)

                break
        if message_in_log == '# выделяем нашу смс - ставим "галочку" в нужной строке':
            break

    logger.info('# подтверждаем свое действие - нажимаем "ОК" во всплывающем окне')
    browser.switch_to.alert.accept()

    time.sleep(7)
    logger.info('# ЗАВЕРШИЛИ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ КОМПАНИИ "ЦИФРОВАЯ СТРОЙКА"')
