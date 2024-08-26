"""
該程式目的是將mask內部的數值轉換成我們所想要的
ex: 2 --> 3
一切根據我們給定的change table

"""

import os
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# 路徑設定
# input_dir = "/home/gary/Desktop/code/dataset/FoodSeg103/Images/ann_dir/train"
# output_dir = "/home/gary/Desktop/code/dataset/FoodSeg103/Images/ann_dir/train_change_3"

input_dir = "/home/gary/Desktop/code/deeplabv3-plus-pytorch/VOCdevkit_2024_1/VOC2007/SegmentationClass"
output_dir = "/home/gary/Desktop/code/deeplabv3-plus-pytorch/VOCdevkit_2024_1/VOC2007/SegmentationClass_0607"

# 確保輸出資料夾存在    
os.makedirs(output_dir, exist_ok=True)

# 讀取更換表與顏色表
"""
==foodseg103 精簡化分類==
0	背景
1	畜牧肉
2	魚肉
3	蝦肉
4	貝肉
5	蛋類
6	甜點
7	水果類
8	堅果類
9	乳製品
10	蔬菜類
11	澱粉類
12	菇類
13	豆類
14	包子水餃
15	藻類
"""
change_table = [ #此為foodseg103原有分類整理至精簡分類
    0,6,6,11,6,6,6,6,6,9,6,0,0,0,0,0,0,8,11,8,7,13,8,8,5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,0,3,2,2,3,0,11,11,14,11,14,14,11,11,11,11,13,10,11,10,10,10,15,15,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,0,10,10,12,12,12,12,12,10,10
]

change_table_2 = [ #此為原分類合併至精簡分類的交換表
    0,1,10,10,10,11,5,12,13,2,2,3,7,15
]

# 使用 numpy vectorize 函數來取代內部的 for 迴圈
vectorized_change = np.vectorize(lambda x: change_table_2[x])
def process_image(file_name):
    if file_name.endswith(".png"):
        # 讀取圖片
        img_path = os.path.join(input_dir, file_name)
        img = Image.open(img_path)
        png = np.array(img)

        # 建立新的圖片陣列
        copy_png = np.zeros((*png.shape, 3), dtype=np.uint8)


        copy_png = vectorized_change(png)

        # 儲存修改後的圖片
        output_img = Image.fromarray(copy_png.astype(np.uint8))
        output_path = os.path.join(output_dir, file_name)
        output_img.save(output_path)
        # print(f"Processed {file_name}")




file_names = os.listdir(input_dir)


total_seg = []
for file in file_names:
    if file.endswith(".png"):
        total_seg.append(file)


num     = len(total_seg)  
list    = range(num)

for i in tqdm(list):

    process_image(total_seg[i])
print("所有圖片已處理完畢。")


