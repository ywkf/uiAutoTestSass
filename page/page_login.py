from selenium.webdriver.common.by import By

import page
from base.base_web import BaseWeb
from tools.get_google_code import GetGoogleCode
from time import sleep


class PageLogin(BaseWeb):

    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 点击忘记谷歌码按钮
    def page_click_google_code(self):
        self.base_click(page.login_google_code_btn)

    # 获取 title 属性
    def page_get_title(self, attribute="title"):
        return self.base_get_ele_attribute(page.login_qrcode, attribute)

    # 输入动态口令
    def page_input_code(self, code):
        self.base_input(page.login_code, code)

    # 点击确定
    def page_click_confirm_btn(self):
        self.base_click(page.login_confirm_btn)

    # 获取登录提示信息
    def page_get_login_msg(self):
        return self.base_get_text(page.login_msg)

    # 选择租户
    def page_select_tenant(self, tenant='河南广播电视台'):
        self.base_web_select_tenant(tenant)

    # 点击立即进入按钮
    def page_click_enter_btn(self):
        self.base_click(page.login_enter_btn)

    # 获取租户名称
    def page_get_tenant_name(self):
        return self.base_get_text(page.login_tenant)

    # 组合登录方法
    def page_login(self, phone, pwd, secret):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        sleep(0.5)
        self.page_click_login_btn()
        code = GetGoogleCode().cal_google_code(secret)
        self.page_input_code(code)
        sleep(0.5)
        self.page_click_confirm_btn()
        self.page_select_tenant()
        self.page_click_enter_btn()

    # 登录依赖方法
    def page_login_success(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
        self.page_click_google_code()
        title = self.page_get_title()
        code = GetGoogleCode().get_google_code(title)
        sleep(0.5)
        self.page_click_confirm_btn()
        self.page_input_code(code)
        sleep(0.5)
        self.page_click_confirm_btn()
        sleep(1)
        self.page_select_tenant()
        self.page_click_enter_btn()

    # 组合登录方法(制作权限)
    def page_login_make(self, phone, pwd, secret):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        sleep(0.5)
        self.page_click_login_btn()
        code = GetGoogleCode().cal_google_code(secret)
        self.page_input_code(code)
        sleep(0.5)
        self.page_click_confirm_btn()
        sleep(1)



