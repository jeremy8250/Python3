# 练习1-英制单位英寸与公制单位厘米互换。
def inch2cm():
    while True:
        try:
            inch = float(input("请输入英寸:"))
            cm = inch * 2.54
            print("%.2f英寸=%.2f厘米" % (inch, cm))
        except ValueError:
            print("输入内容不正确，请重试！")


# 练习2-百分制成绩转换为等级制成绩。
def per2grade():
    while True:
        try:
            per = float(input("请输入成绩:"))
            if per < 60:
                print("你的等级为:E")
            elif 60 <= per < 70:
                print("你的等级为:D")
            elif 70 <= per < 80:
                print("你的等级为:C")
            elif 80 <= per < 90:
                print("你的等级为:B")
            elif 90 <= per <= 99:
                print("你的等级为:A")
            else:
                print("你的等级为:S")
        except ValueError:
            print("输入内容不正确，请重试！")


# 练习3-输入三条边长，如果能构成三角形就计算周长和面积。
def Triangle():
    while True:
        try:
            a = float(input("请输入第一条边长:"))
            b = float(input("请输入第二条边长:"))
            c = float(input("请输入第三条边长:"))
            if (a + b > c) and (a + c > b) and (b + c > a):
                C = (a + b + c)
                p = C / 2
                S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                print("三角形周长为:%.2f, 面积为:%.2f" % (C, S))
            else:
                print("不能构成三角形")
        except ValueError:
            print("输入内容不正确，请重试！")
