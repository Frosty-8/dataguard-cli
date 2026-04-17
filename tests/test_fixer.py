import polars as pl
from dataguard.core.fixer import apply_fixes

def test_fix_nulls():
    df = pl.DataFrame({
        "a": [1, None, 3]
    })

    results = [{
        "column": "a",
        "issue": "High missing values"
    }]

    df_clean, changes = apply_fixes(df, results)

    assert df_clean["a"].null_count() == 0


def test_drop_constant():
    df = pl.DataFrame({
        "x": [1, 1, 1]
    })

    results = [{
        "column": "x",
        "issue": "Constant column"
    }]

    df_clean, changes = apply_fixes(df, results)

    assert "x" not in df_clean.columns