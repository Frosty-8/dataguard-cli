from dataclasses import dataclass

@dataclass
class ColumnResult:
    column: str
    dtype: str
    null_pct: float
    unique_count: int
    issue: str = ""
    suggestion: str = ""
    severity_score: int = 0