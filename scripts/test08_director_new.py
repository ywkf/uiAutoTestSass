import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

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
    @pytest.mark.parametrize("playdate,program_type,column,program_name,duration,self_type,pre_type,reason", read_yaml("director_program.yaml"))
    def test01_new_program(self, playdate, program_type, column, program_name, duration, self_type, pre_type, reason):
        self.program.page_click_program_manage()
        self.program.page_new_program_info(playdate, program_type, column, program_name, duration, self_type, pre_type, reason)
        # page.new_program_list.append((column, program_name))
        try:
            assert "提交审核成功!" == self.program.page_get_msg()
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # 截图
            self.program.base_screenshot()
            # 抛出异常
            raise