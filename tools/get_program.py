import datetime
import operator
import os
import re

import xlrd
from xlrd import xldate_as_datetime, xldate_as_tuple

from config import BASE_PATH

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

    def get_program(self, num):

        self.__table = self.excel.sheet_by_index(num)

        # filepath = BASE_PATH + os.sep + "data" + os.sep + filename
        # excel1 = xlrd.open_workbook(self.filepath)
        # table = self.excel.sheet_by_index(num)

        print('get_prog -> ', self.__table.row_values(3))

        dated0 = self.__table.row_values(1)
        dated = self.__date_t(dated0).strip()
        print('get_prog date -> ', dated)
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

        list1 = []
        list2 = []
        list_week = []
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
                tag_name = tag[6:]
                if operator.contains(tag_name, '好剧'):
                    tag_name = tag_name[:7]
                elif operator.contains(tag_name, '剧场'):
                    tag_name = tag_name[:8]
                # 模板名称
                copy_name = '000000' + tag_name

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

                list1.append({'tag': tag, 'time': time2, 'copy_name': copy_name, 'month': M, 'day': D, 'date': date})
                list2.append((tag, time, copy_name, M, D, date))
                list_week.append({"row": num1, "duration": str(time2), "program_name": tag_name, "column": "河南法治报道"})
                nums += 1

        print('get_prog nums -> ', nums)
        return list_week

    def get_info(self, num):

        self.__table = self.excel.sheet_by_index(num)

        # 日期
        date0 = self.__table.row_values(1)
        date1 = self.__date_t(date0).strip()
        datel = re.findall("\d+", date1)
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

        info_list = [(channel, date_dict, playtime)]

        return info_list


if __name__ == '__main__':
    get_prog = GetProgram("2022.8.1--2022.8.7.xlsx")
    print(get_prog.get_program(6))
    print(get_prog.get_info(6))