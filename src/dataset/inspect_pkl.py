import pickle

def inspect_detection():
    path = "data/raw_pkl/corpus_poses_fateme/CRDL_poses/2005/01_AVIGNON_2005_HISTOIRE_DES_LARMES_TIFF_detection_results.pkl"

    with open(path, "rb") as f:
        df = pickle.load(f)

    sample = df.iloc[0]

    print("TYPE:", type(sample["detection_output"]))
    print("\nCONTENT:")
    print(sample["detection_output"])


if __name__ == "__main__":
    inspect_detection()