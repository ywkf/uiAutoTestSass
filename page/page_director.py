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

    # 搜索框输入周播单名称
    def page_search_input_week_name(self, week_name):
        self.base_input(page.director_week_search_name, week_name)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.director_week_search_btn)

    # 查看查询结果是否存在
    def page_search_result_is_exist(self):
        return self.base_ele_is_exist(page.director_week_name_first)

    # 获取首条节目单名称
    def page_get_first_week_name(self):
        return self.base_get_text(page.director_week_name_first)

    # 获取首条节目单审核状态
    def page_get_first_week_state(self):
        return self.base_get_text(page.director_week_state_first)

    # 组合创建周播单方法
    def page_create_week_list(self):
        pass

    # 组合创建日播单方法
    def page_create_day_list(self):
        pass

    # 周播单基本信息
    def page_program_week_info(self, channel, date):
        # date = {"year": "2020", "month": "八月", "day": "6"}
        self.page_click_arrange()
        self.page_click_create_week()
        self.page_select_channel(channel)
        self.page_select_date(date)
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



    # 创建周播单
    def page_program_week_insert(self, row, duration, program_name, program_type, column, prebroadcast_type, self_type):
        # self.page_input_playtime(1, data.get("playtime"))
        self.page_input_duration(row, duration)
        self.page_input_name(row, program_name)
        self.page_select_type(row, program_type)
        self.page_select_column(row, column)
        self.page_select_prebroadcast_type(row, prebroadcast_type)
        self.page_select_self_type(row, self_type)
        # self.page_insert_program(row)
        sleep(0.5)

    # 组合业务方法
    def page_program_arrange(self, data):
        self.page_program_week_info(data)
        self.page_program_week_info(data)

    # 周播单管理
    def page_week_manage(self, week_name):
        self.page_click_arrange()
        self.page_click_week_manage()
        self.page_search_input_week_name(week_name)
        self.page_click_search_btn()

    # 日播单基本信息
    def page_program_day_info(self, channel, week_program, playdate):
        self.page_click_arrange()
        self.page_create_day()
        sleep(5)
        self.page_select_channel(channel)
        self.page_select_week(week_program)
        self.page_select_playdate(playdate)
        self.base_web_get_table_attr_loc("序号")

    # 日播单编辑节目
    def page_program_day_create_form(self, data):
        row = data.get("row")
        self.page_select_play_mode(row, data.get("play_mode"))
        self.page_select_signal(row, data.get("signal"))
        sleep(1)

    # 创建日播单
    def page_program_day_create_form1(self, data):
        days = page.director_playdate_list
        days = ['2028-05-22', '2028-05-24', '2028-05-25', '2028-05-26', '2028-05-28']
        for day in days:
            # d = self.base_web_find_ele(page.director_playdate, day)
            # if not d:
            #     continue
            self.page_select_playdate(day)
            sleep(1)
            self.page_program_day_create_form(data)
            # self.page_click_submit()



