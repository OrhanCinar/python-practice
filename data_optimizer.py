import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error(line, data):
    """ Compute error between given line model and observed  data

    Parameters
    --------
    line : tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    data : 2D array where each row is a point (x,y)
    """
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err
