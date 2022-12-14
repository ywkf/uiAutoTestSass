import subprocess

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.get_program import director_test_init
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


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
        self.director = self.page_in.get_page_director()
        # 进入节目编单页面
        self.director.page_click_arrange()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("filename,week_name", read_yaml("director.yaml"))
    def test01_director(self, filename, week_name):
        # 输入节目单基本信息
        self.director.page_program_week_info(filename)
        # 判断周播单是否存在
        # if self.director.page_week_program_is_exist():
        #     pytest.exit("周播单已存在")
        self.director.page_week_exist_exit()
        # 获取周播单名称
        page.director_week_program = self.director.page_get_week_name()
        print(page.director_week_program)
        date_s = self.director.base_get_text(page.date_program)
        print(date_s)
        # 创建节目单并提交
        self.director.page_program_week_create_form(filename)
        try:
            assert self.director.page_assert_week_program("审核中", week_name)
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # 截图
            self.director.base_screenshot()
            # 抛出异常
            raise








