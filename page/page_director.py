from selenium.webdriver.common.by import By

import page
from base.base_web import BaseWeb
from time import sleep

from tools.get_program import GetProgram


class PageDirector(BaseWeb):

    # 点击节目编单
    def page_click_arrange(self):
        self.base_click(page.director_arrange)
        sleep(1)
        # 获取窗口句柄列表
        handles = self.driver.window_handles
        # 切换窗口
        self.driver.switch_to.window(handles[1])
        sleep(1)

    # 点击创建周播单
    def page_click_create_week(self):
        self.base_click(page.director_create_week)

    # 选择所属频道
    def page_select_channel(self, channel):
        # self.base_web_click_element("请选择频道", channel)
        self.base_web_click_ele(page.director_belong_channel, channel)

    # 选择周播单时间
    def page_select_date(self, date):
        self.base_web_select_date(date)

    # 获取周播单名称
    def page_get_week_name(self):
        return self.base_get_input_value(page.director_week_name)

    # 选择播放方式
    def page_select_play_type(self, row, play_type):
        self.base_web_select_attr(row, "play_type", play_type)

    # 输入开播时间
    def page_input_playtime(self, row, time):
        loc = page.find_attr_by_num(row, page.attr_num.get("playtime"))
        self.base_web_input_time(loc, time)

    # 输入时长
    def page_input_duration(self, row, time):
        loc = page.find_attr_by_num(row, page.attr_num.get("duration"))
        self.base_web_input_time(loc, time)

    # 输入节目名称
    def page_input_name(self, row, program_name):
        loc = page.find_attr_by_num(row, page.attr_num.get("program_name"))
        self.base_input(loc, program_name)

    # 选择节目类型
    def page_select_type(self, row, program_type):
        self.base_web_select_attr(row, "program_type", program_type)

    # 选择所属栏目
    def page_select_column(self, row, column):
        self.base_web_select_attr(row, "column", column)

    # 选择备播类型
    def page_select_prebroadcast_type(self, row, prebroadcast_type):
        self.base_web_select_attr(row, "prebroadcast_type", prebroadcast_type)

    # 选择自办类型
    def page_select_self_type(self, row, self_type):
        self.base_web_select_attr(row, "self_type", self_type)

    # 在此节目下插入一条节目
    def page_insert_program(self, row):
        loc = page.find_btn_by_num(row, page.button_num.get("plus"))
        self.base_click(loc)
        sleep(0.5)

    # 删除此条节目
    def page_delete_program(self, row):
        loc = page.find_btn_by_num(row, page.button_num.get("delete"))
        self.base_click(loc)
        sleep(0.5)
        self.base_click(page.director_program_delete_confirm_btn)

    # 获取错误信息数量
    def page_get_error_num(self):
        return self.base_get_text(page.director_error_num)

    # 点击周
    def page_click_next_day(self, week_num):
        self.base_web_select_week_num(week_num)

    # 点击新建
    def page_click_new(self):
        self.base_click(page.director_new_btn)

    # 点击提交
    def page_click_submit(self):
        self.base_click(page.director_submit_btn)

    # 点击创建日播单
    def page_create_day(self):
        self.base_click(page.director_create_day)

    # 选择所属周播单
    def page_select_week(self, week_program):
        self.base_web_click_ele(page.director_belong_week, week_program)

    # 选择播出日期
    def page_select_playdate(self, playdate):
        self.base_web_click_ele(page.director_playdate, playdate)

    # 获取日播单名称
    def page_get_day_name(self):
        return self.base_get_input_value(page.director_day_name)

    # 选择播放方式
    def page_select_play_mode(self, row, play_mode):
        if row != 1:
            self.base_web_select_attr(row, "play_mode", play_mode)

    # 选择信号源
    def page_select_signal(self, row, signal):
        self.base_web_select_attr(row, "signal", signal)

    # 点击周播单管理
    def page_click_week_manage(self):
        self.base_click(page.director_week_manage)

    # 选择频道
    def page_select_channel_manage(self, channel):
        self.base_web_click_element("所属频道", channel)

    # 搜索框输入周播单名称
    def page_search_input_week_name(self, week_name):
        self.base_clipboard(page.director_week_search_name, week_name)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.director_manage_search_btn)

    # 查看查询结果是否存在
    def page_search_result_is_exist(self):
        return self.base_ele_is_exist(page.director_manage_name_first)

    # 获取首条节目单名称
    def page_get_first_week_name(self):
        return self.base_get_text(page.director_manage_name_first)

    # 获取首条节目单审核状态
    def page_get_first_week_state(self):
        return self.base_get_text(page.director_manage_state_first)

    # 点击日播单管理
    def page_click_day_manage(self):
        self.base_click(page.director_day_manage)

    # 搜索框输入日播单名称
    def page_search_input_day_name(self, day_name):
        self.base_clipboard(page.director_day_search_name, day_name)

    # 组合创建周播单方法
    def page_create_week_list(self):
        pass

    # 组合创建日播单方法
    def page_create_day_list(self):
        pass

    # 周播单基本信息
    def page_program_week_info(self, filename):
        # date = {"year": "2020", "month": "八月", "day": "6"}
        info_dict = GetProgram(filename).get_info(0)
        # self.page_click_arrange()
        self.page_click_create_week()
        self.page_select_channel(info_dict.get("channel"))
        self.page_select_date(info_dict.get("date"))
        sleep(1)

    # 周播单添加节目(频道导播)
    def page_program_week_program_insert(self, data):
        row = data.get("row")
        self.page_input_duration(row, data.get("duration"))
        self.page_input_name(row, data.get("program_name"))
        self.page_select_column(row, data.get("column"))
        sleep(1)

    # 创建周播单(频道导播)
    def page_program_week_create_form(self, filename):
        for table in range(7):
            # prog_list = GetProgram(filename).get_program(table)
            prog_list = [{'row': '1', 'duration': '12:00:00', 'program_name': '好剧连连看-1', 'column': '河南法治报道'},
                         {'row': '2', 'duration': '12:00:00', 'program_name': '好剧连连看-2', 'column': '河南法治报道'}]
            last = prog_list[-1].get("row")
            for prog in prog_list:
                row = prog.get("row")
                self.page_program_week_program_insert(prog)
                if row != last:
                    self.page_insert_program(row)
            if table < 5:
                self.page_click_next_day(table + 2)
            if table == 5:
                self.page_click_next_day(0)
        sleep(1)
        # self.page_click_submit()

    # 周播单管理查找方法
    def page_week_program_manage_search(self, week_name):
        # self.page_click_arrange()
        self.page_click_week_manage()
        sleep(1)
        self.page_search_input_week_name(week_name)
        sleep(0.5)
        self.page_click_search_btn()
        sleep(2)
        exist = self.page_search_result_is_exist()
        name = self.page_get_first_week_name()
        state = self.page_get_first_week_state()
        print("exist: ", exist, "name: ", name, "state: ", state)

    # 日播单基本信息
    def page_program_day_info(self, filename):
        info = GetProgram(filename).get_info(0)
        # self.page_click_arrange()
        self.page_create_day()
        sleep(5)
        self.page_select_channel(info.get("channel"))
        self.page_select_week(info.get("week_program"))
        # self.page_select_playdate(playdate)
        # self.base_web_get_table_attr_loc("序号")

    # 日播单编辑节目
    def page_program_day_create_form(self, data):
        row = data.get("row")
        self.page_select_play_mode(row, data.get("play_mode"))
        self.page_select_signal(row, data.get("signal"))
        sleep(1)

    # 创建日播单
    def page_program_day_create_form1(self, filename, date):
        signal_list = GetProgram(filename).get_signal_by_date(date)
        signal_list = [{'row': '1', 'play_mode': '顺序', 'signal': '140ST#1', 'date': '2028-05-28'},
                       {'row': '2', 'play_mode': '定时', 'signal': '中1光纤', 'date': '2028-05-28'},
                       {'row': '3', 'play_mode': '顺时', 'signal': '', 'date': '2028-05-28'}]
        self.base_click(page.director_playdate)
        sleep(0.5)
        loc = By.XPATH, "//*[text()='{}']".format(date)
        if self.base_ele_is_exist(loc, timeout=1, poll=0.1):
            self.base_click(loc)
            sleep(1)
            for signal in signal_list:
                self.page_program_day_create_form(signal)
            # self.page_click_submit()

    # 日播单管理查找方法
    def page_day_program_manage_search(self, day_name):
        return self.base_web_program_search("日播单管理", "法治频道", "节目单名称", day_name)
        # self.page_click_arrange()
        # self.page_click_day_manage()
        # sleep(2)
        # self.page_search_input_day_name(day_name)
        # sleep(0.5)
        # self.page_click_search_btn()
        # sleep(2)
        # exist = self.page_search_result_is_exist()
        # name = self.page_get_first_week_name()
        # state = self.page_get_first_week_state()
        # print("exist: ", exist, "name: ", name, "state: ", state)

    # 创建日播单
    def page_program_day_create_form2(self, filename):
        days = page.director_playdate_list
        days = ['2028-05-22', '2028-05-23', '2028-05-24', '2028-05-25', '2028-05-26', '2028-05-27', '2028-05-28']
        for table in range(7):
            # signal_list = GetProgram(filename).get_signal(table)
            signal_list = [{'row': '1', 'play_mode': '顺序', 'signal': '140ST#1', 'date': '2028-05-28'},
                           {'row': '2', 'play_mode': '定时', 'signal': '中1光纤', 'date': '2028-05-28'},
                           {'row': '3', 'play_mode': '顺时', 'signal': '', 'date': '2028-05-28'}]
            self.base_click(page.director_playdate)
            sleep(0.5)
            loc = By.XPATH, "//*[text()='{}']".format(signal_list[0].get("date"))
            if not self.base_ele_is_exist(loc, timeout=1, poll=0.1):
                self.base_click(page.director_playdate)
                continue
            self.base_click(loc)
            for data in signal_list:
                # self.page_select_playdate(day)
                sleep(1)
                self.page_program_day_create_form(data)
                # self.page_click_submit()



