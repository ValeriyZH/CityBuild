import time
import requests
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasePage:

    def assertElementsIsPresentByXpatch(self, xpath_elements):
        try:
            elements = self.find_elements_by_xpath(xpath_elements)
            return [True, len(elements)]
        except NoSuchElementException:
            return [False, 0]

    def assertElementIsPresentByXPath_Click(self, xpath, msg=None):
        try:
            element = self.find_element_by_xpath(xpath).click()
            return True
        except NoSuchElementException:
            return (False)

    def assertElementIsPresentByXPath_Send(self, xpath_input, send_message):
        try:
            element = self.find_element_by_xpath(xpath_input).send_keys(send_message)
            return True
        except NoSuchElementException:
            return (False)

    def element_exists_and_click(self, xpath):
        assert BasePage.assertElementIsPresentByXPath_Click(self, xpath), f'Элемента {xpath} на странице нет'

    def element_exists_and_send(self, xpath_input, send_message) -> object:
        assert BasePage.assertElementIsPresentByXPath_Send(self, xpath_input,
                                                           send_message), f'Элемента {xpath_input} на странице нет'

    def element_exists_count(self, xpath_elements):
        elements_array = BasePage.assertElementsIsPresentByXpatch(self, xpath_elements)
        assert elements_array[0], f'Элементов {xpath_elements} на странице нет'
        return elements_array

    def scroll_down_link_click(self, xpath_down_link):

        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        assert BasePage.assertElementIsPresentByXPath_Click(self,
                                                            xpath_down_link), f'Элемент {xpath_down_link} внизу страницы не обнаружен'

    def drop_down_element_click(self, xpath_drop_down_list, element_text):

        element = self.find_element_by_xpath(xpath_drop_down_list)
        element.click()
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("text") == element_text:  # print("Value is: %s" % option.get_attribute("value"))
                option.click()
                break

    def element_exists_and_click_enter(self, xpath_element):
        self.find_element_by_xpath(xpath_element).send_keys(Keys.RETURN)

    def autorization_user(self, url, login, password):
        session = requests.Session()
        session.post(url, {
            'username': login,
            'password': password,
            'remember': 1,
        })

    def uploading_file(self, xpath_input_file, file_path):
        self.find_element(By.XPATH, xpath_input_file).send_keys(file_path)

    def logging_file(log_file):
        logger.remove()
        logger.add(log_file, level='INFO',
                   format="<lvl>[</lvl><c>{time:DD.MM.YYYY HH:mm:ss.SSS}</c><lvl>]</lvl> <lvl>{message}</lvl>",
                   catch='True')

    def element_exists_array(self, xpath_elements):
        elements_array = self.find_elements(By.XPATH, xpath_elements)
        assert elements_array[0], f'Элементов {xpath_elements} на странице нет'
        return elements_array

    def switch_to_current_window(self):
        self.switch_to.active_element
        handles = self.window_handles
        for handle in handles:
            if self.current_window_handle != handle:
                # Закрываем первое окно
                self.close()
                # переключаемся на второе окно', handle
                self.switch_to.window(handle)

    def element_href_return(self, xpath_element):
        element = self.find_element_by_xpath(xpath_element)
        return element.get_attribute('href')

    def drop_down_select_value(self, xpath_drop_down, drop_down_value):
        select = Select(self.find_element_by_xpath(xpath_drop_down))
        # select by value
        select.select_by_value(drop_down_value)

    def drop_down_select_text(self, xpath_drop_down, drop_down_text):
        select = Select(self.find_element_by_xpath(xpath_drop_down))
        # select by visible text
        select.select_by_visible_text(drop_down_text)

    def clear_element_input(self, xpath_element):
        element = self.find_element_by_xpath(xpath_element)
        element.clear()

    def get_text_of_element(self, xpath_element):
        element = self.find_elements_by_xpath(xpath_element)
        return element.text
