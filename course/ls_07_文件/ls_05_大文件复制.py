file1 = open(input("想要复制的文件"))
file2 = open(input("复制的目标文件"),"w")
while True:
    text = file1.readline()
    if not text:
        break
    file2.write(text)

file1.close()
file2.close()