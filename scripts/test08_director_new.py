import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestDirectorNew:

    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageLogin对象并调用成功登录依赖方法
        self.page_in.get_page_login().page_login_role(page.director_phone, page.director_pwd, page.director_secret)
        # 获取PageNewProgram对象
        self.program = self.page_in.get_page_new_program()
        # 进入节目编单页面
        self.program.page_click_arrange()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试业务方法
    def test01_new_program(self):
        info = {
            "playdate":{
                "year": "2027",
                "month": "八月",
                "day": "2"},
            "program_type": "测试",
            "column": "河南法治报道",
            "program_name": "法制剧场1",
            "duration": "00:15:00:00",
            "self_type": "自办",
            "pre_type": "普通",
            "reason": "test1"
        }
        self.program.page_click_program_manage()
        self.program.page_new_program_info(info)