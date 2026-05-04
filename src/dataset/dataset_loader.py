import pickle
import numpy as np

class HPEDataset:
    def __init__(self, path):
        self.path = path
        self.data = self._load()

    def _load(self):
        with open(self.path, "rb") as f:
            raw = pickle.load(f)

        # TODO: adapt based on your real PKL structure
        return {
            "keypoints_2d": np.array(raw["kpts_2d"]),
            "keypoints_3d": np.array(raw["kpts_3d"]),
            "bbox": np.array(raw["bbox"]),
        }

    def __len__(self):
        return len(self.data["keypoints_2d"])

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.data.items()}
    