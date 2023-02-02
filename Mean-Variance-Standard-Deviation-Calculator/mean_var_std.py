import numpy as np


def calculate (list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        return
    gridarray = np.array(list).reshape((3,3))
    calculations = {
        'mean': [np.mean(gridarray, axis=0).tolist(), np.mean(gridarray, axis=1).tolist(), np.mean(gridarray).tolist()], 
        'variance': [np.var(gridarray, axis=0).tolist(), np.var(gridarray, axis=1).tolist(), np.var(gridarray).tolist()], 
        'standard deviation': [np.std(gridarray, axis=0).tolist(), np.std(gridarray, axis=1).tolist(), np.std(gridarray).tolist()], 
        'max': [np.max(gridarray, axis=0).tolist(), np.max(gridarray, axis=1).tolist(), np.max(gridarray).tolist()],
        'min': [np.min(gridarray, axis=0).tolist(), np.min(gridarray, axis=1).tolist(), np.min(gridarray).tolist()],
        'sum': [np.sum(gridarray, axis=0).tolist(), np.sum(gridarray, axis=1).tolist(), np.sum(gridarray).tolist()]
        }
    print(calculations)
    return calculations