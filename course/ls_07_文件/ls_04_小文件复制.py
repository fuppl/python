file1 = open(input("想要复制的文件"))
file2 = open(input("复制的目标文件"),"w")

file2.write(file1.read())

file1.close()
file2.close()