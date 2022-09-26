import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestDirectorDay:

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
    def test01_director_day(self, channel='法治频道', week_program='法治频道2028-05-22 - 2028-05-28周播单', playdate='2028-05-22'):
        self.director.page_program_day_info(channel, week_program, playdate)

    # 测试业务方法
    def test02_director_day(self):
        data = {
            "row": 2,
            "play_mode": "定时",
            "signal": "140ST#1"
        }
        self.director.page_program_day_create_form2("2028.5.22--2028.5.28.xlsx")







