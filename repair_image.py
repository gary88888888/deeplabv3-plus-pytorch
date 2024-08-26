
from __future__ import print_function
from __future__ import division
import os, cv2
from skimage import io
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt
import tifffile as tif
# import torch, paddle
 
from collections import namedtuple
Cls = namedtuple('cls', ['name', 'id', 'color'])
Clss = [
    Cls('bg', 0, (0, 0, 0)),
    Cls('cls1', 1, (255, 128, 128)),
    Cls('cls2', 2, (255, 255, 128)),
    Cls('cls3', 3, (128, 255, 128)),
    Cls('cls4', 4, (128, 255, 255)),
    Cls('cls5', 5, (0, 128, 255)),
    Cls('cls6', 6, (255, 0, 0)),
    Cls('cls7', 7, (0, 128, 192)),
    Cls('cls8', 8, (255, 0, 255)),
    Cls('cls9', 9, (255, 128, 64)),
    Cls('cls10', 10, (128, 64, 0)),
    Cls('cls11', 11, (128, 128, 0)),
]
 
# region 灰度转彩色
def get_color8bit(grays_path, colors_path):
    '''
    灰度图转8bit彩色图
    :param grays_path:  灰度图文件路径
    :param colors_path: 彩色图文件路径
    :return:
    '''
    if not os.path.exists(colors_path):
        os.makedirs(colors_path)
    file_names = os.listdir(grays_path)
    bin_colormap = get_putpalette(Clss)
    with tqdm(file_names) as pbar:
        for file_name in pbar:
            gray_path = os.path.join(grays_path, file_name)
            color_path = os.path.join(colors_path, file_name.replace('.tif','.png'))
            gt = Image.open(gray_path)
            gt.putpalette(bin_colormap)
            gt.save(color_path)
            pbar.set_description('get color')
 
 
def get_putpalette(Clss, color_other=[0, 0, 0]):
    '''
    灰度图转8bit彩色图
    :param Clss:颜色映射表
    :param color_other:其余颜色设置
    :return:
    '''
    putpalette = []
    for cls in Clss:
        putpalette += list(cls.color)
    putpalette += color_other * (255 - len(Clss))
    return putpalette
 
 
# endregion
 
 
if __name__ == '__main__':
    pass
    grays_path = r'E:\1_dataset\NB_S11_mini100\data\gt'
    colors_path = r'E:\1_dataset\NB_S11_mini100\data\Visual\gt_color2'
    color_file = r'E:\1_dataset\NB_S11_mini100\data\Visual\gt_color2\22.png'
    get_color8bit(grays_path,colors_path)
 
    # 可正常读取
    img = Image.open(color_file)
    img = np.array(img)
    print(img.shape, np.unique(img))
    img = io.imread(color_file)
    print(img.shape, np.unique(img))
    # img = tif.imread(color_file) # 智能读取tif格式文件
    # print(img.shape, np.unique(img))
    # 不能正常读取
    img = cv2.imread(color_file, cv2.IMREAD_COLOR)
    print(img.shape, np.unique(img))
    img = cv2.imread(color_file, cv2.IMREAD_GRAYSCALE)
    print(img.shape, np.unique(img))