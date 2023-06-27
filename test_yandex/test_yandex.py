from selenium import webdriver
from pages.search_page import SearchPage
from pages.image_page import ImagePage


class TestYandex:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.search_page = SearchPage(cls.driver)
        cls.image_page = ImagePage(cls.driver)

    def setup(self):
        self.driver.get("https://ya.ru/")

    def test_01_yandex_search(self):
        """Проверка поиска в яндекс"""
        # Введем в поиск Тензор
        self.search_page.check_search_field()
        self.search_page.type_in_search('Тензор')
        self.search_page.check_show_suggest()
        self.search_page.press_enter()

        # Проверим результат поиска
        self.search_page.check_result_search()
        self.search_page.check_first_link('tensor.ru')

    def test_02_yandex_picture(self):
        """Проверка картинок в яндекс"""
        # Откроем вкладку с картинками
        self.search_page.check_search_field()
        self.search_page.click_search_field()
        self.search_page.open_all_category()
        self.search_page.display_menu()
        self.search_page.choose_category('Картинки')
        self.image_page.check_url('https://yandex.ru/images/')
        category_name = self.image_page.open_first_category()
        self.search_page.check_search_field(category_name)

        # Проверим первую картинку
        self.image_page.open_first_picture()
        image_link_1 = self.image_page.get_image_link()
        self.image_page.check_image_link(image_link_1)

        # Проверим вторую картинку
        self.image_page.click_next_btn()
        image_link_2 = self.image_page.get_image_link()
        assert image_link_2 != image_link_1, "Картинка не сменилась"
        self.image_page.check_image_link(image_link_2)

        # Проверим что вернулись на первую картинку
        self.image_page.click_prev_btn()
        self.image_page.check_image_link(image_link_1)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
