from dataguard.core.rules import apply_rules


def run_engine(df, profile_results):
    results = []

    dup_count = df.is_duplicated().sum()

    for row in profile_results:
        issues, suggestions, score = apply_rules(df, row)

        # Duplicate rows (only once logically)
        if dup_count > 0:
            issues.append(f"🟠 {dup_count} duplicate rows")
            suggestions.append("Remove duplicates")
            score += 2

        if not issues:
            issues.append("🟢 Clean")
            suggestions.append("No action needed")

        new_row = row.copy()
        new_row["issue"] = ", ".join(issues)
        new_row["suggestion"] = ", ".join(suggestions)
        new_row["severity_score"] = score

        results.append(new_row)

    return results