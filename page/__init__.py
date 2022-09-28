from selenium.webdriver.common.by import By

from tools.read_yaml import read_yaml


def find_attr_by_num(row, col):
    loc = By.XPATH, director_program_input[1].format(row, 1, col)
    return loc


def find_btn_by_num(row, btn_num):
    loc = By.XPATH, director_program_button[1].format(row, 1, attr_num.get("button"), btn_num)
    if btn_num == 6:
        loc = By.XPATH, director_program_delete_btn[1].format(row, 1, attr_num.get("button"))
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

# 频道审核账号
channel_audit_phone = 19922222222
# 频道审核密码
channel_audit_pwd = 123456
# 频道审核secret
channel_audit_secret = "ZOAXCQ2DGICS45UX667T2SBGOOABB6YA"

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

"""以下为节目编单（节目编排）页面元素配置信息"""
# 周播单
director_week_program = read_yaml("director.yaml")[0][1]
# 日播单
director_day_program = ""

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
director_create_week = By.XPATH, "//li//*[text()='创建周播单']/.."
# 周播单所属频道
director_belong_channel = By.XPATH, "//*[@for='channelId']/following-sibling::div[1]//input/.."
# 周播单名称
director_week_name = By.XPATH, "//*[text()='周播单名称']/..//input"

# 开播时间
director_playtime = By.XPATH, "//*[@class='el-table_1_column_3   el-table__cell']//input"
# 时长
director_duration = By.XPATH, "//*[@class='el-table_1_column_4   el-table__cell']//input"
# 节目名称
director_program_name = By.XPATH, "//tr[{}]//*[@class='el-table_1_column_5   el-table__cell']//input"

# 节目定位
director_program_row = By.XPATH, "//tr[{}]//*[@class='el-table_{}_column_{}   el-table__cell']"
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
                "button": 10,
                "signal": 7
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

# 创建日播单
director_create_day = By.XPATH, "//li//*[text()='创建日播单']"
# 所属周播单
director_belong_week = By.XPATH, "//*[@for='weekId']/following-sibling::div[1]//input/.."
# 播出日期
director_playdate = By.XPATH, "//*[@for='date']/following-sibling::div[1]//input/.."
# 排单名称
director_day_name = By.XPATH, "//*[text()='排单名称']/..//input"
# 播出日期列表
director_playdate_list = []

# 周播单管理
director_week_manage = By.XPATH, "//li//*[text()='周播单管理']/.."
# 周播单名称搜索框
director_week_search_name = By.CSS_SELECTOR, "[placeholder='周播单名称']"
# 查询按钮
director_manage_search_btn = By.XPATH, "//*[text()='查询']/.."
# 首条节目单名称
director_manage_name_first = By.CSS_SELECTOR, "[class='cell el-tooltip']"
# 首条节目单审核状态
director_manage_state_first = By.XPATH, "//div/span[contains(text(),'审核')]"

# 日播单管理
director_day_manage = By.XPATH, "//li//*[text()='日播单管理']/.."
# 日播单名称搜索框
director_day_search_name = By.CSS_SELECTOR, "[placeholder='节目单名称']"


"""以下为节目编单（审核）页面元素配置信息"""
# 周播单审核
audit_week = By.XPATH, "//li//*[text()='周播单审核']/.."
# 节目单名称搜索框
audit_search_name = By.CSS_SELECTOR, "[placeholder='节目单名称']"
# 查询按钮
audit_search_btn = By.XPATH, "//*[text()='查询']/.."
# 首条节目单名称
audit_first_program_name = By.XPATH, "//td//div[contains(text(),'播单')]"
# 首条节目单查看详情审核按钮
audit_first_info_btn = By.XPATH, "//*[text()='点击详情进行审核']/.."
# 审核通过按钮
audit_info_pass_btn = By.CSS_SELECTOR, "[class='el-button el-button--success el-button--small']"





