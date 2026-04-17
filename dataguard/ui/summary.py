from rich.panel import Panel

def build_summary_panel(score):
    if score >= 90:
        status = "🟢 Excellent"
    elif score >= 70:
        status = "🟠 Moderate"
    else:
        status = "🔴 Poor"

    return Panel.fit(
        f"[bold]Dataset Quality Score:[/bold] {score}/100\n[bold]Status:[/bold] {status}",
        title="📊 Summary",
        border_style="cyan"
    )