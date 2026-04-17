from rich.console import Console
from pyfiglet import figlet_format

def show_banner(console: Console = None):
    if console is None:
        console = Console()

    banner = figlet_format("DataGuard", font="slant")
    console.print(f"[bold cyan]{banner}[/bold cyan]")
    console.print(f"[bold cyan]DataGuard[/bold cyan]")
    console.print("[bold green]⚡ Data Quality Engine Initialized[/bold green]\n")