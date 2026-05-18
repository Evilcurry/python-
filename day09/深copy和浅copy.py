import copy
def use_list_copy():
    """
    使用list的copy方法复制一个列表,是浅copy
    :return:
    """
    a=[1,2,3]
    b=a.copy()
    b[0]=100
    print(id(a))
    print(id(b))

def use_copy1():
    """
    使用copy模块的copy方法
    :return:
    """
    a=[1,2,3]
    b=copy.copy(a)
    b[0]=100
    print(a)
    print(b)


def use_copy2():
    """
    copy是浅拷贝,只做第一层copy

    :return:
    """
    a=[1,2,3]
    b=[4,5,6]
    c=[a,b]
    d=copy.copy(c)
    print(id(c))
    print(id(d))

def use_deepcopy():
    """
    递归去copy,深拷贝
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b]
    d=copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0]=100
    print(a)
    print(b)

if __name__ == '__main__':
    use_list_copy()
    #use_copy1()
    #use_copy2()
    #use_deepcopy()
