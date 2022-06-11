# list 等于 PHP 的array

from collections import deque


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

res = fruits.count('apple')  # PHP的 array_count_values

res = fruits.index('banana', 4)  # PHP的 array_search

fruits.reverse()  # PHP的 array_reverse

fruits.append('boluomi')  # PHP的 array_push

fruits.sort()  # PHP的 sort

res = fruits.pop()  # PHP的 array_pop


# use list as stack

stack = [3, 4, 5]  # 实际上只是变量名变了而已

stack.append(6)


# use list as queue

queue = deque(["aaa", "bbb", "ccc"])

queue.append("ddd")

res = queue.popleft()

# print(res)
# print(queue)

squares = []
for x in range(10):
    squares.append(x**2)


squares2 = [x**2 for x in range(10)]

# del 相当于PHP的unset

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
del a[2:4]

# tuple  这个数据结构很随意啊，我靠
"""
创建速度比list快，
空间开销小，
元素不可更改，可作为dict的键
"""
t = 12345, 54321, 'hello!'
u = t, (11, 22)
x, y, z = t


# Sets PHP没有默认的set,有set类
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
if 'apple2' in basket:
    print(1)
else:
    print(2)

a = set('abracadabra')  # 集合是不重复的

b = {x for x in 'abracadabra' if x not in 'abc'}


# dict  map 类型
tel = {'jack': 4098, 'sape': 4139}

# loop
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
# print('what is your {0}? it is {1}.'.format(q, a))

# print(list(tel))

res = str.split("AA|BB|CC", '|')
res = str.strip("城市", "城")

# generators
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn(10)))


# print(res)
