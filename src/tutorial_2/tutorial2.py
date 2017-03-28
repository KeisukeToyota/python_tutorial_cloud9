import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("train.csv").replace("male", 0).replace("female", 1)
df["Age"].fillna(df.Age.median(), inplace=True)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df2 = df.drop(["Name", "SibSp", "Parch", "Ticket", "Fare",
               "Cabin", "Embarked"], axis=1)

train_data = df2.values
xs = train_data[:, 2:]  # Pclass以降の変数
y = train_data[:, 1]  # 正解データ

# forest = RandomForestClassifier(n_estimators=100)
#
# # 学習
# forest = forest.fit(xs, y)
logistic = LogisticRegression() # ロジスティック回帰
forest = RandomForestClassifier(n_estimators=1000) # ランダムフォレスト

logistic.fit(xs, y)
forest.fit(xs, y)

test_df = pd.read_csv("test.csv").replace("male", 0).replace("female", 1)

# 欠損値の補完
test_df["Age"].fillna(df.Age.median(), inplace=True)
test_df["FamilySize"] = test_df["SibSp"] + test_df["Parch"] + 1
test_df2 = test_df.drop(["Name", "SibSp", "Parch", "Ticket",
                         "Fare", "Cabin", "Embarked"], axis=1)

test_data = test_df2.values
xs_test = test_data[:, 1:]
logistic_output = logistic.predict(xs_test)
forest_output = forest.predict(xs_test)

logistic_zip_data = zip(test_data[:, 0].astype(int), logistic_output.astype(int))
forest_zip_date = zip(test_data[:, 0].astype(int), forest_output.astype(int))

logistic_predict_data = list(logistic_zip_data)
forest_predict_date = list(forest_zip_date)

with open("logistic_predict_data.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), logistic_output.astype(int)):
        writer.writerow([pid, survived])

with open("forest_predict_date.csv", "w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["PassengerId", "Survived"])
    for pid, survived in zip(test_data[:, 0].astype(int), forest_output.astype(int)):
        writer.writerow([pid, survived])
