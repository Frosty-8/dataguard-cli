import polars as pl
from pathlib import Path


def load_data(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    if path.suffix == ".csv":
        return pl.read_csv(path)
    elif path.suffix == ".json":
        return pl.read_json(path)
    else:
        raise ValueError("Unsupported file format")