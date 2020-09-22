# クラス
# 関数
# アクセス制限
# クラス継承
# モジュール 別ファイルのコード

# import user
# from user import AdminUser, User

# package
# import mypackage.user as mymodule  # asで名前をつけられる
from mypackage.user import AdminUser

bob = AdminUser("bob", 23)
print(bob.name)
bob.say_hi()
bob.say_hello()
