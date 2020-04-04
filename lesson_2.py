# 练习1-华氏温度转换为摄氏温度。提示：华氏温度到摄氏温度的转换公式为：C=(F - 32) \div 1.8。
import math


def F2C():
    while True:
        try:
            F = float(input('请输入华氏温度:'))
            C = (F - 32) / 1.8
            print("华氏温度:%.1f，摄氏温度:%.1f" % (F, C))
        except ValueError:
            print("输入内容不正确，请重试！")


# 练习2-输入圆的半径计算计算周长和面积。
def RoundArea():
    while True:
        try:
            R = float(input("请输入圆的半径:"))
            S = math.pi * R * R
            C = 2 * math.pi * R
            print("圆面积是: %.2f, 周长是: %.2f" % (S, C))
        except ValueError:
            print("输入内容不正确，请重试！")


# 练习3-输入年份判断是不是闰年。
def LeapYear():
    while True:
        try:
            year = int(input("请输入年份:"))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("%d年是闰年" % year)
            else:
                print("%d年是平年" % year)
        except ValueError:
            print("输入内容不正确，请重试！")
