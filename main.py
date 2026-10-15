import pandas as pd

df = pd.read_csv("wines_practice.csv")

df_clear = df.dropna(subset=["points", "price"]).copy()

def check_quality(df):
    if df["points"] >= 95:
        return 3
    elif df["points"] >= 85:
        return 2
    else:
        return 1

df_clear["stars"] = df_clear.apply(check_quality, axis=1)
df_clear["quality"] = round((df_clear["points"] / df_clear["price"]) * df_clear["stars"], 2)
df_clear = df_clear.sort_values(by="quality", ascending=False)

res = df_clear.head(50)
only_3_stars = res.loc[res["stars"] == 3]
best_countries = res.country.value_counts()

res.to_csv("best_wines.csv", index=False)
print("Guide worked:")
print()
print(f"Average price of all wines {df.price.mean():.2f}")
print(f"Average price of guide choice {res.price.mean():.2f}")
print()
print("Average points of all wines ", df.points.mean())
print("Average points of guide choice ", res.points.mean())
print()
print("3-stars wine count of guide choice ", len(only_3_stars))
print()
print("Best countries:")
for k,v in best_countries.head(3).items():
    print(f"{k} - {v}")