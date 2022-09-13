import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    # 获取 driver
    def __init__(self, driver):
        """
        :param driver: 获取浏览器
        """
        self.driver = driver
        self.action = ActionChains(driver)

    # 查找元素（显式等待）
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        self.base_find_element(loc, timeout, poll).click()

    # 输入元素
    def base_input(self, loc, value, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param value: 输入的值
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        el = self.base_find_element(loc, timeout, poll)
        el.clear()
        el.send_keys(value)

    # 获取输入文本
    def base_input_get_value(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 输入的文本
        """
        return self.base_find_element(loc, timeout, poll).get_attribute('value')

    # 获取文本
    def base_get_text(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素的文本
        """
        return self.base_find_element(loc, timeout, poll).text.strip()

    # 获取元素属性
    def base_get_ele_attribute(self, loc, attribute, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param attribute: 元素属性
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素属性信息
        """
        return self.base_find_element(loc, timeout, poll).get_attribute(attribute)

    # 判断元素是否存在
    def base_ele_is_exist(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素是否存在
        """
        try:
            self.base_find_element(loc, timeout, poll)
            return True
        except:
            return False

    # 判断按钮元素是否可用
    def base_ele_is_enable(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素是否可用
        """
        return self.base_find_element(loc, timeout, poll).is_enabled()

    # 截图
    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))
        # self.driver.get_screenshot_as_file("../image/%s.png" %(time.strftime("%Y_%m_%d_%H_%M_%S")))
