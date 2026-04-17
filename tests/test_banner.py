from rich.console import Console
from dataguard.ui.banner import show_banner

def test_show_banner_output():
    console = Console(record=True)

    show_banner(console)

    output = console.export_text()

    assert "DataGuard" in output
    assert "Data Quality Engine Initialized" in output