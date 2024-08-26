import os
import numpy as np
import pandas as pd
from collections import defaultdict
from PIL import Image
from tqdm import tqdm
"""
該程式是用來找出該資料集的類別分佈狀態
"""
def count_pixel_values(folder_path):
    pixel_count = defaultdict(int)
    total_pixels = 0

    # 獲取資料夾內所有 PNG 圖片的檔案名稱
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

    # 使用 tqdm 顯示進度
    for file_name in tqdm(png_files, desc="Processing images"):
        file_path = os.path.join(folder_path, file_name)
        
        # 打開圖片並轉換為 numpy 陣列
        with Image.open(file_path) as img:
            img = img.convert('L')  # 確保圖片是單通道（灰度圖）
            pixels = np.array(img)
            total_pixels += pixels.size
            
            # 計算每個像素值的出現次數
            unique, counts = np.unique(pixels, return_counts=True)
            for value, count in zip(unique, counts):
                pixel_count[value] += count

    # 計算各數字的出現次數與佔比
    pixel_stats = {k: {'count': v, 'ratio': v / total_pixels} for k, v in pixel_count.items()}

    return pixel_stats

def save_stats_to_csv(pixel_stats, output_file):
    # 將字典轉換為 DataFrame
    df = pd.DataFrame.from_dict(pixel_stats, orient='index')
    df.reset_index(inplace=True)
    df.columns = ['Pixel Value', 'Count', 'Ratio']
    
    # 儲存為 CSV
    df.to_csv(output_file, index=False)

def main():
    folder_path = 'VOCdevkit_foodseg103/VOC2007/SegmentationClass'  # 替換為你的資料夾路徑
    output_file = 'pixel_stats.csv'  # 替換為你想要儲存的檔案名
    
    pixel_stats = count_pixel_values(folder_path)
    
    # 儲存結果為 CSV
    save_stats_to_csv(pixel_stats, output_file)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
