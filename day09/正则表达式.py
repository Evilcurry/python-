import re


def single():
    """"""
    # 匹配单个字符，只能匹配一个字符串
    result = re.match(".", "M")
    if result:
        print(result.group())
    result = re.match(".", "M")
    if result:
        print(result.group())
    result = re.match("t.", "two")
    if result:
        print(result.group())
    result = re.match("t.o", "two")
    if result:
        print(result.group())
    # 小写大写都可以
    result = re.match("[hH]", "hello python")
    if result:
        print(result.group())

    result = re.match("[hH]", "Hello Python")
    if result:
        print(result.group())
    # 匹配 0 到 9 第一种写法
    ret = re.match("[0123456789]Hello Python", "7Hello Python")
    print(ret.group())
    # 匹配 0 到 9 第二种写法
    ret = re.match("[0-9]Hello Python", "7Hello Python")
    print(ret.group())
    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())

    # 使用\d 进行匹配
    ret = re.match(r"嫦娥\d 号", "嫦娥 1 号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d 号", "嫦娥 2 号发射成功")
    print(ret.group())
    ret = re.match(r"嫦娥\d 号", "嫦娥 3 号发射成功")
    print(ret.group())


def multiple():
    """
    多字符匹配
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())
    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())

    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        ret = re.match(r"[a-zA-Z_]\w*", name)
        if ret:
            print(f'{name}合法')
        else:
            print(f'{name}不合法')

    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())
    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())
    # 匹配0-99
    ret = re.match(r"[1-9]?\d$", "09")
    if ret:
        print(ret.group())
    else:
        print('不是0-99')
    ret = re.match(r"[1-9]?\d", "0")
    print(ret.group())
    ret = re.match(r"[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match(r"[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
    print(ret.group())


def start_end():
    """
    匹配结尾
    :return:
    """
    # 符合163的邮箱找出来
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang @ qq.com"]
    for email in email_list:
        ret = re.match(r"\w{4,20}@163\.com$", email)  # 匹配的字符串中出现正则的符号需要转义\
        if ret:
            print(f'{ret.group()}是邮箱')
        else:
            print(f'{email}邮箱地址不正确')


def divide_group():
    """
    匹配分组
    :return:
    """
    # 匹配0-100
    ret = re.match(r"[1-9]?\d$|100", "8")
    print(ret.group())
    # 匹配1-99
    ret = re.match(r"[1-9][0-9]|[1-9]", "9")
    print(ret.group())
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
    if ret:
        print(ret.group())
    else:
        print("不是 163、126、qq 邮箱")  # 不是 163、126、qq 邮箱
    # ([ ^ -] *)代表没有遇到小横杠 - 就一直进行匹配，一直匹配下去
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmlbalabala>")
    if ret:
        print(ret.group())
    else:
        print(f'这是一对不正确的标签')
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com < / h2 > < / html > "]
    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print(f'{ret.group()}是符合要求的标签')
        else:
            print(f'{label}不符合要求')


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def other_func():
    """
    search findall sub split
    :return:
    """

    ret = re.search(r"\d+", "阅读次数为 9999")
    print(ret.group())
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 99")
    print(ret)
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"
    new_text = re.sub(pattern, replacement, text, count=2)
    print(new_text)


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


def use_finditer():
    """
    使用finditer函数
    :return:
    """
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)


def use_findall():
    s = 'hello world, now is 2020/7/20 18:48, 现在是 2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)
    # findall 内部设计机制，在分组前面加?:
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)
    # search没问题
    ret = pattern.search(ret_s)
    print(ret.group())


def use_sub():
    long_text = """
    <div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握 HTTP 协议，熟悉 MVC、MVVM 等概念以及相关 WEB 开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<
br></p>
<p>4、掌握 NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>
    """
    ret = re.sub(r"<[^>]*>|&nbsp;|\n|\s", "", long_text)
    print(ret)


if __name__ == '__main__':
    # multiple()
    # start_end()
    # divide_group()
    # other_func()
    # use_finditer()
    # use_findall()
    use_sub()
