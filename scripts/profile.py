import pandas as pd
from ydata_profiling import ProfileReport

col = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]

df = pd.read_csv('data/wine.data', header=None)
df.columns = col
profile = ProfileReport(df, title="Wine Profiling Report")
profile.to_file("profiling/report.html")

