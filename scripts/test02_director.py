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

    # 测试业务方法
    @pytest.mark.parametrize("channel,date,playtime,expect", [("法治频道", {"year": "2020", "month": "八月", "day": "6"}, "12:11:10:09", "法治频道2020-08-03 - 2020-08-09周播单")])
    def test01_director(self, channel, date, playtime, expect):
        self.director.page_program_week_info(channel, date, playtime)
        print(self.director.page_get_week_name())
        print(self.director.base_get_text(page.date_program))
        assert expect == self.director.page_get_week_name()

    # 测试业务方法
    @pytest.mark.parametrize("row,duration,program_name,program_type,column,prebroadcast_type,self_type", read_yaml("director.yaml"))
    def test02_director(self, row, duration, program_name, program_type, column, prebroadcast_type, self_type):
        self.director.page_program_week_insert(row, duration, program_name, program_type, column, prebroadcast_type, self_type)
        print()
        self.director.page_insert_program(row)

