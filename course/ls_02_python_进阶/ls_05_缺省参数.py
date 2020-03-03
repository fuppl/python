# 为参数设置默认值，有默认值的参数称为缺省参数
# 缺省参数必须定义在参数列表的末尾
def print_info(name, title = "学生", gender = True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_text))


name ="xiaoming"
# 传参时可用0和1表示True和False
# 有多个缺省参数需要指定参数
print_info(name, gender=False)