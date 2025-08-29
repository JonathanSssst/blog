# 写入文件
with open("data.txt", "w") as f:
    f.write("Hello, AI World!\n")
    f.write("This is a test file.\n")

# 读取文件
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# 逐行读取文件
with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 读取CSV文件（手动方式）
with open("data.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")
    data = []
    for line in lines[1:]:
        row = line.strip().split(",")
        data.append(row)
    print(header)
    print(data)