import os
"""
該程式是用來比對不同資料夾是否檔名都有批配

"""
def get_file_names(folder):
    files = [file.split('.')[0] for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    return set(files)

def compare_folders(folder1, folder2):
    files1 = get_file_names(folder1)
    files2 = get_file_names(folder2)

    missing_in_folder1 = files2 - files1
    missing_in_folder2 = files1 - files2

    if missing_in_folder1:
        print(f"檔案夾 {folder1} 中缺失的檔案名稱:")
        for file in missing_in_folder1:
            print(file)

    if missing_in_folder2:
        print(f"檔案夾 {folder2} 中缺失的檔案名稱:")
        for file in missing_in_folder2:
            print(file)

# 指定兩個要比對的資料夾路徑
folder_path1 = 'VOCdevkit_2024_1/VOC2007/JPEGImages'
folder_path2 = 'VOCdevkit_2024_1/VOC2007/SegmentationClass'

compare_folders(folder_path1, folder_path2)