import operator
import os

import xlrd
from xlrd import xldate_as_datetime

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

    def __init__(self, filename, num):
        self.filepath = BASE_PATH + os.sep + "data" + os.sep + filename
        self.excel = xlrd.open_workbook(self.filepath)
        self.table = self.excel.sheet_by_index(num)

    def date_t(self, dated):
        for i in dated:
            if len(i.strip()) != 0:
                return i

    def get_program(self):

        # filepath = BASE_PATH + os.sep + "data" + os.sep + filename
        # excel1 = xlrd.open_workbook(self.filepath)
        # table = self.excel.sheet_by_index(num)

        print('get_prog -> ', self.table.row_values(3))

        dated0 = self.table.row_values(1)
        dated = self.date_t(dated0).strip()
        print('get_prog -> ', dated)
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
        rows = self.table.nrows
        nums = 1
        for i in range(rows):
            col = self.table.row_values(i)
            if i >= 3 and len(col[3].strip()) != 0 and col[5].strip() != '140ST1#':
                dateH = xldate_as_datetime(col[4], 0).strftime('%H')
                dateM = xldate_as_datetime(col[4], 0).strftime('%M')
                dateS = xldate_as_datetime(col[4], 0).strftime('%S')
                num1 = str(col[0]).split('.0')[0]
                if len(num1) == 1:
                    num1 = '0' + num1
                num = m + d + num1
                tag = num + col[3].strip()
                tag = tag.replace(' ', '')
                time = dateH + ':' + dateM + ':' + dateS
                date = y + '-' + m + '-' + d

                tag_name = tag[6:]
                if operator.contains(tag_name, '好剧'):
                    tag_name = tag_name[:7]
                elif operator.contains(tag_name, '剧场'):
                    tag_name = tag_name[:8]
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

                list1.append({'tag': tag, 'time': time, 'copy_name': copy_name, 'month': M, 'day': D, 'date': date})
                list2.append((tag, time, copy_name, M, D, date))
                nums += 1

        print('get_prog -> ', nums)
        return list2

    def get_date(self):
        dated0 = self.table.row_values(1)
        dated = self.date_t(dated0).strip()
        print('get_prog -> ', dated)


if __name__ == '__main__':
    print(GetProgram("2022.8.1--2022.8.7.xlsx", 1).get_program())