import kagglehub
import os
import pandas as pd

def load_online_retail_data():
    path = kagglehub.dataset_download(
        "ulrikthygepedersen/online-retail-dataset"
    )
    csv_path = os.path.join(path, "online_retail.csv")
    df = pd.read_csv(csv_path)
    return df
