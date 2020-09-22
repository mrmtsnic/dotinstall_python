# イテレータ

# scores = [40, 50, 70, 90, 60]
# it = iter(scores)  # リストをイテレータに変換
# print(next(it))
# print(next(it))
# print("hello")
# print(next(it))  # nextで次の要素取得 間に別の処理を挟んでも影響なし

def get_infinite():  # ジェネレータ
    i = 0
    while True:
        yield i * 2
        i += 1


g = get_infinite()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
