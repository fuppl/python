num_str = "1"
num_str1 = "\u00b2"
num_str2 = "一千零一"
# 判断字符串是否只包含数字
# 1.三种方法都不能判断小数
# 2.isdigit 和 isnumeric 比 isdecimal 强大一些，后者只能判断正常数字，前两者可以判断带有数字的符号，如平方
# isnumeric 还可以判断中文数字
print(num_str)
print(num_str1)
print(num_str.isdecimal())
print(num_str1.isdecimal())
print(num_str.isdigit())
print(num_str1.isdigit())
print(num_str.isnumeric())
print(num_str1.isnumeric())
print(num_str2.isnumeric())