import polars as pl
from dataguard.profiler import profile_data
from dataguard.detector import detect_issues

def test_null_detection():
    df = pl.DataFrame({
        "age": [None, None, 10, 20]
    })

    profile = profile_data(df)
    result = detect_issues(df, profile)

    assert result[0]["severity_score"] > 0


def test_constant_column():
    df = pl.DataFrame({
        "x": [1, 1, 1, 1]
    })

    profile = profile_data(df)
    result = detect_issues(df, profile)

    assert "Constant column" in result[0]["issue"]

def test_duplicate_detection():
    import polars as pl
    from dataguard.profiler import profile_data
    from dataguard.detector import detect_issues

    df = pl.DataFrame({
        "a": [1, 1, 2, 2]
    })

    profile = profile_data(df)
    result = detect_issues(df, profile)

    assert any("duplicate" in r["issue"].lower() for r in result)

def test_quality_score():
    from dataguard.utils import compute_quality_score

    results = [
        {"severity_score": 3},
        {"severity_score": 1},
        {"severity_score": 0},
    ]

    score = compute_quality_score(results)

    assert score < 100