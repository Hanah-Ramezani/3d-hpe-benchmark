from pathlib import Path

folders = [
    "data/raw_pkl",
    "data/processed",
    "evaluation",
    "models"
]

for f in folders:
    Path(f).mkdir(parents=True, exist_ok=True)

print("Done")