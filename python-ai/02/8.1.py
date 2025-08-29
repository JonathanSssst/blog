import os

def load_csv(file_path):
    """加载CSV文件"""
    # 检查文件是否存在，如果不存在则抛出异常
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # 使用with语句打开文件，这样可以确保文件在使用后被正确关闭
    with open(file_path, "r", encoding='utf-8') as f:
        # 读取文件的所有行
        lines = f.readlines()
        # 提取表头：第一行内容，去除两端空白字符，然后按逗号分割
        header = lines[0].strip().split(",")
        # 用于存储数据的列表
        data = []
        # 遍历除第一行外的所有行（数据行）
        for line in lines[1:]:
            # 去除行两端的空白字符，然后按逗号分割成列表
            row = line.strip().split(",")
            # 尝试将数值型数据转换为浮点数
            for i in range(len(row)):
                try:
                    row[i] = float(row[i])
                except ValueError:
                    # 如果无法转换为浮点数（如字符串），则保持原样
                    pass
            # 将处理后的行添加到数据列表中
            data.append(row)
    # 返回表头和数据
    return header, data

def save_csv(file_path, header, data):
    """保存数据到CSV文件"""
    # 使用with语句打开文件进行写入
    with open(file_path, "w", encoding='utf-8') as f:
        # 将表头用逗号连接并写入文件，最后添加换行符
        f.write(",".join(header) + "\n")
        # 遍历每一行数据
        for row in data:
            # 用于存储转换为字符串后的数据
            row_str = []
            # 遍历行中的每个元素
            for item in row:
                # 如果元素是浮点数，则转换为字符串
                if isinstance(item, float):
                    # 处理小数位数，避免科学计数法
                    if item.is_integer():
                        row_str.append(str(int(item)))
                    else:
                        row_str.append(str(item))
                # 否则（如字符串），保持原样
                else:
                    row_str.append(str(item))
            # 将转换后的行用逗号连接并写入文件，最后添加换行符
            f.write(",".join(row_str) + "\n")

def normalize_data(data, header, columns):
    """标准化数据"""
    # 找出指定列的最小值和最大值
    # 初始化最小值字典，默认值为正无穷大
    min_vals = {col: float('inf') for col in columns}
    # 初始化最大值字典，默认值为负无穷大
    max_vals = {col: float('-inf') for col in columns}

    # 遍历所有数据行，找出每列的最小值和最大值
    for row in data:
        for col in columns:
            # 获取列在数据中的索引位置
            col_index = header.index(col)
            # 确保该列的值是数值类型
            if isinstance(row[col_index], (int, float)):
                # 更新最小值
                if row[col_index] < min_vals[col]:
                    min_vals[col] = row[col_index]
                # 更新最大值
                if row[col_index] > max_vals[col]:
                    max_vals[col] = row[col_index]

    # 标准化数据（将数据缩放到[0, 1]范围内）
    normalized_data = []
    for row in data:
        # 创建当前行的副本，避免修改原始数据
        new_row = row.copy()
        # 对指定的每一列进行标准化
        for col in columns:
            # 获取列在数据中的索引位置
            col_index = header.index(col)
            # 确保该列的值是数值类型
            if isinstance(new_row[col_index], (int, float)):
                # 如果最大值和最小值相等（所有值都相同），则标准化为0
                if max_vals[col] - min_vals[col] == 0:
                    new_row[col_index] = 0.0
                # 否则，使用公式：(x - min) / (max - min) 进行标准化
                else:
                    new_row[col_index] = (row[col_index] - min_vals[col]) / (max_vals[col] - min_vals[col])
        # 将标准化后的行添加到结果列表中
        normalized_data.append(new_row)

    # 返回标准化后的数据
    return normalized_data

def get_numeric_columns(data, header):
    """获取数值型列名"""
    numeric_columns = []
    if data and header:
        for col in header:
            col_index = header.index(col)
            # 检查该列在第一行数据中的值是否为数值类型
            if col_index < len(data[0]) and isinstance(data[0][col_index], (int, float)):
                numeric_columns.append(col)
    return numeric_columns

def main():
    """主函数：演示数据预处理流程"""
    # 加载数据
    try:
        # 调用load_csv函数加载data.csv文件
        header, data = load_csv("data.csv")
        
        # 打印数据的基本信息
        print("=" * 50)
        print("数据加载成功！")
        print(f"Loaded data with {len(data)} rows and {len(header)} columns.")
        print(f"Header: {header}")
        print(f"First 3 rows:")
        for i, row in enumerate(data[:3], 1):
            print(f"  {i}: {row}")
        print()

        # 获取数值型列
        numeric_columns = get_numeric_columns(data, header)
        
        if numeric_columns:
            print(f"找到数值型列: {numeric_columns}")
            print()
            
            # 调用normalize_data函数对数值型列进行标准化
            normalized_data = normalize_data(data, header, numeric_columns)
            
            # 打印标准化后的前3行数据
            print("标准化后的前3行数据:")
            for i, row in enumerate(normalized_data[:3], 1):
                print(f"  {i}: {row}")
            print()
            
            # 保存标准化后的数据
            save_csv("normalized_data.csv", header, normalized_data)
            print("标准化后的数据已保存到 'normalized_data.csv'")
            print("数据预处理完成！")
        else:
            print("未找到数值型列进行标准化")
            
    # 捕获所有可能的异常并打印错误信息
    except Exception as e:
        print(f"发生错误: {e}")
        import traceback
        traceback.print_exc()

# 如果这个脚本是直接运行的（而不是被导入的），则执行main函数
if __name__ == "__main__":
    main()