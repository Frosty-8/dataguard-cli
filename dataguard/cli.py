import typer
from dataguard.ui.banner import show_banner
from dataguard.commands.scan import scan_command
from dataguard.commands.report import report_command
from dataguard.core.fixer import apply_fixes
from dataguard.loader import load_data
from dataguard.profiler import profile_data
from dataguard.core.engine import run_engine
from dataguard.ui.table import build_table
from dataguard.ui.summary import build_summary_panel
from dataguard.utils import compute_quality_score
from pathlib import Path
from rich.console import Console

app = typer.Typer(help="DataGuard CLI - Data Quality Tool")
console = Console()


@app.callback()
def main(
    no_banner: bool = typer.Option(False, help="Disable banner display")
):
    if not no_banner:
        show_banner()


@app.command()
def scan(
    file: str,
    export: str = typer.Option(None),
    summary: bool = typer.Option(False),
    strict: bool = typer.Option(False),
):
    scan_command(file, export, summary, strict)


@app.command()
def report(
    file: str,
    export: str = typer.Option(None),
):
    report_command(file, export)


@app.command()
def fix(
    file: str,
    output: str = typer.Option(None),
    apply_changes: bool = typer.Option(False),
):
    from dataguard.core.fixer import apply_fixes

    with console.status("Loading dataset..."):
        df = load_data(file)

    with console.status("Profiling data..."):
        profile = profile_data(df)

    with console.status("Running engine..."):
        results = run_engine(df, profile)

    console.print(build_summary_panel(compute_quality_score(results)))
    console.print(build_table(results))

    if not apply_changes:
        console.print("\n⚠️ Dry run mode. Use --apply-changes to modify data.")
        return

    with console.status("Applying fixes..."):
        df_clean, changes = apply_fixes(df, results)

    for change in changes:
        console.print(f"✔ {change}")

    if not output:
        output = "cleaned_data.csv"

    df_clean.write_csv(output)
    console.print(f"\n✅ Cleaned file saved to {output}")


@app.command()
def batch(
    folder: str,
    export: str = typer.Option(None),
):
    path = Path(folder)
    all_results = []

    for file in path.glob("*"):
        if file.suffix not in [".csv", ".json"]:
            continue

        console.print(f"\nProcessing: {file.name}")

        df = load_data(str(file))
        profile = profile_data(df)
        results = run_engine(df, profile)

        score = compute_quality_score(results)
        console.print(build_summary_panel(score))

        all_results.append({
            "file": file.name,
            "score": score,
            "issues": results
        })

    if export:
        from dataguard.utils import export_json
        export_json(all_results, export)
        console.print(f"Batch report exported to {export}")


if __name__ == "__main__":
    app()