hello_str = "hello world"
# 查看是否以指定字符串开始
print(hello_str.startswith("hel"))
# 查看是否以指定字符串结束
print(hello_str.endswith("rld"))
# 查找指定指定字符串
# 和index 方法类似，区别是，find找不到不会报错，显示-1
print(hello_str.find("llo"))
# 替换指定字符串
# hello_str 中内容并未改变
print(hello_str.replace("llo", "lala"))
print(hello_str)