import numpy as np

true_cookies = np.array([14, 14, 13, 14, 12, 14, 13, 14, 14, 13, 12, 11, 13, 11, 13, 10, 11,
       10, 12, 14, 11, 14, 11, 12, 13, 14, 12, 12, 12, 13, 12, 12, 10, 12,
       10, 14, 14, 10, 10, 13, 14, 14, 12, 12, 10, 12, 10, 12, 10, 12, 11,
       13, 10, 14, 10, 12, 14, 13, 12, 10, 13, 14, 12, 12, 11, 12, 13, 11,
       14, 11, 13, 14, 12, 13, 11, 14, 10, 13, 14, 11, 11, 11, 13, 14, 13,
       12, 10, 14, 13, 12, 11, 14, 10, 11, 12, 14, 13, 10, 12, 10])

def diff(current_values):
    if current_values.shape[0] != 100:
        print('error! loss function need number of cookies per box, which requires a numpy array of length 100')

    noise = np.random.normal(0, 2.5, 100)
    
    diff = np.sum(np.square(current_values - true_cookies + noise))
    
    return diff