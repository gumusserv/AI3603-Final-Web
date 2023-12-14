import os

# 指定两个文件夹的路径
folder1 = r"C:\Users\Lenovo\Desktop\cycle-gan\data\cycle_gan\test"
folder2 = r"C:\Users\Lenovo\Desktop\cycle-gan\data\cycle_gan\real2mural\testA"

# 获取两个文件夹中的文件列表
files1 = os.listdir(folder1)
files2 = os.listdir(folder2)

# 将文件名列表转换为集合，以便进行快速查找
file_set1 = set(files1)
file_set2 = set(files2)

# 找到两个文件夹中相同的文件
common_files = file_set1.intersection(file_set2)

# 打印相同文件的列表
if common_files:
    print("两个文件夹中相同的文件:")
    for file in common_files:
        print(file)
else:
    print("两个文件夹中没有相同的文件。")
