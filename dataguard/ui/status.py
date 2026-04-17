from rich.console import Console

def status(message, console: Console = None):
    if console is None:
        console = Console()

    return console.status(f"[bold blue]{message}")