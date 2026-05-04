from pathlib import Path

folders = [
    "data/raw_pkl",
    "data/processed",
    "models",
    "evaluation",
    "src/dataset",
    "src/models",
    "src/training",
    "src/utils",
    ".devcontainer"
]

for f in folders:
    Path(f).mkdir(parents=True, exist_ok=True)

print("HPE structure ready")
