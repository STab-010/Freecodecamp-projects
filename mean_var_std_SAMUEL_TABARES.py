import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    fixed = np.array(list).reshape(3,3)

    calculation = {

        'mean' : [np.mean(fixed, axis = 0).tolist(), np.mean(fixed, axis = 1).tolist(), np.mean(fixed)],
        'variance': [np.var(fixed, axis = 0).tolist(), np.var(fixed, axis = 1).tolist(), np.var(fixed)],
        'standard deviation' : [np.std(fixed, axis = 0).tolist(), np.std(fixed, axis = 1).tolist(), np.std(fixed)],
        'max': [np.max(fixed, axis = 0).tolist(), np.max(fixed, axis = 1).tolist(), np.max(fixed)],
        'min': [np.min(fixed, axis = 0).tolist(), np.min(fixed, axis = 1).tolist(), np.min(fixed)],
        'sum': [np.sum(fixed, axis = 0).tolist(), np.sum(fixed, axis = 1).tolist(), np.sum(fixed)]

    }

    return calculation

calculate([0,1,2,3,4,5,6,7,8])