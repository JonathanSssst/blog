import numpy as np

# 模拟一张3x3的RGB图像
image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                  [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
                  [[128, 128, 128], [64, 192, 32], [192, 64, 160]]])

print("图像形状:", image.shape)  # (3, 3, 3)
print("图像数据类型:", image.dtype)

# 转换为灰度图像（简单的加权平均法）
def rgb_to_grayscale(rgb_image):
    weights = np.array([0.299, 0.587, 0.114])
    return np.dot(rgb_image, weights)

grayscale = rgb_to_grayscale(image)
print("灰度图像:\n", grayscale)

# 图像归一化（0-1之间）
normalized = image / 255.0
print("归一化后的图像:\n", normalized)

# 图像翻转
flipped_h = np.flip(image, axis=0)  # 水平翻转
flipped_v = np.flip(image, axis=1)  # 垂直翻转