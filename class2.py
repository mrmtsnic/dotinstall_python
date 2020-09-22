# クラスの多重継承
# A,B -> C
# 継承元のクラスに同じメソッドがあった場合は先に継承したクラスのメソッドが実行される

class A:
    def say_a(self):
        print("A")

    def say_hi(self):
        print("hi from A")


class B:
    def say_b(self):
        print("B")

    def say_hi(self):
        print("hi from B")


class C(A, B):
    pass


c = C()
c.say_a()
c.say_b()
c.say_hi()
