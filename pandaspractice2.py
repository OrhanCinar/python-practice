import pandas as pd

df = pd.read_csv("data/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
albany_df = df[df["region"] == "Albany"]

albany_df.set_index("Date", inplace=True)
albany_df.sort_index(inplace=True)
# albany_df["AveragePrice"].rolling(25).mean()
print(albany_df["region"].unique())

for region in df["region"].unique():
    print(region)
