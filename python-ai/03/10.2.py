import numpy as np

# 模拟一个包含缺失值的数据集
np.random.seed(42)
data = np.random.randn(100, 5)
# 人为制造一些缺失值
mask = np.random.random((100, 5)) < 0.1
data[mask] = np.nan

print("原始数据统计:")
print("形状:", data.shape)
print("缺失值数量:", np.sum(np.isnan(data)))

# 处理缺失值：用列均值填充
def fill_missing_values(data):
    col_mean = np.nanmean(data, axis=0)
    inds = np.where(np.isnan(data))
    data[inds] = np.take(col_mean, inds[1])
    return data

filled_data = fill_missing_values(data.copy())
print("填充后缺失值数量:", np.sum(np.isnan(filled_data)))

# 标准化数据（Z-score标准化）
def standardize(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean) / std

standardized = standardize(filled_data)
print("标准化后的数据统计:")
print("均值（接近0）:", np.mean(standardized, axis=0))
print("标准差（接近1）:", np.std(standardized, axis=0))