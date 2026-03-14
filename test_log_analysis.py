import json


def filter_by_level(lines, wanted_level):
    if not isinstance(lines, list):
        return []
    result = []
    for line in lines:
        try:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            level = parts[1].strip()
            if level == wanted_level:
                result.append(line)
        except Exception:
            continue
    return result


def count_levels(lines):
    counts = {}
    if not isinstance(lines, list):
        return counts
    for line in lines:
        try:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            level = parts[1].strip()
            if not level:
                continue
            counts[level] = counts.get(level, 0) + 1
        except Exception:
            continue
    return counts


def count_services(lines):
    counts = {}
    if not isinstance(lines, list):
        return counts
    for line in lines:
        try:
            parts = line.split("|")
            if len(parts) < 3:
                continue
            service = parts[2].strip()
            if not service:
                continue
            counts[service] = counts.get(service, 0) + 1
        except Exception:
            continue
    return counts


def read_logs_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


if __name__ == "__main__":
    logs = read_logs_from_file("logs.txt")

    # 1) filter logs by level
    error_logs = filter_by_level(logs, "ERROR")

    # 2) count logs by level
    level_counts = count_levels(logs)

    # 3) count logs by service
    service_counts = count_services(logs)

    output = {
        "filtered_error_logs": error_logs,
        "counts_by_level": level_counts,
        "counts_by_service": service_counts,
    }

    # Write output to JSON file
    with open("output.json", "w", encoding="utf-8") as out_file:
        json.dump(output, out_file, indent=2)

    # Also print to console for confirmation
    print(json.dumps(output, indent=2))
