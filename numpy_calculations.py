import numpy as np

def revenue_statistics(df):
    revenue = df["Revenue"].values
    return {
        "mean": np.mean(revenue),
        "median": np.median(revenue),
        "std_dev": np.std(revenue),
        "max": np.max(revenue)
    }
