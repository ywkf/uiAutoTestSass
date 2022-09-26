import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


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

    # # 测试业务方法
    # @pytest.mark.parametrize("channel,date,expect", read_yaml("director.yaml"))
    # def test01_director(self, channel, date, expect):
    #     self.director.page_program_week_info(channel, date)
    #     page.director_week_program = self.director.page_get_week_name()
    #     print(page.director_week_program)
    #     date_s = self.director.base_get_text(page.date_program)
    #     print(date_s)
    #     assert expect == self.director.page_get_week_name()
    #
    # # 测试业务方法
    # def test02_director(self, filename="2022.8.1--2022.8.7.xlsx"):
    #     self.director.page_program_week_create_form(filename)
    #
    # # 测试业务方法
    # def test03_director(self, week_name="法治频道2020-08-03 - 2020-08-09周播单", expect="法治频道2020-08-03 - 2020-08-09周播单"):
    #     self.director.page_week_program_manage_search(week_name)
    #     assert self.director.page_search_result_is_exist() is True
    #     assert self.director.page_get_first_week_name() == expect
    #     assert self.director.page_get_first_week_state() == "审核失败"

    # 测试业务方法
    @pytest.mark.parametrize("filename,expect", read_yaml("director.yaml"))
    def test01_director(self, filename, expect):
        # 输入节目单基本信息
        self.director.page_program_week_info(filename)
        page.director_week_program = self.director.page_get_week_name()
        print(page.director_week_program)
        date_s = self.director.base_get_text(page.date_program)
        print(date_s)
        # 验证节目单名称
        assert expect == self.director.page_get_week_name()
        # 创建节目单并提交
        self.director.page_program_week_create_form(filename)
        # 周播单管理查找验证
        self.director.page_week_program_manage_search(page.director_week_program)
        assert self.director.page_search_result_is_exist() is True
        assert self.director.page_get_first_week_name() == expect
        assert self.director.page_get_first_week_state() == "审核通过"






