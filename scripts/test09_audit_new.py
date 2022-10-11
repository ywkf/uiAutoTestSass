import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestAuditNew:

    # 初始化
    def setup_class(self):
        # 获取 driver
        driver = GetDriver.get_web_driver(page.url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageLogin对象并调用成功登录依赖方法
        self.page_in.get_page_login().page_login_role(page.channel_audit_phone, page.channel_audit_pwd, page.channel_audit_secret)
        # 获取PageDirector页面对象
        self.audit = self.page_in.get_page_audit()
        # 进入节目编单页面
        self.audit.page_click_arrange()
        # 点击展开节目排单菜单
        self.audit.page_click_arrange_menu()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("column,program_name", page.new_program_list)
    def test01_audit_program(self, column, program_name):
        self.audit.page_new_audit(column, program_name)
        try:
            assert "处理成功" == self.audit.page_get_msg()
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # 截图
            self.audit.base_screenshot()
            # 抛出异常
            raise
