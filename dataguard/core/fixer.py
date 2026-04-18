import polars as pl

def apply_fixes(df, results):
    df_clean = df.clone()
    changes = []

    columns_to_drop = []
    remove_duplicates = False

    for row in results:
        col = row["column"]
        issue_text = row["issue"].lower()

        series = df_clean[col]

        # -------------------------------
        # Missing values handling
        # -------------------------------
        if "missing values" in issue_text:

            # Numeric → median
            if series.dtype in [pl.Int64, pl.Float64]:
                median_val = series.median()

                if median_val is not None:
                    df_clean = df_clean.with_columns(
                        series.fill_null(median_val).alias(col)
                    )
                    changes.append(f"{col}: filled nulls with median")

            # String → mode
            else:
                mode_result = series.mode()

                if isinstance(mode_result, pl.DataFrame):
                    if mode_result.height == 0:
                        continue
                    mode_val = mode_result.to_series()[0]

                elif isinstance(mode_result, pl.Series):
                    if len(mode_result) == 0:
                        continue
                    mode_val = mode_result[0]

                else:
                    continue

                df_clean = df_clean.with_columns(
                    series.fill_null(mode_val).alias(col)
                )
                changes.append(f"{col}: filled nulls with mode")

        # -------------------------------
        # Constant column
        # -------------------------------
        if "constant column" in issue_text:
            columns_to_drop.append(col)

        # -------------------------------
        # Duplicate detection
        # -------------------------------
        if "duplicate" in issue_text:
            remove_duplicates = True

    # Drop columns
    if columns_to_drop:
        df_clean = df_clean.drop(columns_to_drop)
        for col in columns_to_drop:
            changes.append(f"{col}: dropped constant column")

    # Remove duplicates
    if remove_duplicates:
        before = df_clean.height
        df_clean = df_clean.unique()
        removed = before - df_clean.height

        if removed > 0:
            changes.append(f"Removed {removed} duplicate rows")

    return df_clean, changes