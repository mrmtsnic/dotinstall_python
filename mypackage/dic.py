# 辞書型

sales = {"taguchi": 200, "fkoji": 400}
# print(sales["taguchi"])
# sales["taguchi"] = 300
# sales["dotinstall"] = 500  # 追加
# del (sales["fkoji"])  # 削除
# print(sales)


# 辞書のループ
for key, value in sales.items():
    print("{0}: {1}".format(key, value))
