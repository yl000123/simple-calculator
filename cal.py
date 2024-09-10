# 计算器功能实现
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "除数不能为0"
        else:
            return num1 / num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "无效的运算符"


# 用户输入
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符（+，-，*，/，**）：")
num2 = float(input("请输入第二个数字："))

# 执行计算
result = calculate(num1, num2, operator)

# 输出结果
if isinstance(result, str):
    print(result)
else:
    print(f"结果是：{result}")