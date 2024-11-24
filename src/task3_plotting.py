import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_1d(data):
    plt.plot(data)
    plt.title("1D Line Plot")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

def plot_2d(x, y):

    plt.scatter(x, y, color='green')
    plt.title("2D Scatter Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def plot_3d(x, y, z):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='red')
    ax.set_title("3D Scatter Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plot_1d(x)  # 1D Line Plot
plot_2d(x, y)  # 2D Scatter Plot
plot_3d(x, y, z)  # 3D Scatter Plot
