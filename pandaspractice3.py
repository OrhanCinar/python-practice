import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/Minimum Wage Data.csv", encoding="latin")


gb = df.groupby("State")

gb.get_group("Alabama").set_index("Year")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name})
    else:
        act_min_wage = act_min_wage.join(group.set_index(
            "Year")[["Low.2018"]].rename(columns={"Low.2018": name}))


# print(act_min_wage.corr().head())

issue_df = df[df["Low.2018"] == 0]

min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

# for problem in issue_df["State"].unique():
#     if problem in min_wage_corr.columns:
#         print("Missing")

labels = [c[:2] for c in min_wage_corr.columns]

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111)
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))
ax.set_yticklabels(labels)
ax.set_xticklabels(labels)
plt.show()
