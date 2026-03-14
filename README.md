# Applying-Filtering-and-Counting-Skills

A small Python utility repository demonstrating log processing skills including filtering and counting through structured log lines.

## 📁 Repository structure

- `logs.txt` - input log file (one entry per line, pipe-separated format: `timestamp | level | service | message`).
- `test_log_analysis.py` - functions to filter and count logs, plus a runnable script that generates `output.json`.
- `output.json` - generated output (filtered logs + aggregated counts by level and service).

## 🔧 Functions

- `filter_by_level(lines, wanted_level)` - returns log lines with the given severity level.
- `count_levels(lines)` - returns a dictionary count for each log level.
- `count_services(lines)` - returns a dictionary count for each service.
- `read_logs_from_file(path)` - reads non-empty lines from a file.

## ▶️ Run the script

```bash
python test_log_analysis.py
```

This loads `logs.txt`, filters `ERROR` logs, counts per level and service, then writes results to `output.json` and prints them.

## ✅ Example output structure (`output.json`)

```json
{
  "filtered_error_logs": [ ... ],
  "counts_by_level": { "INFO": 5, "ERROR": 2, ... },
  "counts_by_service": { "auth": 3, "db": 4, ... }
}
```

## 🧪 Testing

You can add unit tests around the three functions (`filter_by_level`, `count_levels`, `count_services`) using pytest or unittest.

## 💡 Notes

- The parser is resilient to malformed lines and skips entries with fewer than 3 pipe-separated fields.
- Non-list input values return empty results to avoid crashes.
