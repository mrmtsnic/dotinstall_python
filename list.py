# リスト型

scores = [40, 50]
print(scores[0])

# 要素の個数取得
print(len(scores))

# 要素追加
scores.append(100)

print(scores)


for score in scores:
    print(score)

# 要素のインデックスも取得
for i, score in enumerate(scores):
    print("{0}:{1}".format(i, score))
