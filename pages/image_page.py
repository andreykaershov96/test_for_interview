from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ImagePage:
    """Страница с картинками"""

    def __init__(self, driver):
        self.driver = driver

        self.first_category = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
        self.first_picture = (By.CSS_SELECTOR, '.serp-item_pos_0')
        self.image_link = (By.CSS_SELECTOR, '.MMImage-Origin')
        self.image = (By.CSS_SELECTOR, '.MediaViewer-View.MediaViewer_theme_fiji-View')
        self.next_btn = (By.CSS_SELECTOR, '.CircleButton_type_next')
        self.prev_btn = (By.CSS_SELECTOR, '.CircleButton_type_prev')

    def check_url(self, url):
        """Переключить вкладку и проверить адрес страницы"""
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == url, 'Не открылась нужная страница'

    def open_first_category(self):
        """Открыть первую категорию"""
        first_category = self.driver.find_element(*self.first_category)
        first_category.click()
        return first_category.text

    def open_first_picture(self):
        """Открыть первое изображение"""
        wait = WebDriverWait(self.driver, 10)
        first_picture = wait.until(EC.element_to_be_clickable(self.first_picture))
        first_picture.click()

    def click_next_btn(self):
        """Нажать кнопку далее"""
        next_button = self.driver.find_element(*self.next_btn)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(next_button)
        action_chains.perform()
        next_button.click()
        self.driver.implicitly_wait(5)

    def click_prev_btn(self):
        """Нажать кнопку назад"""
        preview_button = self.driver.find_element(*self.prev_btn)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(preview_button)
        action_chains.perform()
        preview_button.click()
        self.driver.implicitly_wait(5)

    def check_image_link(self, link):
        """Проверить ссылку изображения"""
        image_link = self.driver.find_element(*self.image_link)
        assert image_link.get_attribute("src") == link, "Ссылка отличается"

    def get_image_link(self):
        """Получить ссылку на изображение"""
        image = self.driver.find_element(*self.image)
        assert image.is_displayed(), "Картинка не отображается"
        image_link = self.driver.find_element(*self.image_link)
        return image_link.get_attribute("src")
