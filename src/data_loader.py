import pandas as pd
from pathlib import Path

DATA_PATH = Path("../data/raw")

def load_train_data():
    """Load training dataset"""
    return pd.read_csv(DATA_PATH / "train.csv")


def load_test_data():
    """Load test dataset"""
    return pd.read_csv(DATA_PATH / "test.csv")