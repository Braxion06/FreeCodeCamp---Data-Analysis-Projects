import numpy as np


def calculate (list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        return
    flatarray = np.array(list)
    gridarray = flatarray.reshape((3,3))
    calculations = {
        'mean': [np.mean(gridarray, axis=0), np.mean(gridarray, axis=1), np.mean(gridarray)], 
        'variance': [np.var(gridarray, axis=0), np.var(gridarray, axis=1), np.var(gridarray)], 
        'standard deviation': [np.std(gridarray, axis=0), np.std(gridarray, axis=1), np.std(gridarray)], 
        'max': [np.max(gridarray, axis=0), np.max(gridarray, axis=1), np.max(gridarray)],
        'min': [np.min(gridarray, axis=0), np.min(gridarray, axis=1), np.min(gridarray)],
        'sum': [np.sum(gridarray, axis=0), np.sum(gridarray, axis=1), np.sum(gridarray)]
        
    }
    print(calculations)
    return calculations