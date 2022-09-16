from selenium.webdriver.common.by import By


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

