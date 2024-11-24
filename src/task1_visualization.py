import matplotlib.pyplot as plt
import numpy as np
import collections

def plot_distribution(data):
    counter = collections.Counter(data)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(counter.keys(), counter.values(), color=['blue', 'green', 'orange'])
    
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Category Frequency Distribution')
    
    plt.show()

    return fig


data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)