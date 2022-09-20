import operator

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
        log.info("正在调用web专属选择日期封装方法")
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
    def base_web_find_by_num(self, row, col):
        loc = "//tr[{}]//*[@class='el-table_1_column_{}   el-table__cell']//input".format(row, col)
        return self.base_find_element(loc, timeout=30, poll=0.5)

    # 下拉框选择
    def base_web_selector(self, text):
        sleep(0.5)
        loc = (page.director_selector[0], page.director_selector[1].format(text))
        self.base_click(loc)




