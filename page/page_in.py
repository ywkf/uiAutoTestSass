from page.page_channel_check import PageChannelCheck
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

    # 频道审核
    def get_page_channel_check(self):
        return PageChannelCheck(self.driver)