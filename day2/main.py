# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def sum_odd():
    a = [i for i in range(1, 101) if i % 2 == 1]
    sum(a)


def table():
    for i in range(1, 10):
        print('\n')
        for j in range(1, i + 1):
            print(f'{j}*{i}={j * i:<2}', end=' ')


def calculate_number():
    s = int(input('Enter a number: '))
    print(bin(s))
    if s >= 0:
        num = bin(s).count('1')
    else:
        num = 32 - bin(~s).count('1')
    print(num)


def use_method():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list1 = dict(enumerate(seasons))
    print({v: k for k, v in list1.items()})


if __name__ == '__main__':
    # table()
    use_method()
