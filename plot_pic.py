from PIL import Image


image2 = Image.open('/lustre/home/acct-stu/stu047/Desktop/cycle-gan/data/cycle_gan/test_e33556dc35/result.jpg')
image1 = Image.open('/lustre/home/acct-stu/stu047/Desktop/cycle-gan/data/cycle_gan/test_e33556dc35/testA/e33556dc35.jpg')
image3 = Image.open('/lustre/home/acct-stu/stu047/Desktop/cycle-gan/data/cycle_gan/test_ea60c54c69/testA/ea60c54c69.jpg')
image4 = Image.open('/lustre/home/acct-stu/stu047/Desktop/cycle-gan/data/cycle_gan/test_ea60c54c69/result.jpg')


# 调整369x369的图片大小到256x256
image2 = image2.resize((256, 256))
image4 = image4.resize((256, 256))

# 确定新画布的大小
new_width, new_height = 256 * 2, 256 * 2

# 创建新的画布
new_im = Image.new('RGB', (new_width, new_height))

# 将图片放置到画布上
new_im.paste(image1, (0, 0))
new_im.paste(image2, (256, 0))
new_im.paste(image3, (0, 256))
new_im.paste(image4, (256, 256))

# 保存新的图片
new_im.save('combined_image.jpg')
