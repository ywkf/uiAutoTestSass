import time

import allure
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog
log = GetLog.get_logger()


class Base:

    # 初始化
    def __init__(self, driver):
        """
        :param driver: 获取浏览器
        """
        log.info("正在初始化 driver: {}".format(driver))
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
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        log.info("正在对：{} 元素执行点击操作！".format(loc))
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
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        log.info("正在对：{} 元素执行输入：{} 操作！".format(loc, value))
        el.send_keys(value)

    # 获取输入文本
    def base_get_input_value(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 输入的文本
        """
        value = self.base_find_element(loc, timeout, poll).get_attribute('value')
        log.info("正在对：{} 元素获取输入文本操作！，输入的文本值：{}".format(loc, value))
        return value

    # 获取文本
    def base_get_text(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素的文本
        """
        text = self.base_find_element(loc, timeout, poll).text.strip()
        log.info("正在对：{} 元素获取文本操作！，获取的文本值：{}".format(loc, text))
        return text

    # 获取文本列表
    def base_get_text_list(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return:
        """
        text_list = []
        ele_list = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        for ele in ele_list:
            text = ele.text
            text_list.append(text)
        return text_list

    # 获取元素属性
    def base_get_ele_attribute(self, loc, attribute, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param attribute: 元素属性
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素属性信息
        """
        attribute_value = self.base_find_element(loc, timeout, poll).get_attribute(attribute)
        log.info("正在对：{} 元素获取属性操作！，获取的属性：[{}]，属性值：{}".format(loc, attribute, attribute_value))
        return attribute_value

    # 判断元素是否存在
    def base_ele_is_exist(self, loc, timeout=5, poll=0.2):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素是否存在
        """
        log.info("正在调用查找页面是否存在指定元素：{} 方法".format(loc))
        try:
            self.base_find_element(loc, timeout, poll)
            log.info("找到：{} 元素啦！".format(loc))
            return True
        except:
            log.info("没有找到：{} 元素！".format(loc))
            return False

    # 判断按钮元素是否可用
    def base_ele_is_enable(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        :return: 元素是否可用
        """
        log.info("正在调用查找页面指定元素：{} 是否可用方法".format(loc))
        return self.base_find_element(loc, timeout, poll).is_enabled()

    # 指针移动
    def base_mouse_move_to(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        log.info("正在调用指针移动方法，移动位置：{}".format(loc))
        el = self.base_find_element(loc, timeout, poll)
        self.action.move_to_element(el).perform()

    # 双击
    def base_mouse_double_click(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        log.info("正在对：{} 元素执行双击操作！".format(loc))
        el = self.base_find_element(loc, timeout, poll)
        self.action.double_click(el).perform()

    # 剪贴板操作
    def base_clipboard(self, loc, value, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param value: 输入的值
        :param timeout: 超时时间
        :param poll: 查找频率
        :return:
        """
        log.info("正在将：{} 文本传入到剪贴板！".format(value))
        pyperclip.copy(value)
        el = self.base_find_element(loc, timeout, poll)
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        log.info("正在对：{} 元素执行从剪贴板粘贴：{} 操作！".format(loc, value))
        el.send_keys(Keys.CONTROL, "v")

    # 截图
    def base_screenshot(self):
        # 1. 调用截图方法
        log.error("断言出错，正在执行截图操作！")
        self.driver.get_screenshot_as_file("./image/err.png")
        # 2. 调用图片写入报告方法
        log.error("断言出错，正在将错误截图写入allure报告！")
        self.__base_write_img()

    # 刷新
    def base_refresh(self):
        self.driver.refresh()

    # 将截图写入报告（私有）
    def __base_write_img(self):
        # 1. 获取图片文件流
        with open("./image/err.png", "rb") as f:
            # 2. 调用allure.attach附加方法
            allure.attach(f.read(), "错误原因: ", allure.attachment_type.PNG)
