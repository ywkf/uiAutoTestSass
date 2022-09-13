from base.base_web import BaseWeb
from page.page_login import PageLogin


class PageIn:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 登录
    def get_page_login(self):
        return PageLogin(self.driver)