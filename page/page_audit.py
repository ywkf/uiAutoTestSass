from time import sleep

import page
from base.base_web import BaseWeb
from tools.get_program import GetProgram


class PageAudit(BaseWeb):

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
    def page_click_audit(self):
        self.base_web_click_mute("审核")

    # 点击周播单审核
    def page_click_week_audit(self, click_text="周播单审核"):
        self.base_web_click_mute(click_text)

    # 选择频道
    def page_select_channel(self, channel):
        self.base_web_click_element(placeholder_text="所属频道", click_text=channel)

    # 搜索框输入节目单名称
    def page_input_search_name(self, value):
        self.base_input(page.audit_search_name, value)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.audit_search_btn)

    # 获取首条节目单名称
    def page_get_first_program_name(self):
        return self.base_get_text(page.audit_first_program_name)

    # 点击详情进行审核按钮
    def page_click_info_btn(self):
        self.base_click(page.audit_first_info_btn)

    # 点击审核通过按钮
    def page_click_pass_btn(self):
        self.base_click(page.audit_info_pass_btn)

    # 点击日播单审核
    def page_click_day_audit(self, click_text="日播单审核"):
        self.base_web_click_mute(click_text)

    # 点击节目编排菜单
    def page_click_arrange_menu(self, click_text="节目编排"):
        self.base_web_click_mute(click_text)

    # 点击周播单管理
    def page_click_week_manage(self, click_text="周播单管理"):
        self.base_web_click_mute(click_text)

    # 周播单管理查询
    def page_week_manage_search(self, filename, week_name):
        channel = GetProgram(filename).get_info(0).get("channel")
        return self.base_web_program_search(mute_text="周播单管理", channel=channel, placeholder_text="周播单名称",
                                            program_name=week_name)

    # 点击日播单管理
    def page_click_day_manage(self):
        self.base_web_click_mute("日播单管理")

    # 日播单管理查询
    def page_day_manage_search(self, filename, day_name):
        channel = GetProgram(filename).get_info(0).get("channel")
        return self.base_web_program_search(mute_text="日播单管理", channel=channel, placeholder_text="节目单名称",
                                            program_name=day_name)

    # 节目单审核查找方法
    def page_audit_search(self, channel, name):
        self.page_select_channel(channel)
        self.page_input_search_name(name)
        sleep(0.5)
        self.page_click_search_btn()
        sleep(2)
        program_name = self.page_get_first_program_name()
        self.page_click_info_btn()
        sleep(0.5)
        self.page_click_pass_btn()
        sleep(1)
        return program_name

    # 周播单审核组合业务方法
    def page_week_audit(self, channel, name):
        self.page_click_week_audit()
        self.page_audit_search(channel, name)

        self.page_click_arrange_menu()
        sleep(0.5)
        self.page_week_manage_search()
        sleep(2)

    # 日播单审核组合业务方法
    def page_day_audit(self, channel, name):
        self.page_click_day_audit()
        self.page_audit_search(channel, name)

        self.page_click_arrange_menu()
        sleep(0.5)
        self.page_day_manage_search()
        sleep(2)

    # 断言业务方法
    def page_assert_audit(self):
        self.page_click_arrange_menu()
        sleep(0.5)
        self.page_day_manage_search()
        sleep(2)




