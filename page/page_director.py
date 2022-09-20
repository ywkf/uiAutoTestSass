import page
from base.base_web import BaseWeb
from time import sleep


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
        self.base_web_click_element("请选择频道", channel)

    # 选择周播单时间
    def page_select_date(self, date):
        self.base_web_select_date(date)

    # 获取周播单名称
    def page_get_week_name(self):
        return self.base_get_input_value(page.director_week_name)

    # 输入开播时间
    def page_input_playtime(self, row, time):
        loc = page.find_attr_by_num(row, page.attr_num.get("playtime"))
        self.base_web_input_time(loc, time)
        print("playtime_new: ", self.base_get_input_value(page.director_playtime))

    # 输入时长
    def page_input_duration(self, row, time):
        loc = page.find_attr_by_num(row, page.attr_num.get("duration"))
        self.base_web_input_time(loc, time)
        print("duration_new: ", self.base_get_input_value(page.director_duration))

    # 输入节目名称
    def page_input_name(self, row, program_name):
        loc = page.find_attr_by_num(row, page.attr_num.get("program_name"))
        self.base_input(loc, program_name)

    # 选择节目类型
    def page_select_type(self, row, program_type):
        loc = page.find_attr_by_num(row, page.attr_num.get("program_type"))
        value = self.base_get_input_value(loc)
        if value != program_type:
            self.base_click(loc)
            self.base_web_selector(program_type)

    # 选择所属栏目
    def page_select_column(self, row, column):
        loc = page.find_attr_by_num(row, page.attr_num.get("column"))
        value = self.base_get_input_value(loc)
        if value != column:
            self.base_click(loc)
            self.base_web_selector(column)

    # 选择备播类型
    def page_select_prebroadcast_type(self, row, prebroadcast_type):
        loc = page.find_attr_by_num(row, page.attr_num.get("prebroadcast_type"))
        value = self.base_get_input_value(loc)
        if value != prebroadcast_type:
            self.base_click(loc)
            self.base_web_selector(prebroadcast_type)

    # 选择自办类型
    def page_select_self_type(self, row, self_type):
        loc = page.find_attr_by_num(row, page.attr_num.get("self_type"))
        value = self.base_get_input_value(loc)
        if value != self_type:
            self.base_click(loc)
            self.base_web_selector(self_type)

    # 在此节目下插入一条节目
    def page_insert_program(self, row):
        loc = page.find_btn_by_num(row, page.button_num.get("plus"))
        self.base_click(loc)
        sleep(0.5)

    # 获取错误信息数量
    def page_get_error_num(self):
        pass

    # 点击下一天
    def page_click_next_day(self):
        pass

    # 点击新建
    def page_click_new(self):
        pass

    # 点击提交
    def page_click_submit(self):
        pass

    # 点击创建日播单
    def page_create_day(self):
        pass

    # 选择所属周播单
    def page_select_week(self):
        pass

    # 选择播出日期
    def page_select_broadcast_date(self):
        pass

    # 选择播放方式
    def page_select_broadcast_mode(self):
        pass

    # 选择信号源
    def page_select_signal(self):
        pass

    # 组合创建周播单方法
    def page_create_week_list(self):
        pass

    # 组合创建日播单方法
    def page_create_day_list(self):
        pass

    # 输入基本信息
    def page_program_week_info(self, data):
        self.page_click_arrange()
        self.page_click_create_week()
        self.page_select_channel(data.get("channel"))
        self.page_select_date(data.get("date"))
        sleep(1)

    # 添加节目单
    def page_program_week_insert0(self, data):
        row = data.get("row")
        self.page_input_playtime(1, data.get("playtime"))
        self.page_input_duration(row, data.get("duration"))
        self.page_input_name(row, data.get("program_name"))
        self.page_select_type(row, data.get("program_type"))
        self.page_select_column(row, data.get("column"))
        self.page_select_prebroadcast_type(row, data.get("prebroadcast_type"))
        self.page_select_self_type(row, data.get("self_type"))
        # self.page_insert_program(row)
        sleep(1)

    # 添加节目单
    def page_program_week_insert(self, row, duration, program_name, program_type, column, prebroadcast_type, self_type):
        # self.page_input_playtime(1, data.get("playtime"))
        self.page_input_duration(row, duration)
        self.page_input_name(row, program_name)
        self.page_select_type(row, program_type)
        self.page_select_column(row, column)
        self.page_select_prebroadcast_type(row, prebroadcast_type)
        self.page_select_self_type(row, self_type)
        # self.page_insert_program(row)
        sleep(1)

    # 组合业务方法
    def page_program_arrange(self, data):
        self.page_program_week_info(data)
        self.page_program_week_info(data)


