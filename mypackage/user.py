# モジュール
# モジュールを入れるフォルダをパッケージという

class User:
    # クラス変数
    count = 0

    def __init__(self, name):
        # インスタンス変数
        self.name = name

    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))

    # クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))


class AdminUser(User):  # 継承元を()に入れる
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # インスタンスメソッド
    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))

    # override
    def say_hi(self):
        print("[admin] hi {0}".format(self.name))
