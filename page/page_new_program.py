from time import sleep

import page
from base.base_web import BaseWeb


class PageNewProgram(BaseWeb):

    # 点击节目编单
    def page_click_arrange(self):
        self.base_click(page.director_arrange)
        sleep(1)
        # 获取窗口句柄列表
        handles = self.driver.window_handles
        # 切换窗口
        self.driver.switch_to.window(handles[1])
        sleep(1)

    # 点击节目管理
    def page_click_program_manage(self):
        self.base_web_click_mute("节目管理")

    # 点击新增节目按钮
    def page_click_new(self):
        self.base_click(page.director_new_program_btn)

    # 选择播出日期
    def page_select_playdate(self, playdate):
        self.base_web_select_date(playdate)

    # 选择节目类型
    def page_select_program_type(self, program_type):
        self.base_web_click_element(placeholder_text="请选择节目类型", click_text=program_type)

    # 选择所属栏目
    def page_select_column(self, column):
        self.base_web_click_element(placeholder_text="请选择栏目", click_text=column)

    # 输入节目名称
    def page_input_program_name(self, program_name):
        self.base_web_input_text(placeholder_text="请输入节目名称", input_text=program_name)

    # 输入预计时长
    def page_input_duration(self, duration):
        self.base_web_input_time(page.director_new_program_duration, duration)

    # 选择节目自办类型
    def page_select_self_type(self, self_type):
        self.base_web_click_element(placeholder_text="自办/非自办，默认值设自办", click_text=self_type)

    # 选择备播类型
    def page_select_pre_type(self, pre_type):
        self.base_web_click_element(placeholder_text="普通/当日（涉及到节目提交的关门时间）", click_text=pre_type)

    # 输入申请原因
    def page_input_reason(self, reason):
        self.base_web_input_text(placeholder_text="请输入申请原因", input_text=reason)

    # 点击提交审核按钮
    def page_click_submit(self):
        self.base_click(page.director_new_program_submit_btn)

    # 获取提示信息
    def page_get_msg(self):
        return self.base_get_text(page.director_new_program_msg)

    # 选择所属栏目查询
    def page_select_column_search(self, column):
        self.base_web_click_element(placeholder_text="所属栏目", click_text=column)

    # 输入节目ID查询
    def page_input_id_search(self, program_id):
        self.base_web_input_text(placeholder_text="请输入节目ID查询", input_text=program_id)

    # 选择预播日期查询
    def page_select_date_search(self, playdate):
        self.base_web_select_date(playdate)

    # 输入节目名称查询
    def page_input_program_name_search(self, program_name):
        self.base_web_input_text(placeholder_text="请输入节目名称查询", input_text=program_name)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.director_search_btn)

    # 频道首条节目是否存在
    def page_first_is_exist(self):
        return self.base_ele_is_exist(page.director_new_program_first_id)

    # 获取首条节目名称
    def page_get_first_name(self):
        return self.base_get_text(page.director_new_program_first_name)

    # 获取首条节目状态
    def page_get_first_program_state(self):
        return self.base_get_text(page.director_new_program_first_state)

    # 整合查询方法
    def page_search(self, program_id):
        self.page_input_id_search(program_id)
        sleep(0.5)
        self.page_click_search_btn()

    # 整合输入节目信息方法
    def page_new_program_info(self, info):
        self.page_click_new()
        sleep(1)
        self.page_select_playdate(info.get("playdate"))
        # self.page_select_program_type(info.get("program_type"))
        # self.page_select_column(info.get("column"))
        self.page_input_program_name(info.get("program_name"))
        self.page_input_duration(info.get("duration"))
        # self.page_select_self_type(info.get("self_type"))
        self.page_select_pre_type(info.get("pre_type"))
        self.page_input_reason(info.get("reason"))
        self.page_click_submit()

    # 整合业务方法
    def page_new_program(self, info):
        self.page_click_program_manage()
        sleep(1)
        self.page_new_program_info(info)

