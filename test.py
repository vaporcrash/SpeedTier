import polars as pl


df = pl.read_csv("pokemon_champions_base_stats.csv")
print(df.filter(pl.col("name") == "Charizard").to_dicts()[0]["bst"])