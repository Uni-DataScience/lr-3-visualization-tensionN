import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def create_scatter_plot(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='x', y='y', data=data, ax=ax, color='blue')

    ax.set_title('Scatter Plot of x vs. y', fontsize=14)
    ax.set_xlabel('X Variable', fontsize=12)
    ax.set_ylabel('Y Variable', fontsize=12)

    plt.show()

    return fig

data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

create_scatter_plot(data)
