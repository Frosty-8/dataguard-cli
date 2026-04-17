from rich.console import Console

from dataguard.loader import load_data
from dataguard.profiler import profile_data
from dataguard.core.engine import run_engine
from dataguard.ui.table import build_table
from dataguard.ui.summary import build_summary_panel
from dataguard.utils import compute_quality_score, export_json

console = Console()


def scan_command(
    file: str,
    export: str = None,
    summary: bool = False,
    strict: bool = False,
):
    with console.status("[bold blue]Loading dataset..."):
        df = load_data(file)

    with console.status("[bold yellow]Profiling data..."):
        profile = profile_data(df)

    with console.status("[bold green]Running data quality engine..."):
        results = run_engine(df, profile)

    score = compute_quality_score(results)

    if summary:
        results = [r for r in results if r["severity_score"] > 1]

    console.print(build_summary_panel(score))
    console.print(build_table(results))

    if export:
        export_json(results, export)
        console.print(f"[green]Report exported to {export}[/green]")

    if strict and any(r["severity_score"] >= 3 for r in results):
        console.print("[bold red]❌ Critical issues found. Exiting (strict mode).[/bold red]")
        raise SystemExit(1)

    return results