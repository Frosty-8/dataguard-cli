# DataGuard CLI

**DataGuard CLI** is a fast, modular data quality tool that helps developers validate, analyze, and clean datasets before using them in analytics or machine learning pipelines.

Built with **Polars**, **Rich**, and **Typer**, it provides a powerful command-line interface for profiling datasets and detecting issues such as missing values, duplicates, and inconsistent formats.

---

## 🚀 Features

* ⚡ Fast data profiling using **Polars**
* 🧠 Rule-based issue detection engine
* 📊 Dataset quality scoring system
* 🔍 Detailed column-level analysis
* 🛠️ Auto-fix functionality for cleaning data
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

### From Source

```bash
git clone https://github.com/your-username/dataguard-cli.git
cd dataguard-cli
pip install -e .
```

---

## 🧑‍💻 Usage

### Scan a dataset

```bash
dataguard scan data.csv
```

### Show only important issues

```bash
dataguard scan data.csv --summary
```

### Export report

```bash
dataguard scan data.csv --export report.json
```

### Strict mode (CI/CD pipelines)

```bash
dataguard scan data.csv --strict
```

---

### Fix dataset issues

```bash
dataguard fix data.csv
dataguard fix data.csv --apply-changes
```

---

### Generate structured report

```bash
dataguard report data.csv
dataguard report data.csv --export report.json
```

---

### Batch processing

```bash
dataguard batch ./datasets/
```

---

## 📊 Example Output

```
📊 Dataset Quality Score: 78/100 🟠

Column   Type     Null %   Severity   Issues
--------------------------------------------------------
age      Int64    45%      3          High missing values
email    String   5%       2          Invalid format
salary   Float64  0%       0          Clean
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
