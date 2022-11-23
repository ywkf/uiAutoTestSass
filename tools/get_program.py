import datetime
import operator
import os
import re

import xlrd
import yaml
from xlrd import xldate_as_datetime, xldate_as_tuple

from config import BASE_PATH
from tools.read_yaml import read_yaml

month_dict = {
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九',
        '10': '十',
        '11': '十一',
        '12': '十二',
    }


class GetProgram:

    __excel = None
    __table = None

    def __init__(self, filename):
        self.filename = filename
        self.filepath = BASE_PATH + os.sep + "data" + os.sep + filename
        if self.__excel is None:
            self.excel = xlrd.open_workbook(self.filepath)

    def __date_t(self, dated):
        for i in dated:
            if len(i.strip()) != 0:
                return i

    def __time_format(self, value):
        time1 = xldate_as_tuple(value, 0)
        time2 = datetime.time(*time1[-3:-1])
        return time2

    def __get_date(self, num):

        self.__table = self.excel.sheet_by_index(num)

        dated0 = self.__table.row_values(1)
        dated = self.__date_t(dated0).strip()
        # print('get_prog date -> ', dated)
        dated1 = dated.split()[1].split('月')
        y = dated1[0].split('年')[0].strip()
        m = dated1[0].split('年')[1]
        d = dated1[1].split('日')[0]
        w = dated[-1]
        M = month_dict.get(m) + '月'
        D = d
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        date = y + '-' + m + '-' + d
        return date

    def program_decons(self, num):

        self.__table = self.excel.sheet_by_index(num)

        # filepath = BASE_PATH + os.sep + "data" + os.sep + filename
        # excel1 = xlrd.open_workbook(self.filepath)
        # table = self.excel.sheet_by_index(num)

        # print('get_prog -> ', self.__table.row_values(3))

        dated0 = self.__table.row_values(1)
        dated = self.__date_t(dated0).strip()
        # print('get_prog date -> ', dated)
        dated1 = dated.split()[1].split('月')
        y = dated1[0].split('年')[0].strip()
        m = dated1[0].split('年')[1]
        d = dated1[1].split('日')[0]
        w = dated[-1]
        M = month_dict.get(m) + '月'
        D = d
        if len(m) == 1:
            m = '0' + m
        if len(d) == 1:
            d = '0' + d
        date = y + '-' + m + '-' + d

        list1 = []
        list2 = []
        list_week = []
        list_signal = []
        list_decons = []
        rows = self.__table.nrows
        nums = 1
        for i in range(rows):
            col = self.__table.row_values(i)
            if i >= 3 and len(col[3].strip()) != 0:

                time1 = xldate_as_tuple(col[4], 0)
                time2 = datetime.time(*time1[-3:-1])

                dateH = xldate_as_datetime(col[4], 0).strftime('%H')
                dateM = xldate_as_datetime(col[4], 0).strftime('%M')
                dateS = xldate_as_datetime(col[4], 0).strftime('%S')
                # 节目编号
                num1 = str(col[0]).split('.0')[0]
                if len(num1) == 1:
                    num01 = '0' + num1
                num = m + d + num01
                tag = num + col[3].strip()
                tag = tag.replace(' ', '')
                time = dateH + ':' + dateM + ':' + dateS
                date = y + '-' + m + '-' + d
                # 节目名称
                tag_name0 = tag[6:]
                if operator.contains(tag_name0, '好剧'):
                    tag_name = tag_name0[:7]
                elif operator.contains(tag_name0, '剧场'):
                    tag_name = tag_name0[:8]
                # 模板名称
                copy_name = '000000' + tag_name0

                if w == '三':
                    if i == 3:
                        tag = num + col[3].strip().replace('                  ', ' ')
                        copy_name = '000000法治测试卡 *（1）'
                    if i == 4:
                        tag = num + col[3].strip().replace('                  ', ' ')
                        copy_name = '000000法治测试卡 *（2）'
                    if i == 30:
                        copy_name = '000000法治黄金剧场-03'
                if w != '三' and i == 35:
                    copy_name = '000000法治黄金剧场-03'
                    if w == '日' and i == 35:
                        copy_name = '000000法治黄金剧场-3（周日）'

                mode = col[1].strip()
                signal = col[5].strip()

                list1.append({'tag': tag, 'time': time2, 'copy_name': copy_name, 'month': M, 'day': D, 'date': date})
                list2.append((tag, time, copy_name, M, D, date))
                list_week.append({"row": num1, "duration": str(time2), "program_name": tag_name0, "column": "河南法治报道"})
                list_signal.append({"row": num1, "play_mode": mode, "signal": signal, "date": date})
                nums += 1

        list_decons.append(list_week)
        list_decons.append(list_signal)

        # print('list_decons nums -> ', nums)
        return list_decons

    # 获取节目单
    def get_program(self, num):
        return self.program_decons(num)[0]

    # 获取信号源
    def get_signal(self, num):
        return self.program_decons(num)[1]

    # 获取当周日期
    def get_week_date(self):
        week_date = []
        for i in range(7):
            week_date.append(self.__get_date(i))
        return week_date

    # 根据日期获取节目单
    def get_program_by_date(self, date):
        num = [i for i, x in enumerate(self.get_week_date()) if x == date]
        return self.get_program(num[0])

    # 根据日期获取信号源
    def get_signal_by_date(self, date):
        num = [i for i, x in enumerate(self.get_week_date()) if x == date]
        return self.get_signal(num[0])

    # 生成 director.yaml, director_day.yaml, audit_day.yaml
    def generate_test_yaml(self, filename_director="director.yaml", filename_day="director_day.yaml", filename_audit="audit_day.yaml"):
        # 文件路径
        filename_director = BASE_PATH + os.sep + "data" + os.sep + filename_director
        filepath_day = BASE_PATH + os.sep + "data" + os.sep + filename_day
        filepath_audit = BASE_PATH + os.sep + "data" + os.sep + filename_audit
        # 获取周播单名称和频道
        program_info = self.get_info(0)
        week_name = program_info.get("week_program")
        channel = program_info.get("channel")
        # 生成dict
        director_dict = {}
        day_dict = {}
        day_audit = {}
        for i in range(7):
            day_dict["directorDay00{}".format(i+1)] = {"day_name": channel + self.__get_date(i) + "日播单", "state": "审核中"}
            day_audit["auditDay00{}".format(i+1)] = {"day_name": channel + self.__get_date(i) + "日播单", "state": "审核通过"}
        director_dict["director001"] = {"filename": self.filename, "week_name": week_name}
        # json转yaml
        director_yaml = yaml.dump(director_dict, indent=2, sort_keys=False, allow_unicode=True)
        day_yaml = yaml.dump(day_dict, indent=2, sort_keys=False, allow_unicode=True)
        audit_yaml = yaml.dump(day_audit, indent=2, sort_keys=False, allow_unicode=True)
        # 写入文件
        with open(filepath_day, "w", encoding="utf-8") as f:
            f.write(day_yaml)
        with open(filepath_audit, "w", encoding="utf-8") as f:
            f.write(audit_yaml)
        with open(filename_director, "w", encoding="utf-8") as f:
            f.write(director_yaml)
        yaml_dict = {"director": director_yaml, "director_day": day_yaml, "audit_day": audit_yaml}
        return yaml_dict

    # 获取基本信息
    def get_info(self, num):

        self.__table = self.excel.sheet_by_index(num)

        # 日期
        date0 = self.__table.row_values(1)
        date1 = self.__date_t(date0).strip()
        datel = re.findall("\\d+", date1)
        date_dict = {
            "year": datel[0],
            "month": month_dict.get(datel[1]) + '月',
            "day": datel[2]
        }

        # 频道
        channel0 = self.__table.row_values(0)
        channel1 = self.__date_t(channel0).strip()
        channel = re.search(".{2}频道", channel1).group()

        # 开播时间
        time0 = self.__table.cell_value(3, 2)
        playtime = str(self.__time_format(time0))

        # 周播单名称
        week_program = channel + self.get_week_date()[0] + " - " + self.get_week_date()[-1] + "周播单"

        # 日播单名称
        self.get_week_date()

        info_list = [(channel, date_dict, playtime)]
        info_dict = {"channel": channel, "date": date_dict, "playtime": playtime, "week_program": week_program}

        return info_dict


# 选择文件
def select_file():
    # 获取xlsx文件名称
    filepath = BASE_PATH + os.sep + "data"
    filelist = os.listdir(filepath)
    data_list = []
    data_name = ""
    for i in filelist:
        if i.endswith(".xlsx") and i.startswith("2"):
            data_list.append(i)
    if len(data_list) != 1:
        print("data目录中存在多个xlsx文件：", data_list)
        data_name = input("选择文件：")
    else:
        data_name = data_list[0]
    print("已选择：", data_name)
    return data_name


# 生成 director.yaml, director_day.yaml, audit_day.yaml
def generate_yaml(data_name):
    get_prog = GetProgram(data_name)
    yaml_dict = get_prog.generate_test_yaml()
    print("生成yaml文件：director.yaml, director_day.yaml, audit_day.yaml\n\n", yaml_dict.get("director"), "\n", yaml_dict.get("director_day"), "\n", yaml_dict.get("audit_day"), sep="")


# 初始化
def director_test_init():
    da_name = select_file()
    generate_yaml(da_name)


# 清空report目录
# report_path = BASE_PATH + os.sep + "report" + os.sep
def clear_report(path=BASE_PATH + os.sep + "report" + os.sep):
    i = input("clear report (Y/N)? ")
    if i == "Y" or i == "y":
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                clear_report(c_path)
            else:
                os.remove(c_path)
        print("report clear")
    else:
        exit()


if __name__ == '__main__':
    # 初始化生成yaml测试数据
    director_test_init()
    # 清空report
    # clear_report()

    # get_prog = GetProgram(data_name)
    # print(get_prog.get_program(6))
    # print(get_prog.get_info(6))
    # print(get_prog.get_signal(6))
    # print(get_prog.get_signal_by_date('2027-08-16'))
    # print(get_prog.get_week_date())

    # 生成 director.yaml, director_day.yaml, audit_day.yaml
    # yaml_dict = get_prog.generate_director_day_yaml()
    # print("生成yaml文件：director.yaml, director_day.yaml, audit_day.yaml\n\n", yaml_dict.get("director"), "\n", yaml_dict.get("director_day"), "\n", yaml_dict.get("audit_day"), sep="")

    # 清空report目录
    # get_prog.clear_report()

