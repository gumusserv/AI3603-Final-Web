import os
import shutil

# 原始图片所在文件夹路径
input_folder = 'test'

# 获取test文件夹下所有jpg图片的文件名
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]
print(image_files)

# 遍历每张图片
for image_file in image_files:
    # 获取图片的文件名（不包括扩展名）
    image_name = os.path.splitext(image_file)[0]
    
    # 创建新文件夹test_{name}
    new_folder = f'test_{image_name}'
    os.makedirs(new_folder, exist_ok=True)
    
    # 在新文件夹内创建testA和testB文件夹
    testA_folder = os.path.join(new_folder, 'testA')
    testB_folder = os.path.join(new_folder, 'testB')
    os.makedirs(testA_folder, exist_ok=True)
    os.makedirs(testB_folder, exist_ok=True)
    
    # 复制图片到testA和testB文件夹
    image_path = os.path.join(input_folder, image_file)
    shutil.copy(image_path, testA_folder)
    shutil.copy(image_path, testB_folder)
