def profile_data(df):
    results = []
    total_rows = df.height

    for col in df.columns:
        series = df[col]

        null_count = series.null_count()
        null_pct = (null_count / total_rows) * 100
        unique_count = series.n_unique()

        results.append({
            "column": col,
            "dtype": str(series.dtype),
            "null_pct": round(null_pct, 2),
            "unique_count": unique_count,
        })

    return results