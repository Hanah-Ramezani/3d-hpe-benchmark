import numpy as np

class ModelAAdapter:

    def __init__(self, dataset):
        self.dataset = dataset

    def transform(self, sample):
        
        det = sample["detection_output"]

        
        keypoints_2d = np.array(det["pred_keypoints_2d"])
        keypoints_3d = np.array(det["pred_keypoints_3d"])
        bbox = np.array(det["bbox"])
        focal_length = det.get("focal_length", None)


        keypoints_2d = self._normalize_2d(keypoints_2d, bbox)

        return {
            "input_2d": keypoints_2d,     # model input
            "input_3d": keypoints_3d,     # optional supervision
            "bbox": bbox,
            "focal_length": focal_length
        }

    def _normalize_2d(self, kpts, bbox):
        
        x1, y1, x2, y2 = bbox
        width = x2 - x1
        height = y2 - y1

        kpts = kpts.copy()
        kpts[:, 0] = (kpts[:, 0] - x1) / width
        kpts[:, 1] = (kpts[:, 1] - y1) / height

        return kpts