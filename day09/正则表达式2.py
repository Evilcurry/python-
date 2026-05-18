import re


def use_greedy():
    s = "This is a number 234-235-22-423"
    r = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(r.group(1))
    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))
    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))
    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))
    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))


def use_r():
    """
    r的作用：原生字符串
    :return:
    """
    mm = "c:\\a\\b\\c"
    print(mm)
    print(re.match("c:\\\\", mm).group())


def use_option():
    print(re.match(r"\w*", "abc函", flags=re.A).group())
    print(re.match(r"a*", "aA", flags=re.I).group())
    print(re.match(r".*", "abc\ndef", flags=re.S).group())


if __name__ == '__main__':
    # use_greedy()
    use_option()
