import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.driver.find_element(*MainPageLocators.order_button_in_header).click()

    @allure.step('Кликнуть по кнопке "Заказать" на странице')
    def click_on_order_button_on_page(self):
        self.driver.find_element(*MainPageLocators.order_button_in_main).click()

    @allure.step('Кликнуть по "Самокат" в лого хэдера')
    def click_header_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.header_logo_scooter).click()

    @allure.step('Кликнуть по "Яндекс" в лого хэдера')
    def click_header_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.header_logo_yandex).click()