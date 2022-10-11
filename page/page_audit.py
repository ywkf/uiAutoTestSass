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
        self.base_web_select_ele(placeholder_text="所属频道", click_text=channel)

    # 周播单审核搜索框输入节目单名称
    def page_input_search_name(self, program_name):
        self.base_web_input_element(placeholder_text="节目单名称", input_text=program_name)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.audit_search_btn)

    # 获取首条节目单名称
    def page_get_first_program_name(self):
        return self.base_get_text(page.audit_first_program_name)

    # 点击详情进行审核按钮
    def page_click_info_btn(self):
        self.base_click(page.audit_first_info_btn, timeout=5)

    # 点击审核通过按钮
    def page_click_pass_btn(self):
        self.base_click(page.audit_info_pass_btn, timeout=5)

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
    def page_week_manage_search(self, state, week_name):
        channel = self.base_web_get_channel_by_program(week_name)
        self.page_click_week_manage()
        sleep(2)
        return self.base_web_program_search(channel=channel, state=state, placeholder_text="周播单名称", program_name=week_name)

    # 点击日播单管理
    def page_click_day_manage(self, click_text="日播单管理"):
        self.base_web_click_mute(click_text)

    # 点击新增节目审核
    def page_click_new_program_audit(self, click_text="新增节目审核"):
        self.base_web_click_mute(click_text)

    # 选择栏目
    def page_select_column(self, column):
        self.base_web_select_ele(placeholder_text="所属栏目", click_text=column)

    # 选择审核状态
    def page_select_audit_state(self, audit_state):
        self.base_web_click_element(placeholder_text="审核", click_text=audit_state)

    # 新增节目审核输入节目名称
    def page_input_program_name(self, program_name):
        self.base_web_input_text(placeholder_text="请输入节目名称查询", input_text=program_name)

    # 获取新增节目审核首条节目名称
    def page_get_new_audit_first_name(self):
        return self.base_get_text(page.audit_new_program_first_name)

    # 点击新增节目审核同意按钮
    def page_click_new_audit_accept_btn(self):
        self.base_click(page.audit_new_program_accept)

    # 获取提示信息
    def page_get_msg(self):
        return self.base_get_text(page.director_new_program_msg)

    # 日播单管理查询
    def page_day_manage_search(self, state, day_name):
        channel = self.base_web_get_channel_by_program(day_name)
        self.page_click_day_manage()
        sleep(2)
        print("audit day_name: ", day_name, type(day_name))
        return self.base_web_program_search(channel=channel, state=state, placeholder_text="节目单名称", program_name=day_name)

    # 节目单审核查找方法
    def page_audit_search(self, channel, name):
        self.page_select_channel(channel)
        self.page_input_search_name(name)
        sleep(0.5)
        self.page_click_search_btn()
        sleep(2)
        program_name = self.page_get_first_program_name()
        return program_name

    # 新增节目审核查询方法
    def page_new_audit_search(self, column, name):
        self.page_select_column(column)
        self.page_input_program_name(name)
        sleep(0.5)
        self.page_click_search_btn()
        sleep(2)
        program_name = self.page_get_new_audit_first_name()
        return program_name

    # 周播单审核组合业务方法
    def page_week_audit(self, week_name):
        channel = self.base_web_get_channel_by_program(week_name)
        self.page_click_week_audit()
        sleep(2)
        self.page_audit_search(channel, week_name)
        self.page_click_info_btn()
        sleep(0.5)
        self.page_click_pass_btn()
        sleep(1)

    # 日播单审核组合业务方法
    def page_day_audit(self, day_name):
        channel = self.base_web_get_channel_by_program(day_name)
        self.page_click_day_audit()
        sleep(2)
        self.page_audit_search(channel, day_name)
        self.page_click_info_btn()
        sleep(0.5)
        self.page_click_pass_btn()
        sleep(1)

    # 新增节目审核组合业务方法
    def page_new_audit(self, column, program_name):
        self.page_click_new_program_audit()
        sleep(2)
        self.page_new_audit_search(column, program_name)
        self.page_click_info_btn()
        sleep(0.5)
        self.page_click_new_audit_accept_btn()
        sleep(1)

    # 断言业务方法（周播单）
    def page_assert_week_audit(self, state, week_name):
        # self.page_click_arrange_menu()
        sleep(0.5)
        program_dict = self.page_week_manage_search(state=state, week_name=week_name)
        sleep(2)
        return program_dict.get("exist")

    # 断言业务方法（日播单）
    def page_assert_day_audit(self, state, day_name):
        # self.page_click_arrange_menu()
        sleep(0.5)
        program_dict = self.page_day_manage_search(state=state, day_name=day_name)
        sleep(2)
        return program_dict.get("exist")

    # 断言业务方法（周播单审核）
    def page_assert_week_audit2(self, state, week_program):
        sleep(0.5)
        program_dict = self.page_week_manage_search(state=state, week_name=week_program)
        sleep(2)
        self.base_click(page.director_manage_view_first_btn)
        sleep(0.5)
        class1 = self.base_get_ele_attribute(page.director_route_department, "class")
        return program_dict.get("exist") and (class1 == page.director_route_finish)

    # 断言业务方法（日播单审核）
    def page_assert_day_audit2(self, state, day_name):
        sleep(0.5)
        program_dict = self.page_day_manage_search(state=state, day_name=day_name)
        sleep(2)
        self.base_click(page.director_manage_view_first_btn)
        sleep(0.5)
        class1 = self.base_get_ele_attribute(page.director_route_department, "class")
        return program_dict.get("exist") and (class1 == page.director_route_finish)



