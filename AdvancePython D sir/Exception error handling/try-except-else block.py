# 08 / 04 / 2025

# try-except-else block
# else block is executed only when there is no exception inside try block

try:
    print("try block")
    print(10/0)
except ZeroDivisionError as msg :
    print(msg)
else: print('else block')