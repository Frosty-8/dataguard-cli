import polars as pl


def apply_fixes(df, results):
    df_clean = df.clone()
    changes = []

    columns_to_drop = []
    remove_duplicates = False

    for row in results:
        col = row["column"]

        # Missing values handling
        if "High missing values" in row["issue"] or "Some missing values" in row["issue"]:
            if df_clean[col].dtype in [pl.Int64, pl.Float64]:
                median = df_clean[col].median()

                df_clean = df_clean.with_columns(
                    df_clean[col].fill_null(median).alias(col)
                )
                changes.append(f"{col}: filled nulls with median")

            else:
                mode_df = df_clean[col].mode()

                if len(mode_df) > 0:
                    mode_val = mode_df[0, 0]

                    df_clean = df_clean.with_columns(
                        df_clean[col].fill_null(mode_val).alias(col)
                    )
                    changes.append(f"{col}: filled nulls with mode")

        # Mark constant columns for removal
        if "Constant column" in row["issue"]:
            columns_to_drop.append(col)

        # Mark duplicates removal
        if "duplicate" in row["issue"].lower():
            remove_duplicates = True

    # Apply column drops
    if columns_to_drop:
        df_clean = df_clean.drop(columns_to_drop)
        for col in columns_to_drop:
            changes.append(f"{col}: dropped constant column")

    # Apply duplicate removal once
    if remove_duplicates:
        df_clean = df_clean.unique()
        changes.append("Removed duplicate rows")

    return df_clean, changes