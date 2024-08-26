from PIL import Image, ImageDraw, ImageFont

def process_image(img, class_nums, class_names, colors, max_width=600, output_size=(800, 600)):
    # 打開圖片
    img = img
    
    # 計算新的尺寸保持原比例
    aspect_ratio = img.height / img.width
    new_width = min(max_width, img.width)
    new_height = int(new_width * aspect_ratio)
    
    # 縮小圖片
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    
    # 創建一個固定大小的全白圖片
    new_img = Image.new('RGB', output_size, (255, 255, 255))
    
    # 計算圖片的位置，使其位於新圖片的左側
    img_x = 20  # 固定的左邊距
    img_y = (output_size[1] - new_height) // 2  # 垂直居中
    
    # 將縮小的圖片粘貼到新圖片上
    new_img.paste(img, (img_x, img_y))
    
    # 繪製色塊和class_name
    draw = ImageDraw.Draw(new_img)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    
    # 色塊的寬高
    block_width = 30
    block_height = 30
    text_x = img_x + new_width + 20  # 色塊和文字的起始x位置
    text_y = 20  # 第一個色塊和文字的起始y位置
    spacing = 10  # 色塊和文字之間的間距
    class_show_index = 0
    for i, class_num in enumerate(class_nums):
        if class_num > 0:

            color = colors[i % len(colors)]
            block_y = text_y + (block_height + spacing) * class_show_index  # 每個色塊和文字的y位置
            class_show_index+=1
            # 繪製色塊
            draw.rectangle([(text_x, block_y), (text_x + block_width, block_y + block_height)], fill=color)
            
            # 繪製文字
            draw.text((text_x + block_width + 10, block_y + 5), class_names[i], fill=(0, 0, 0), font=font)
    
    return new_img

# 測試函數
image_path = 'Image_7_beef.png'  # 原始圖片路徑
img = Image.open(image_path)
output_path = 'output_image.jpg'       # 輸出圖片路徑

class_nums = [0, 3, 0, 1, 5]  # 假設的class_nums數組
class_names = ['Class1', 'Class2', 'Class3', 'Class4', 'Class5']  # 假設的class_names數組
colors = [
    (0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128), 
    (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0), (192, 128, 0), 
    (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128), (0, 64, 0), (128, 64, 0), 
    (0, 192, 0), (128, 192, 0), (0, 64, 128), (128, 64, 12)
]

returnImage = process_image(img, class_nums, class_names, colors)

returnImage.save(output_path)
