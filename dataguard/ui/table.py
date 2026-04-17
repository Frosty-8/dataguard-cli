from rich.table import Table

def build_table(results):
    table = Table(title="📊 Data Quality Report", row_styles=["none", "dim"])

    table.add_column("Column", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Null %", justify="right")
    table.add_column("Unique", justify="right")
    table.add_column("Severity", justify="center")
    table.add_column("Issues", style="red", overflow="fold")
    table.add_column("Suggestion", style="green", overflow="fold")

    for r in results:
        table.add_row(
            r["column"],
            r["dtype"],
            f"{r['null_pct']}%",
            str(r["unique_count"]),
            str(r["severity_score"]),
            r["issue"],
            r["suggestion"]
        )

    return table