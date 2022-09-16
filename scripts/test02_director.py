import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestDirector:

    # 初始化
    def setup_class(self):

        # 获取 driver
        driver = GetDriver.get_web_driver(page.url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageLogin对象并调用成功登录依赖方法
        self.page_in.get_page_login().page_login_role(page.director_phone, page.director_pwd, page.director_secret)
        # 获取PageDirector页面对象
        self.director = PageIn(driver).get_page_director()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test_director(self):
        date = {"year": "2022", "month": "八月", "day": "6"}
        self.director.page_program_arrange(date)
        print(self.director.base_get_text(page.date_program))
