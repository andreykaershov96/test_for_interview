from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class SearchPage:
    """Страница поиска"""

    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.CSS_SELECTOR, '.mini-suggest__input')
        self.suggest_box = (By.CSS_SELECTOR, '.mini-suggest__popup-content')
        self.result = (By.CSS_SELECTOR, '.serp-item.serp-item_card')
        self.link = (By.CSS_SELECTOR, '.Link.Link_theme_outer')
        self.menu_button = (By.CSS_SELECTOR, 'a[title="Все сервисы"]')
        self.menu = (By.CSS_SELECTOR, '.popup2__content-wrapper')
        self.service_button = (By.CSS_SELECTOR, '.services-more-popup__tab')
        self.category_button = (By.CSS_SELECTOR, '.home-link2.services-more-popup__item-link')

    def check_search_field(self, search_text=None):
        """Проверить что отобразилась строка поиска"""
        search_field = self.driver.find_element(*self.search_field)
        assert search_field.is_displayed(), "Поле поиска не отображается"
        if search_text:
            assert search_field.get_attribute("value") == search_text, "Текст в поле поиска отличается"

    def click_search_field(self):
        """Нажать в строку поиска"""
        self.driver.find_element(*self.search_field).click()

    def check_show_suggest(self):
        """Проверить что отобразилась таблица suggest"""
        suggest_field = self.driver.find_element(*self.suggest_box)
        assert suggest_field.is_displayed(), "Таблица с подсказками (suggest) не отображается на странице"

    def type_in_search(self, text):
        """
        Ввести тест в строку поиска
        :param text: текст для ввода
        :return:
        """
        search_field = self.driver.find_element(*self.search_field)
        search_field.send_keys(text)

    def check_result_search(self):
        """Проверка что отобразились результаты поиска"""
        result = self.driver.find_elements(*self.result)
        assert result, 'Страница результатов не появилась'

    def press_enter(self):
        """Нажать Enter"""
        search_field = self.driver.find_element(*self.search_field)
        search_field.send_keys(Keys.ENTER)

    def check_first_link(self, link_text):
        """
        Проверить первую ссылку на странице
        :param link_text: тест ссылки
        :return:
        """
        link = self.driver.find_element(*self.link)
        href = link.get_attribute("href")
        assert link_text in href, 'Страница результатов не появилась'

    def display_menu(self):
        """Проверка отображения меню"""
        menu = self.driver.find_element(*self.menu)
        assert menu.is_displayed(), 'Меню не отображается'

    def open_all_category(self):
        """Открыть меню категорий"""
        self.driver.find_element(*self.menu_button).click()

    def choose_category(self, category_name):
        """Открыть категорию"""
        self.driver.find_element(*self.service_button).click()
        category_list = self.driver.find_elements(*self.category_button)
        for category in category_list:
            if category.text == category_name:
                category.click()
                break
