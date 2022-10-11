import operator
import re
import datetime

from selenium.webdriver.common.by import By

from time import sleep

import page
from base.base import Base
from tools.get_log import GetLog
log = GetLog.get_logger()


class BaseWeb(Base):

    # 选择租户
    def base_web_select_tenant(self, tenant):
        """
        :param tenant: 选择租户
        """
        log.info("正在调用web专属选择租户方法，所选租户：{}".format(tenant))
        login_tenant = By.XPATH, "//*[@class='name'][text()='{}']".format(tenant)
        self.base_click(login_tenant)

    # 根据显示文本点击指定元素
    def base_web_click_element(self, placeholder_text, click_text):
        log.info("正在调用web专属点击封装方法")
        # 1. 点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2. 暂停
        sleep(1)
        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 根据显示文本点击指定元素
    def base_web_click_ele(self, loc, click_text):
        log.info("正在调用web专属点击封装方法2")
        # 1. 点击复选框
        self.base_click(loc)
        # 2. 暂停
        sleep(0.5)
        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']/..".format(click_text)
        self.base_click(loc)

    # 根据显示文本点击指定元素
    def base_web_select_element(self, placeholder_text, click_text):
        log.info("正在调用web新增节目复选框选择封装方法")
        # 1. 点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2. 暂停
        sleep(0.5)
        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//div[@x-placement='bottom-start']//span[text()='{}']/..".format(click_text)
        self.base_click(loc)

    # 根据显示文本点击指定元素
    def base_web_select_ele(self, placeholder_text, click_text):
        log.info("正在调用web专属复选框选择封装方法")
        # 1. 点击复选框
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 2. 暂停
        sleep(0.5)
        # 3. 点击包含显示文本的元素
        loc1 = By.XPATH, "//li//*[text()='{}']".format(click_text)
        self.base_click(loc1)

    # 根据显示文本输入指定元素
    def base_web_input_text(self, placeholder_text, input_text):
        log.info("正在调用web专属输入封装方法")
        # if type(input_text) is tuple:
        #     input_text = input_text[0]
        #     print("web input_text", input_text)
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_input(loc, input_text)

    # 根据显示文本从剪贴板粘贴指定元素
    def base_web_input_element(self, placeholder_text, input_text):
        log.info("正在调用web专属剪贴板封装方法")
        if type(input_text) is tuple:
            input_text = input_text[0]
            print("web input_text", input_text)
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_clipboard(loc, input_text)

    # 根据文本点击导航菜单
    def base_web_click_mute(self, click_text):
        log.info("正在调用web点击导航菜单方法，选择菜单：{}".format(click_text))
        loc = By.XPATH, "//li//*[text()='{}']/..".format(click_text)
        self.base_click(loc)

    # 选择年份 >
    def __select_year(self, loc_Y, loc_m, loc_d):
        self.base_click(loc_Y)
        sleep(0.5)
        self.base_click(loc_m)
        sleep(0.5)
        self.base_click(loc_d)

    # 选择月份 >
    def __select_month(self, loc_m, loc_d):
        self.base_click(loc_m)
        sleep(0.5)
        self.base_click(loc_d)

    # 循环判断选择年份
    def __loop_select_year(self, year):
        year_list = self.base_get_text_list(page.date_year_list)
        print("year_list", year_list)
        try:
            # 年份列表包含数据年份
            if operator.contains(year_list, str(year)):
                return True
            # 年份列表不包含数据年份，且数据年份小于该页最小年份
            elif year < int(year_list[0]):
                # 点击前一年按钮
                self.base_click(page.date_last_year)
                sleep(0.5)
                self.__loop_select_year(year)
            # 年份列表不包含数据年份，且数据年份大于该页最大年份
            elif year > int(year_list[-1]):
                # 点击后一年按钮
                self.base_click(page.date_next_year)
                sleep(0.5)
                self.__loop_select_year(year)
            return True
        except Exception as e:
            log.error("错误信息：", e)
            print("错误信息： ", e)

    # 选择日期
    def base_web_select_date(self, date):
        log.info("正在调用web专属选择日期封装方法, 选择日期：{}".format(date))
        # date = {"year": "2022", "month": "八月", "day": "6"}
        loc_Y = By.XPATH, "//*[@class='cell'][text()='{}']".format(date.get("year"))
        loc_m = By.XPATH, "//*[@class='cell'][text()='{}']".format(date.get("month"))
        loc_d = By.XPATH, "//*[@class='available']//span[normalize-space(text())='{}']".format(date.get("day"))
        # 点击选择日期
        self.base_click(page.date_select)
        sleep(0.5)
        # 获取日期框当前年份
        year = self.base_get_text(page.date_year_select)
        # 日期框当前年份与date年份相同
        if operator.contains(year, date.get("year")):
            # 点击日期框当前月份
            self.base_click(page.date_month_select)
            sleep(0.5)
            # 调用方法选择月份 >
            self.__select_month(loc_m, loc_d)
        # 日期框当前年份与date年份不同
        else:
            # 点击日期框当前年份
            self.base_click(page.date_year_select)
            sleep(0.5)
            # 判断年份列表是否包含数据年份
            contains_year = self.__loop_select_year(int(date.get("year")))
            # 年份列表包含数据年份
            if contains_year:
                # 调用方法选择年份 >
                self.__select_year(loc_Y, loc_m, loc_d)

    # 输入时间
    def base_web_input_time(self, loc, time):
        log.info("正在调用web专属输入时间封装方法")
        # time = "11:12:12:12"
        time_list = time.split(":")
        self.base_find_element(loc, timeout=30, poll=0.5).send_keys(0)
        for time in time_list:
            # sleep(0.1)
            self.base_find_element(loc, timeout=30, poll=0.5).send_keys(time)

    # 定位属性
    def base_web_find_by_num(self, row, table, col):
        loc = "//tr[{}]//*[@class='el-table_{}_column_{}   el-table__cell']//input".format(row, table, col)
        return self.base_find_element(loc, timeout=30, poll=0.5)

    # 根据行和属性名称选择对应属性
    def base_web_select_attr(self, row, attr_name, attr):
        log.info("正在调用web专属选择属性封装方法，第 {} 行，{} 属性，值为：{}".format(row, attr_name, attr))
        loc = page.find_attr_by_num(row, page.attr_num.get(attr_name))
        if attr_name == "play_mode" or attr_name == "signal":
            loc = page.find_day_attr(row, attr_name)
        value = self.base_get_input_value(loc)
        if (attr is not None) and (value != attr) and (len(attr.strip()) != 0):
            self.base_click(loc)
            self.base_web_selector(attr)

    # 复选框选择
    def base_web_selector(self, text):
        log.info("正在调用web专属复选框选择封装方法")
        sleep(0.2)
        loc = (page.director_selector[0], page.director_selector[1].format(text))
        loc_or = (page.director_selector_or[0], page.director_selector_or[1].format(text))
        if self.base_ele_is_exist(loc, timeout=0.2, poll=0.05):
            self.base_click(loc)
        if self.base_ele_is_exist(loc_or, timeout=0.2, poll=0.05):
            self.base_click(loc_or)

    # 周选择
    def base_web_select_week_num(self, week_num):
        log.info("正在调用web专属周播单选择星期方法")
        loc = (page.director_week_num[0], page.director_week_num[1].format(week_num))
        self.base_click(loc)
        sleep(0.5)

    # 获取当周日期列表
    def base_web_week_date(self, date):
        date_s = re.search(r"(?<=（)(.+?)(?=）)", date).group()
        d1 = date_s.split('-')
        d2 = []
        date_list = []
        for i in d1:
            d2.append(int(i))
        d3 = datetime.date(*d2)
        for j in range(7):
            d4 = d3 + datetime.timedelta(j)
            date_list.append(str(d4))
        return date_list

    # 获取table属性
    def base_web_get_table_attr_loc(self, attr_text):
        loc = By.XPATH, "//*[text()='{}']/..".format(attr_text)
        class_v = self.base_get_ele_attribute(loc, "class")
        print(class_v)

    # 获取频道
    def base_web_get_channel_by_program(self, program_name):
        if type(program_name) is tuple:
            program_name = program_name[0]
            print("web tuple", program_name)
        return re.search(r".*?频道", program_name).group()

    # 节目单管理查询
    def base_web_program_search(self, channel, state, placeholder_text, program_name):
        log.info("正在调用web专属节目单管理查询封装方法")
        name = ""
        state1 = ""
        # 选择频道
        self.base_web_select_ele("所属频道", channel)
        # 选择审核状态
        self.base_web_select_ele("审核状态", state)
        # 搜索框输入节目单名称
        self.base_web_input_element(placeholder_text, program_name)
        sleep(0.5)
        # 点击查询按钮
        self.base_click(page.director_manage_search_btn)
        sleep(2)
        # 查看查询结果是否存在
        exist = self.base_ele_is_exist(page.director_manage_name_first)
        if exist:
            # 获取首条节目单名称
            name = self.base_get_text(page.director_manage_name_first)
            # 获取首条节目单审核状态
            state1 = self.base_get_text(page.director_manage_state_first)
        program_dict = {"exist": exist, "name": name, "state": state1}
        return program_dict
