# 例外処理

class MyException(Exception):
    pass


def div(a, b):
    try:
        if (b < 0):
            raise MyException("not minus")
        print(a / b)
    except ZeroDivisionError:
        print("not by zero")
    except MyException as e:
        print(e)
    else:
        print("no exception")
    finally:
        print("--end--")


div(1, 0)
div(2, -1)
