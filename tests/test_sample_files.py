import polars as pl
from pathlib import Path

from dataguard.loader import load_data
from dataguard.profiler import profile_data
from dataguard.detector import detect_issues


def test_sample_csv_pipeline():
    file_path = Path("examples/sample.csv")

    df = load_data(str(file_path))

    assert isinstance(df, pl.DataFrame)
    assert df.height > 0
    assert len(df.columns) > 0

    profile = profile_data(df)
    results = detect_issues(df, profile)

    assert isinstance(results, list)
    assert len(results) == len(df.columns)

    for row in results:
        assert "column" in row
        assert "issue" in row
        assert "suggestion" in row
        assert "severity_score" in row