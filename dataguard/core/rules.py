import re
import polars as pl
from dataguard.config import load_config

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def apply_rules(df, row, config=None):
    if config is None:
        config = load_config()

    issues = []
    suggestions = []
    score = 0

    col = row["column"]
    series = df[col]

    # Missing values
    if row["null_pct"] > config["null_thresholds"]["critical"]:
        issues.append("🔴 High missing values")
        suggestions.append("Fill median or drop")
        score += 3
    elif row["null_pct"] > config["null_thresholds"]["warning"]:
        issues.append("🟠 Some missing values")
        suggestions.append("Impute values")
        score += 1

    # Constant column
    if config.get("constant_column", True) and row["unique_count"] == 1:
        issues.append("🟡 Constant column")
        suggestions.append("Consider dropping")
        score += 1

    # Email validation
    if (
        config.get("email_validation", True)
        and "email" in col.lower()
        and series.dtype == pl.Utf8
    ):
        valid_series = series.drop_nulls()
        invalid = valid_series.filter(~valid_series.str.contains(EMAIL_REGEX))

        if len(invalid) > 0:
            issues.append("🟠 Invalid email format")
            suggestions.append("Apply regex cleaning")
            score += 2

    return issues, suggestions, score