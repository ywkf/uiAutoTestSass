from selenium.webdriver.common.by import By


def find_attr_by_num(row, col):
    loc = By.XPATH, director_program_input[1].format(row, col)
    return loc


def find_btn_by_num(row, btn_num):
    loc = By.XPATH, director_program_button[1].format(row, attr_num.get("button"), btn_num)
    if btn_num == 6:
        loc = By.XPATH, director_program_delete_btn[1].format(row, attr_num.get("button"))
    return loc


"""项目配置地址"""

# url
url = "https://pre-admin.hndt.com/home"

# 节目制作账号
programing_phone = 19977777777
# 节目制作密码
programing_pwd = 123456
# 节目制作secret
programing_secret = "NE4WEQJZ7UTZGKRYUR5PTGOGU5OJ2ZIG"

# 频道导播账号
director_phone = 19933333333
# 频道导播密码
director_pwd = 123456
# 频道导播secret
director_secret = "ZUWHRTMFUO5RRMFE6JW2YB7W3SF3JC3G"

"""以下为登录页面元素配置信息"""
# 手机号
login_phone = By.CSS_SELECTOR, "#usernameVal"
# 密码
login_pwd = By.CSS_SELECTOR, "#passVal"
# 登录按钮
login_btn = By.CSS_SELECTOR, "#submit"
# 动态口令
login_code = By.CSS_SELECTOR, "#codeNum"
# 动态口令标识
login_codem_mark = By.CSS_SELECTOR, "[class='layui-form-label']"
# 忘记谷歌码按钮
login_google_code_btn = By.CSS_SELECTOR, ".layui-layer-btn2"
# QRCode
login_qrcode = By.CSS_SELECTOR, "#qrcode"
# 动态口令确定按钮
login_confirm_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
# 登录提示信息
login_msg = By.CSS_SELECTOR, ".layui-layer-content"
# 选择租户
login_hntv = By.XPATH, "//*[text()='河南广播电视台']"
# 立即进入按钮
login_enter_btn = By.XPATH, "//button//*[contains(text(),'进入')]"
# 租户名称
login_tenant = By.XPATH, "//main//*[@style='color: rgb(255, 255, 255);']"
# 退出系统
login_logout = By.XPATH, "//*[text()='退出系统']"

# 日期选择框
date_select = By.CSS_SELECTOR, "[placeholder='选择日期']"
# 当前年份选择
date_year_select = By.XPATH, "//span[contains(text(), '年')]"
# 当前月份选择
date_month_select = By.XPATH, "//span[contains(text(), '月')]"
# 年份列表
date_year_list = By.XPATH, "//td/a[@class='cell']"
# 日期表后一年
date_next_year = By.CSS_SELECTOR, "[aria-label='后一年']"
# 日期编前一年
date_last_year = By.CSS_SELECTOR, "[aria-label='前一年']"
# 日期表下个月
date_next_month = By.CSS_SELECTOR, "[aria-label='下个月']"
# 日期表上个月
date_last_month = By.CSS_SELECTOR, "[aria-label='上个月']"
# 节目单日期
date_program = By.XPATH, "//*[@class='time']//span[1]"

# 节目编单
director_arrange = By.XPATH, "//*[text()='节目编单']/.."
# 创建周播单
director_create_week = By.XPATH, "//li//*[text()='创建周播单']"
# 周播单名称
director_week_name = By.XPATH, "//*[text()='周播单名称']/..//input"
# 开播时间
director_playtime = By.XPATH, "//*[@class='el-table_1_column_3   el-table__cell']//input"
# 时长
director_duration = By.XPATH, "//*[@class='el-table_1_column_4   el-table__cell']//input"
# 节目名称
director_program_name = By.XPATH, "//tr[{}]//*[@class='el-table_1_column_5   el-table__cell']//input"
# 节目定位
director_program_row = By.XPATH, "//tr[{}]//*[@class='el-table_1_column_{}   el-table__cell']"
# 节目属性输入框
director_program_input = By.XPATH, director_program_row[1] + "//input"
# 节目操作按钮
director_program_button = By.XPATH, director_program_row[1] + "//button[{}]"
# 属性编号
attr_num = {
                "play_mode": 2,
                "playtime": 3,
                "duration": 4,
                "program_name": 5,
                "program_type": 6,
                "column": 7,
                "prebroadcast_type": 8,
                "self_type": 9,
                "button": 10
           }
# 按钮编号
button_num = {
                "sort_up": 1,
                "sort_down": 2,
                "plus": 3,
                "delete": 6
             }
# 节目删除按钮
director_program_delete_btn = By.XPATH, director_program_row[1] + "//*[@class='el-icon-delete']//.."
# 删除确定按钮
director_program_delete_confirm_btn = By.XPATH, "//*[@aria-hidden='false']//*[normalize-space(text())='确定']"
# 复选框down
director_selector = By.XPATH, "//*[@x-placement='bottom-start']//*[text()='{}']/.."
# 复选框up
director_selector_or = By.XPATH, "//*[@x-placement='top-start']//*[text()='{}']/.."
# 错误信息数量
director_error_num = By.XPATH, "//sup"
# 周
director_week_num = By.CSS_SELECTOR, "#tab-{}"
# week编号
week_num = {
    "周一": 1,
    "周二": 2,
    "周三": 3,
    "周四": 4,
    "周五": 5,
    "周六": 6,
    "周日": 0,
}
# 新建按钮
director_new_btn = By.XPATH, "//*[normalize-space(text())='新建']/.."
# 提交按钮
director_submit_btn = By.XPATH, "//*[normalize-space(text())='提交']/.."
# 周播单
director_week_program = ""
# 创建日播单
director_create_day = By.XPATH, "//li//*[text()='创建日播单']"