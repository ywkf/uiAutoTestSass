from time import sleep

import page
from base.base_web import BaseWeb


class PageChannelCheck(BaseWeb):

    # 点击节目编单
    def page_click_arrange(self):
        self.base_click(page.director_arrange)
        sleep(1)
        # 获取窗口句柄列表
        handles = self.driver.window_handles
        # 切换窗口
        self.driver.switch_to.window(handles[1])
        sleep(1)

    # 点击审核菜单
    def page_click_check(self):
        self.base_web_click_mute("审核")

    # 点击周播单审核
    def page_click_week_check(self):
        self.base_web_click_mute("周播单审核")

    # 选择频道
    def page_select_channel_check(self, channel):
        self.base_web_click_element("所属频道", channel)

    # 搜索框输入节目单名称
    def page_input_search_name(self, value):
        self.base_input(page.check_search_name, value)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.check_search_btn)

    # 获取首条周播单名称
    def page_get_first_week_name(self):
        return self.base_get_text(page.check_first_program_name)

    # 点击详情进行审核按钮
    def page_click_info_btn(self):
        self.base_click(page.check_first_info_btn)

    # 点击审核通过按钮
    def page_click_pass_btn(self):
        self.base_click(page.check_info_pass_btn)

    # 点击节目编排菜单
    def page_click_arrange_menu(self):
        self.base_web_click_mute("节目编排")

    # 点击周播单管理
    def page_click_week_manage(self):
        self.base_web_click_mute("周播单管理")

    # 周播单管理查询
    def page_week_manage_search(self, week_name):
        return self.base_web_program_search("周播单管理", "法治频道", "周播单名称", week_name)

    # 点击日播单管理
    def page_click_day_manage(self):
        self.base_web_click_mute("日播单管理")

    # 日播单管理查询
    def page_day_manage_search(self, day_name):
        return self.base_web_program_search("日播单管理", "法治频道", "节目单名称", day_name)

    # 组合业务方法
    def page_week_check(self):
        pass