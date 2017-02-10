import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %matplotlib inline

survey_df = pd.read_csv('2016-FCC-New-Coders-Survey-Data.csv', low_memory=False)


'''性別のデータ'''
sns.countplot('Gender', data=survey_df)
# plt.show()


'''子供の有無'''
sns.countplot('HasChildren', data=survey_df)
# plt.show()


'''年齢'''
sns.kdeplot(survey_df['Age'])
# plt.show()


'''学習時間'''
sns.kdeplot(survey_df['HoursLearning'])
# plt.show()
