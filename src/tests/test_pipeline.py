import os 
from src.dataset.loader import HPEDataset
from src.adapters.model_a_adapter import ModelAAdapter

BASE = "data/raw_pkl/corpus_poses_fateme/CRDL_poses/2005"

file = os.path.join(
    BASE,
    "01_AVIGNON_2005_HISTOIRE_DES_LARMES_TIFF_detection_results.pkl"
)

adapter = ModelAAdapter(dataset)

sample = dataset[0]
model_input = adapter.transform(sample)

print("Pipeline works:", model_input.keys())