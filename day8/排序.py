import random
import time
import sys

sys.setrecursionlimit(10 ** 6)  # 设置递归深度限制


class Sort:
    def __init__(self, n):
        """"
        n is the number of elements in the list
        """
        self.length = n
        self.array = [0] * n
        self.random_date()

    def random_date(self):
        for i in range(self.length):
            self.array[i] = random.randint(0, 99)

    def partition(self, left, right):
        arr = self.array
        k = i = left
        for i in range(left, right):
            if arr[i] <= arr[right]:  # 如果当前元素小于等于基准元素，交换它们的位置
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, length):
        """
        把某颗子树调整为最大堆
        :param pos:被调整元素的位置
        :param length:当时列表总长度
        :return:
        """
        arr = self.array
        dad = pos
        son = 2 * dad + 1
        while son < length:#做孩子小于arr_length
            if son + 1 < length and arr[son] < arr[son + 1]:  # 如果存在右孩子，并且右孩子比左孩子大，则将son指向右孩子
                son = son + 1
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_sort(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.length)
        arr = self.array
        for j in range(self.length - 1, 0, -1):
            arr[0], arr[j] = arr[j], arr[0]
            self.adjust_max_heap(0, j)

    def time_test(self, sort_func, *args, **kwargs):
        """
        回调函数
        :param sort_func:
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.time()
        sort_func(*args, **kwargs)
        end_time = time.time()
        print(f'It cost {end_time - start_time} seconds')


if __name__ == '__main__':
    my_sort = Sort(2)
    print(my_sort.array)
    # start = time.time()
    my_sort.quick_sort(0,my_sort.length - 1)
    # my_sort.heap_sort()
    # end = time.time()
    print(my_sort.array)
    # print(f'It cost {end - start}')
