import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load():
    col = ["Class", "Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium",
    "Total phenols", "Flavanoids", "Nonflavanoid phenols", "Proanthocyanins",
    "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
    df = pd.read_csv('data/wine.data', header=None)
    df.columns = col
    return df

def summary_statistics(df):
    summary = df.describe()
    summary.to_csv('results/summary_statistics.csv')

def corr_analysis(df):
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix of Wine Variables")
    plt.savefig('results/correlation_matrix.png')

def visualizations(df):
    plt.figure(figsize=(10, 6))
    df['Alcohol'].hist(bins=20)
    plt.title('Alcohol Content Distribution')
    plt.xlabel('Alcohol')
    plt.ylabel('Frequency')
    plt.savefig('results/alcohol_distribution.png')

def main():
    df = load()
    summary_statistics(df)
    corr_analysis(df)
    visualizations(df)

if __name__ == "__main__":
    main()
