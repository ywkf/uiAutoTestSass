from selenium.webdriver.common.by import By

from base.base import Base


class BaseWeb(Base):

    # 鼠标移动
    def base_web_mouse_move_to(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        el = self.base_find_element(loc, timeout, poll)
        self.action.move_to_element(el).perform()

    # 鼠标双击
    def base_web_mouse_double_click(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素定位信息
        :param timeout: 超时时间
        :param poll: 查找频率
        """
        el = self.base_find_element(loc, timeout, poll)
        self.action.double_click(el).perform()

    # 选择租户
    def base_web_select_tenant(self, tenant):
        """
        :param tenant: 选择租户
        """
        login_tenant = By.XPATH, "//*[@class='name'][text()='{}']".format(tenant)
        self.base_click(login_tenant)