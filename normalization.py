import numpy as np

norm_fact = {
    'int16': (2**15)-1,
    'int32': (2**31)-1,
    'int64': (2**63)-1,
    'float32': 1.0,
    'float64': 1.0}


def norm(x):
    return np.float32(x) / norm_fact[x.dtype.name]
