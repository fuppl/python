
def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_list = (1,2,3)
gl_dict = {"name" : "laosi"}
demo(gl_list,gl_dict)
print("*"*30)
# 在传参时指明元组与字典，称为拆包语法
demo(*gl_list, **gl_dict)
print("*"*30)
# 此过程称为拆包，拆包语法可以简化拆包过程
demo(1,2,3,name="laosi")