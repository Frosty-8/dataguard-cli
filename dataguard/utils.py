import json


def export_json(results, output_path):
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4, default=str)


def compute_quality_score(results):
    if not results:
        return 100

    total_score = sum(r["severity_score"] for r in results)
    max_score = len(results) * 5

    quality = 100 - (total_score / max_score) * 100
    return round(quality, 2)