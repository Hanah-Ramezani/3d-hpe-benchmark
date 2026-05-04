import pickle
from pathlib import Path

def inspect_detection():
    path = "data/raw_pkl/corpus_poses_fateme/CRDL_poses/2005/01_AVIGNON_2005_HISTOIRE_DES_LARMES_TIFF_detection_results.pkl"

    with open(path, "rb") as f:
        df = pickle.load(f)

    sample = df.iloc[0]

    print("TYPE:", type(sample["detection_output"]))
    print("\nCONTENT:")
    print(sample["detection_output"])
    print(sample.keys())

    keys_set = set()

    for i in range(min(200, len(df))):
        sample = df["detection_output"].iloc[i]
        if isinstance(sample, dict):
            keys_set.update(sample.keys())

    print("\nUNIQUE KEYS:", keys_set)

    # ---- export ----
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    output_path = out_dir / "detection_results.xlsx"
    df.to_excel(output_path, index=False)

    print("\nSaved to:", output_path)


if __name__ == "__main__":
    inspect_detection()