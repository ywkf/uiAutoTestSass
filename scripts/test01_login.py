import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestLogin:

    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url)
        # 2. 通过统一入口类获取PageMpLogin对象
        self.login = PageIn(driver).get_page_login()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test_login(self, phone="19977777777", pwd="123456", secret="NE4WEQJZ7UTZGKRYUR5PTGOGU5OJ2ZIG"):
        # 调用登录业务方法
        self.login.page_login_make(phone, pwd, secret)
        # 断言
        print("\n 获取的租户名称为", self.login.page_get_tenant_name())