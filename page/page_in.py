from page.page_director import PageDirector
from page.page_login import PageLogin


class PageIn:

    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 登录
    def get_page_login(self):
        return PageLogin(self.driver)

    # 频道导播
    def get_page_director(self):
        return PageDirector(self.driver)