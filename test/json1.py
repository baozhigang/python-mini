# 序列化与反序列化
import json

data = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

data2 = json.dumps(data)

res = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# dumps 序列化python obj到json字符串
# dump 序列化python obj成json字符串 到文件
res = json.dumps({'4':5, '6':7}, sort_keys=True, indent=4)

# loads vs load 同上
res = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# JSONEncoder JSONDecoder 属于扩展，作用类似于 dumps 和 loads
res = json.JSONEncoder().encode({"foo": ["bar", "baz"]})

res = json.JSONDecoder().decode(res)

print(res)

# ujson 是比json更快的工具，纯C语言写的
