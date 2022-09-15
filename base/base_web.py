from selenium.webdriver.common.by import By

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