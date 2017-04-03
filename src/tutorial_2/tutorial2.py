import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC

df = pd.read_csv("train.csv").replace("male", 0).replace("female", 1)
df["Age"].fillna(df.Age.mean(), inplace=True)


split_data = []
for survived in [0,1]:
    split_data.append(df[df.Survived==survived])

# 客室グレードごとのヒストグラム
temp = [i["Pclass"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=3)

# 年齢ごとのヒストグラム
temp = [i["Age"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=16)

# 性別ごとのヒストグラム
temp = [i["Sex"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=2)

# データの成形
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df2 = df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare",
               "Cabin", "Embarked"], axis=1)


train_data = df2.values
xs = train_data[:, 2:]  # Pclass以降の変数
y = train_data[:, 1]  # 正解データ


# model = LogisticRegression() # ロジスティック回帰
model = RandomForestClassifier(n_estimators=1000) # ランダムフォレスト
# model = Perceptron() # パーセプトロン
# model = SVC() # サポートベクターマシン


# 学習
model.fit(xs, y)

# テストデータの読み込み
test_df = pd.read_csv("test.csv").replace("male", 0).replace("female", 1)

# 欠損値の補完
test_df["Age"].fillna(df.Age.median(), inplace=True)
test_df["FamilySize"] = test_df["SibSp"] + test_df["Parch"] + 1
test_df2 = test_df.drop(["Name", "SibSp", "Parch", "Ticket",
                         "Fare", "Cabin", "Embarked"], axis=1)

test_data = test_df2.values
xs_test = test_data[:, 1:]
output = model.predict(xs_test)

zip_date = zip(test_data[:, 0].astype(int), output.astype(int))

predict_date = list(zip_date)

# 結果をCSVで保存
with open("predict_date.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), output.astype(int)):
        writer.writerow([pid, survived])
