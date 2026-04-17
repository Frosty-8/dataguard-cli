from rich.console import Console
from rich.panel import Panel

from dataguard.loader import load_data
from dataguard.profiler import profile_data
from dataguard.core.engine import run_engine
from dataguard.utils import compute_quality_score, export_json

console = Console()


def generate_report(file: str):
    df = load_data(file)
    profile = profile_data(df)
    results = run_engine(df, profile)

    score = compute_quality_score(results)

    report = {
        "file": file,
        "rows": df.height,
        "columns": len(df.columns),
        "quality_score": score,
        "columns_analysis": [
            r.to_dict() if hasattr(r, "to_dict") else r
            for r in results
        ],
    }

    return report, results


def display_report(report, results):
    score = report["quality_score"]

    status = (
        "🟢 Excellent"
        if score >= 90
        else "🟠 Moderate"
        if score >= 70
        else "🔴 Poor"
    )

    console.print(
        Panel.fit(
            f"[bold]File:[/bold] {report['file']}\n"
            f"[bold]Rows:[/bold] {report['rows']}\n"
            f"[bold]Columns:[/bold] {report['columns']}\n"
            f"[bold]Quality Score:[/bold] {score}/100\n"
            f"[bold]Status:[/bold] {status}",
            title="📄 Data Report Summary",
            border_style="cyan",
        )
    )

    critical = sum(1 for r in results if r["severity_score"] >= 3)
    warnings = sum(1 for r in results if 1 <= r["severity_score"] < 3)

    console.print(
        Panel.fit(
            f"[red]Critical Issues:[/red] {critical}\n"
            f"[yellow]Warnings:[/yellow] {warnings}\n"
            f"[green]Clean Columns:[/green] {len(results) - critical - warnings}",
            title="📊 Issue Breakdown",
            border_style="magenta",
        )
    )


def report_command(file: str, export: str = None):
    with console.status("[bold blue]Loading dataset..."):
        report, results = generate_report(file)

    display_report(report, results)

    if export:
        export_json(report, export)
        console.print(f"[green]Report exported to {export}[/green]")

    return report