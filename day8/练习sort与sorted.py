my_list = "This is a test sting from Andrew".split()
print(my_list)


def change_lower(str_name: str):
    return str_name.lower()

#key传递一个比较规则的函数
#print(sorted(my_list, key=change_lower))
my_list.sort(key=change_lower)
#print(my_list)

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        """
        相对于str来说更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
print(sorted(student_objects, key=lambda student: student.age)) # sort by age
#lambda表达式就是匿名函数
#print(sorted(student_tuples, key=lambda x: x[1]))
#student = Student('john', grade=5, age=10)
#print(student)


game_result = [
{ "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]
from operator import itemgetter,attrgetter
print(f'引用operator系列')
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects, key=attrgetter('age')))
print(f'引用operator系列，多个排序')
print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_tuples, key=lambda x:(x[1],-x[2])))
print(sorted(student_objects, key=attrgetter('age', 'name')))
print(sorted(game_result, key=itemgetter('rating', 'name')))