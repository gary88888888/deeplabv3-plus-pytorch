from PIL import Image
import numpy as np 


colors_rgb = [ [0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [128, 128, 128],
  [64, 0, 0], [192, 0, 0], [64, 128, 0], [192, 128, 0], [64, 0, 128], [192, 0, 128], [64, 128, 128], [192, 128, 128],
  [0, 64, 0], [128, 64, 0], [0, 192, 0], [128, 192, 0], [0, 64, 128] ]
colors = np.array(colors_rgb,dtype='uint8').flatten()

colors_rgb = np.array(colors_rgb)

print(colors_rgb)

file_name = 'aug_000001_131.png'

img  = Image.open(file_name)
img.show()


origin_paletee = img.getpalette()
origin_paletee = np.array(origin_paletee).reshape(-1,3)
img.putpalette(colors)

img_arrays = np.array(img)

paletee = np.array(img.getpalette()).reshape(-1,3)



# img.show()


for r in range(len(img_arrays)):
    for c in range(len(img_arrays[r])):
        old_color = origin_paletee[img_arrays[r][c]]
        index = np.where((colors_rgb == old_color).all(axis=1))[0][0]

        img_arrays[r][c] = index





img = Image.fromarray(img_arrays,'P')
img.putpalette(colors)

img.save('aug_000001_131_test.png')

img.show()
img_array = np.array(img)
print('數據維度格式',len(np.shape(img_array)))
print('總共幾種classes',np.unique(img_array))

classes_nums        = np.zeros([256], np.int)

classes_nums += np.bincount(np.reshape(img_array, [-1]),minlength=256)
print(classes_nums)



if len(np.shape(img_array)) > 2:
            
    print("标签图片%s的shape为%s，不属于灰度图或者八位彩图，请仔细检查数据集格式。")
    print("标签图片需要为灰度图或者八位彩图，标签的每个像素点的值就是这个像素点所属的种类。")




print("打印像素点的值与数量。")
print('-' * 37)
print("| %15s | %15s |"%("Key", "Value"))
print('-' * 37)
for i in range(256):
    if classes_nums[i] > 0:
        print("| %15s | %15s |"%(str(i), str(classes_nums[i])))
        print('-' * 37)