import subprocess

from tools.get_program import director_test_init, clear_report


# 执行测试用例
def run_test():
    subprocess.run("pytest")


# 生成测试报告
def generate_report():
    subprocess.run("allure serve report", shell=True)


if __name__ == '__main__':
    # 初始化生成yaml测试数据
    director_test_init()
    # 执行测试用例
    run_test()

    # 生成测试报告
    generate_report()
    # # 清空report
    # clear_report()

