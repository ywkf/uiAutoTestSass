"""项目配置地址"""
from selenium.webdriver.common.by import By

url = "https://pre-gw.hndt.com/uaa/login"

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
# 选择租户
login_hntv = By.XPATH, "//*[text()='河南广播电视台']"
# 立即进入按钮
login_enter_btn = By.XPATH, "//button//*[contains(text(),'进入')]"
# 租户名称
login_tenant = By.XPATH, "//main//*[@class='text']"
