import pandas as pd
import numpy as np

alpha = list("abcdefghijklmnopqrstuv")
numeric = list("0123456789")

def random_password(size=6):
    res = np.random.random(size=size)
    # 50% alpha, 50% numeric
    res = [np.random.choice(alpha) if val > 0.5 else np.random.choice(numeric) for val in res]
    # to str
    res = "".join(res)
    return res

def random_str(size=6):
    res = np.random.choice(alpha, size=size)
    res = "".join(res)
    return res