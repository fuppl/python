
def sum_nums(num):
    if num == 1:
        return 1
    # 假设sum_nums已经可以处理1+...+num-1
    temp = sum_nums(num - 1)
    return temp + num


print(sum_nums(100))
