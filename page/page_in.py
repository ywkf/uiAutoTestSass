from page.page_audit import PageAudit
from page.page_director import PageDirector
from page.page_login import PageLogin
from page.page_new_program import PageNewProgram


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

    # 频道导播（新增节目）
    def get_page_new_program(self):
        return PageNewProgram(self.driver)

    # 频道审核
    def get_page_audit(self):
        return PageAudit(self.driver)
