from pathlib import Path

from dataguard.commands.report import report_command


def test_report_structure():
    file_path = Path("examples/sample.csv")

    report = report_command(str(file_path))

    assert isinstance(report, dict)
    assert "file" in report
    assert "rows" in report
    assert "columns" in report
    assert "quality_score" in report
    assert "columns_analysis" in report

    assert report["rows"] > 0
    assert report["columns"] > 0
    assert isinstance(report["columns_analysis"], list)


def test_report_export(tmp_path):
    file_path = "examples/sample.csv"
    output_file = tmp_path / "report.json"

    report = report_command(file_path, export=str(output_file))

    assert output_file.exists()

    # Optional: validate content structure
    import json
    with open(output_file, "r") as f:
        data = json.load(f)

    assert "quality_score" in data
    assert "columns_analysis" in data