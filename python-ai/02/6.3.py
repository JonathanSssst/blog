# finally子句
try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    try:
        f.close()
    except:
        pass