import os, sys
import numpy as np
from datetime import datetime

def get_rng(obj=None):
    """ obj: some object to use to generate random seed"""
    seed = (id(obj) + os.getpid() +
            int(datetime.now().strftime("%Y%m%d%H%M%S%f"))) % 4294967295
    return np.random.RandomState(seed)
