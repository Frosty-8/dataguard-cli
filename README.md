# DataGuard CLI

**DataGuard CLI** is a fast, modular data quality tool that helps developers validate, analyze, and clean datasets before using them in analytics or machine learning pipelines.

Built with **Polars**, **Rich**, and **Typer**, it provides a powerful command-line interface for profiling datasets and detecting issues such as missing values, duplicates, and inconsistent formats.

---

## 🚀 Features

* ⚡ Fast data profiling using **Polars**
* 🧠 Rule-based issue detection engine
* 📊 Dataset quality scoring system
* 🔍 Detailed column-level analysis
* 🛠️ Safe and controlled data fixing (dry-run by default)
* 📁 Batch processing for multiple datasets
* 🔒 Strict mode for pipeline enforcement
* 🎨 Rich CLI interface with tables and panels
* ⚙️ Configurable validation rules (YAML-based)
* ✅ Fully testable and modular architecture

---

## 📦 Installation

### From PyPI

```bash
pip install dataguard-cli
```

---

## 🧑‍💻 Usage

> After installation, use the `dataguard` command.
> If CLI is not available, fallback to:
>
> ```bash
> python -m dataguard.cli
> ```

---

### 🔍 Scan a dataset

```bash
dataguard.cli scan data.csv
```

---

### 📊 Show only important issues

```bash
python -m dataguard.cli scan data.csv --summary
```

---

### 📤 Export scan report

```bash
python -m dataguard.cli scan data.csv --export report.json
```

---

### 🔒 Strict mode (for pipelines / CI)

```bash
python -m dataguard.cli scan data.csv --strict
```

---

## 🛠️ Fix dataset issues

By default, **DataGuard runs in dry-run mode** (no changes applied):

Do not go for these changes as of now, still working on these commands due to real life edge cases do keep changin so please wait for this update in future.
Focus on Data analytics part with the summary been received for smoother explanations and insights.

```bash
python -m dataguard.cli fix data.csv
```

Apply changes explicitly:

```bash
python -m dataguard.cli fix data.csv --apply-changes
```

Optionally specify output file:

```bash
python -m dataguard.cli fix data.csv --apply-changes --output cleaned.csv
```

---

## 📄 Generate structured report

```bash
python -m dataguard.cli report data.csv
```

Export report:

```bash
python -m dataguard.cli report data.csv --export report.json
```

---

## 📁 Batch processing

```bash
python -m dataguard.cli batch ./datasets/
```

Export batch results:

```bash
python -m dataguard.cli batch ./datasets/ --export batch.json
```

---

## 📊 Example Output

```
📊 Dataset Quality Score: 37.5/100 🔴

Column   Type     Null %   Severity   Issues
--------------------------------------------------------
age      String   52%      5          High missing values
email    String   0%       4          Invalid format
name     String   11%      3          Missing values
```

---

## ⚙️ Configuration

Edit rules in:

```
dataguard/config/rules.yaml
```

Example:

```yaml
null_thresholds:
  critical: 30
  warning: 0

duplicate_threshold: 0
constant_column: true
email_validation: true
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🏗️ Architecture

```
CLI → Commands → Core Engine → Rules → UI
```

* **CLI**: Typer-based command interface
* **Core**: Rule engine and processing logic
* **UI**: Rich-based rendering
* **Config**: YAML-driven rules

---

## 💡 Why DataGuard?

Data quality issues are a major cause of:

* incorrect analytics
* unreliable ML models
* pipeline failures

DataGuard provides a lightweight and extensible way to enforce data validation before downstream usage.

---

## 🔮 Future Improvements

* Schema validation support
* ML-based anomaly detection
* Strategy-based fixing engine (safe / smart / aggressive)
* Integration with data pipelines (Airflow, etc.)
* Plugin-based rule system

---

## 🛠️ Tech Stack

* Python
* Polars
* Rich
* Typer
* Pytest

---

## 👨‍💻 Author

Sarthak Dongare (Frosty-8)
