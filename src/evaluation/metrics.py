import numpy as np

def mpjpe(pred, gt):
    return np.mean(np.linalg.norm(pred - gt, axis=-1))