import pymysql
import xlrd
from openpyxl import load_workbook


def open_excel():
    try:
        book = xlrd.open_workbook("材料院2021-2022-1选课.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


def insert_deta():
    sheet = open_excel()

    num = 1
    while 1:
        cell = sheet.cell(row=num, column=1).value
    if cell:
        num = num + 1
    print(num)



open_excel()
insert_deta()