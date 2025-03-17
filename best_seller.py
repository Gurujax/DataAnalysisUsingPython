import pandas as pd

df = pd.read_csv(r"C:\Users\User\Desktop\bestsellers.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"]= df["Price"].astype(float)
author_counts = df["Author"].value_counts()
print(author_counts)

average_rating_by_genre=df.groupby("Genre")["Rating"].mean()
print(average_rating_by_genre)

author_counts.head(10).to_csv("Top_authors.csv")
average_rating_by_genre.to_csv("avg_rating_by_genre.csv")


