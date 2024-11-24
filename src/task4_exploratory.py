import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    desc_stats = df.describe().T  # Transpose to make it more readable
    desc_stats['range'] = desc_stats['max'] - desc_stats['min']
    desc_stats['median'] = df.median()
    desc_stats['mode'] = df.mode().iloc[0]
    
    print("Descriptive Statistics:")
    print(desc_stats)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df)
    plt.title('Box Plot for Outlier Detection')
    plt.show()
    
    corr_matrix = df.corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    plt.title('Correlation Heatmap')
    plt.show()


df = pd.DataFrame({
    'A': np.random.rand(50),
    'B': np.random.rand(50) * 10,
    'C': np.random.rand(50) * 100
})

perform_eda(df)
