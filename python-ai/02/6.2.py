# 捕获多个异常
try:
    x = int("abc")
    y = 10 / x
except ValueError:
    print("Invalid integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception as e:
    print(f"An error occurred: {e}")