import os

# 指定文件夹路径
folder_path = 'data'

# 使用os.listdir获取文件夹下的所有子文件夹和文件
items = os.listdir(folder_path)

# 使用列表推导式筛选出以"test_"开头的子文件夹
subfolders_starting_with_test = [item for item in items if os.path.isdir(os.path.join(folder_path, item)) and item.startswith("test_")]

# 打印满足条件的子文件夹列表
print(subfolders_starting_with_test)


folder_path = 'data/cycle_gan'

# \u4f7f\u7528os.listdir\u83b7\u53d6\u6587\u4ef6\u5939\u4e0b\u7684\u6240\u6709\u5b50\u6587\u4ef6\u5939\u548c\u6587\u4ef6
items = os.listdir(folder_path)

# \u4f7f\u7528\u5217\u8868\u63a8\u5bfc\u5f0f\u7b5b\u9009\u51fa\u4ee5"test_"\u5f00\u5934\u7684\u5b50\u6587\u4ef6\u5939
subfolders_starting_with_test = [item for item in items if os.path.isdir(os.path.join(folder_path, item)) and item.startswith("test_")]

# \u6253\u5370\u6ee1\u8db3\u6761\u4ef6\u7684\u5b50\u6587\u4ef6\u5939\u5217\u8868
print(subfolders_starting_with_test)

# 计算最大值、最小值、中位数和平均值
max_value = np.max(ans)
min_value = np.min(ans)
median_value = np.median(ans)
average_value = np.mean(ans)

# 打印结果
print("最大值:", max_value)
print("最小值:", min_value)
print("中位数:", median_value)
print("平均值:", average_value)