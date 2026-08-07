import pandas as pd

print("二次元データ DataFrame\n")

df = pd.DataFrame({
    "Name": ["Takeshi", "Bob", "Tom","Hanako","Takuya","John"],
    "Age": [25, 30, 35, 30, 25, 35],
    "City": ["Tokyo", "Osaka", "Nagoya","Kanagawa","Saitama","Tokyo"]
})

print(df)

#nameの列を取得

print("\nNameの列を取得")

print(df["Name"])

#Ageの列を取得

print("\nAgeの列を取得")

print(df["Age"])

#Cityの列を取得

print("\nCityの列を取得")

print(df["City"])

#0行目を取得

print("\n0番目の行を取得")

print(df[0:1])

#0~1行目を取得

print("\n0~1番目の行を取得")

print(df[0:2])

#1行目を取得

print("\n1番目の行を取得")

print(df[1:2])

#head()で先頭の5行を取得

print("\nhead()で先頭の5行を取得")

print(df.head())

#tail()で後ろの5行を取得

print("\ntailで後ろの5行を取得")

print(df.tail())

#query()を使って条件を満たす列を取得

print("\nquery()を使って条件を満たす列を取得 (Ageが30以上の人)")

print(df.query('Age >= 30'))