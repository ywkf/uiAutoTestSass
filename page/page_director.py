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
    def page_select_channel(self):
        pass

    # 选择周播单时间
    def page_select_date(self, date):
        self.base_web_select_date(date)

    # 输入时长
    def page_input_time(self):
        pass

    # 输入节目名称
    def page_input_name(self):
        pass

    # 选择节目类型
    def page_select_type(self):
        pass

    # 选择所属栏目
    def page_select_column(self):
        pass

    # 选择备播类型
    def page_select_prebroadcast_type(self):
        pass

    # 选择自办类型
    def page_select_self_type(self):
        pass

    # 在此节目下插入一条节目
    def page_insert_program(self):
        pass

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

    # 组合业务方法
    def page_program_arrange(self, date):
        self.page_click_arrange()
        self.page_click_create_week()
        self.page_select_date(date)


