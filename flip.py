from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def flip_image(image_path):
    # 1. 读取图片
    original_img = Image.open(image_path)
    
    # 2. 左右翻转
    flipped_img = ImageOps.mirror(original_img)
    
    # 3. 在屏幕上显示
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_img)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title("Flipped Image")
    plt.imshow(flipped_img)
    plt.axis('off')
    
    plt.show()
    
    return flipped_img

if __name__ == "__main__":
    flip_image('C：\Users\杨欣妍\Desktop\test.jpg')