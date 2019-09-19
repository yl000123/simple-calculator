# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/18
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
from tkinter import *


class Cala():
    def __init__(self):
        self.master = Tk()
        self.master.title("简单计算器")

        self.show = Entry(self.master, text="")
        self.show.grid(row=0, columnspan=5)

        self.is_res = False  # 是不是上次计算的结果
        # 添加 1~9
        for i in range(1, 10):
            Button(self.master, text=i, width=5, height=2, command=lambda x=i: self.add_char(x)) \
                .grid(row=3 - (i - 1) // 3, column=(i - 1) % 3)
        # 添加 0 。
        Button(self.master, text="0", width=10, height=2, command=lambda: self.add_char("0")).grid(row=4,
                                                                                                   columnspan=2)
        Button(self.master, text=".", width=5, height=2, command=lambda: self.add_char(".")).grid(row=4,
                                                                                                  column=2)
        # 添加 + - * / =
        Button(self.master, text="+", width=5, height=2, command=lambda: self.add_char("+")).grid(row=1,
                                                                                                  column=3)
        Button(self.master, text="-", width=5, height=2, command=lambda: self.add_char("-")).grid(row=1,
                                                                                                  column=4)
        Button(self.master, text="×", width=5, height=2, command=lambda: self.add_char("×")).grid(row=2,
                                                                                                  column=3)
        Button(self.master, text="÷", width=5, height=2, command=lambda: self.add_char("÷")).grid(row=2,
                                                                                                  column=4)
        Button(self.master, text="=", width=10, height=2, command=self.computerX).grid(row=4,
                                                                                       column=3,
                                                                                       columnspan=2)
        # 添加 Del-删除一个字符，C-删除所有字符
        Button(self.master, text="Del", width=5, height=2, command=self.delete).grid(row=3,
                                                                                     column=3)
        Button(self.master, text="C", width=5, height=2, command=lambda: self.delete_all()).grid(row=3,
                                                                                                 column=4)

    def add_char(self, text):
        """将字符添加到显示框"""
        if str(text).isdigit() or text == ".":
            # 如果时数字或者"."，直接添加
            if self.is_res:
                self.delete_all()
                self.is_res = False
            self.show.insert(len(self.show.get()), text)
        else:
            # 如果时运算符，检查是否已经有运算符，检查是否是第一个字符
            self.is_res = False
            text_old = self.show.get()
            if not text_old:
                return
            if text_old[-1:] in "+-×÷":
                self.show.delete(len(self.show.get()) - 1)
            self.show.insert(len(self.show.get()), text)

    def delete(self):
        """删除最后一个字符"""
        self.show.delete(len(self.show.get()) - 1)

    def delete_all(self):
        """删除所有字符"""
        self.show.delete(0, len(self.show.get()))

    def update(self, res):
        """更新显示框"""
        if int(res) == res:
            res = int(res)
        self.delete_all()
        self.show.insert(0, res)

    def computerX(self):
        """考虑运算符计算"""
        # 求出前缀表达式
        text_old = self.show.get()
        text_old_split = [i for i in re.findall("\d*\.?\d*|\+|-|×|÷", text_old) if i]
        prefix_expression = []
        sign_stack = []
        for i in range(len(text_old_split)):
            char = text_old_split[-(i + 1)]
            if char.isdigit() or "." in char:
                prefix_expression.insert(0, char)
            else:
                if char in "+-":
                    if sign_stack:
                        while sign_stack:
                            # if not sign_stack:
                            #     sign_stack.append(char)
                            #     break
                            if sign_stack[-1] in "×÷":
                                prefix_expression.insert(0, sign_stack.pop())
                            else:
                                # sign_stack.append(char)
                                break
                        sign_stack.append(char)
                    else:
                        sign_stack.append(char)
                else:
                    sign_stack.append(char)
        if i == len(text_old_split) - 1:
                while sign_stack:
                    prefix_expression.insert(0, sign_stack.pop())
        print("前缀表达式为：", ' '.join(prefix_expression))

        # 求解前缀表达式（从右向左扫描）
        prefix_expression.reverse()
        result_stack = []
        for i in prefix_expression:
            if i.isdigit() or "." in i:
                result_stack.append(float(i))
            else:
                if i == "+":
                    result_stack.append(result_stack.pop() + result_stack.pop())
                if i == "-":
                    result_stack.append(result_stack.pop() - result_stack.pop())
                if i == "×":
                    result_stack.append(result_stack.pop() * result_stack.pop())
                if i == "÷":
                    result_stack.append(result_stack.pop() / result_stack.pop())
        assert len(result_stack) == 1
        res = result_stack[0]
        # 更新值
        print("res = %s" % res)
        self.is_res = True
        self.update(res)

    def computer(self):
        """计算结果"""
        text_old = self.show.get()
        if text_old:
            res = 0  # 结果
            digit = [float(i) for i in re.findall("\d*\.?\d*", text_old) if i]
            sign = re.findall("\+|-|×|÷", text_old)
            assert len(digit) == len(sign) or len(digit) - 1 == len(sign)
            if len(digit) == len(sign):
                digit.append(0)
            res = digit[0]
            for i, j in enumerate(sign):
                if j == "+":
                    print("%s + %s" % (res, digit[i + 1]))
                    res += digit[i + 1]
                if j == "-":
                    print("%s " - " %s" % (res, digit[i + 1]))
                    res -= digit[i + 1]
                if j == "×":
                    print("%s × %s" % (res, digit[i + 1]))
                    res *= digit[i + 1]
                if j == "÷":
                    print("%s ÷ %s" % (res, digit[i + 1]))
                    res += digit[i + 1]
            # 更新值
            print("res = %s" % res)
            self.is_res = True
            self.update(res)

    def run(self):
        self.master.mainloop()


if __name__ == '__main__':
    Cala().run()
