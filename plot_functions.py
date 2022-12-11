import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def polutionHistogram(classmethod):
    plt.hist(classmethod, 
    weights=np.ones(len(classmethod)) / len(classmethod))
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()
    return