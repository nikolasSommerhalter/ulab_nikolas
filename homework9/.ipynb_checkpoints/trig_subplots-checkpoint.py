import matplotlib.pyplot as plt
import numpy as np 

def side_by_side_subplots(domain = [0,2*np.pi]):
    x_data = np.linspace(domain[0], domain[1], 1000)
    y_1 = np.cos(x_data)
    y_2 = np.sin(x_data)
    fig, ax = plt.subplots(1,2,figsize=(10,10))
    ax[0].plot(x_data, y_1)
    ax[1].plot(x_data, y_2)
    ax[0].set_title("f(x) = cos(x)")
    ax[1].set_title("g(x) = sin(x)")
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")
    ax[1].set_ylabel("y-axis")
    ax[1].set_xlabel("x-axis")
    plt.show()
    return

def vertical_subplots(domain = [0,2*np.pi]):
    x_data = np.linspace(domain[0], domain[1], 1000)
    y_1 = np.cos(x_data)
    y_2 = np.sin(x_data)
    fig, ax = plt.subplots(2,1,figsize=(10,10))
    ax[0].plot(x_data, y_1)
    ax[1].plot(x_data, y_2)
    ax[0].set_title("f(x) = cos(x)")
    ax[1].set_title("g(x) = sin(x)")
    ax[0].set_xlabel("X-axis")
    ax[0].set_ylabel("Y-axis")
    ax[1].set_ylabel("y-axis")
    ax[1].set_xlabel("x-axis")
    plt.show()
    return