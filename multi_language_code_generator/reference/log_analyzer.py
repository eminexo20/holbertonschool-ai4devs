import re
from collections import Counter
from typing import Dict, List, Optional, Union


LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+(?P<bytes>\d+|-)$'
)


class LogAnalyzer:
    def parse_line(self, line: str) -> Optional[Dict[str, Union[str, int]]]:
        match = LOG_PATTERN.match(line.strip())
        if not match:
            return None

        status = int(match.group("status"))
        if not (100 <= status <= 599):
            return None

        raw_bytes = match.group("bytes")
        byte_count = 0 if raw_bytes == "-" else int(raw_bytes)

        return {
            "ip": match.group("ip"),
            "timestamp": match.group("timestamp"),
            "method": match.group("method"),
            "path": match.group("path"),
            "protocol": match.group("protocol"),
            "status": status,
            "bytes": byte_count,
        }

    def analyze(self, raw_logs: Union[str, List[str]]) -> Dict[str, Union[int, float, Optional[str]]]:
        lines = raw_logs.splitlines() if isinstance(raw_logs, str) else raw_logs

        total_requests = 0
        error_count = 0
        total_bytes = 0
        malformed_entries = 0
        visitors = set()
        endpoint_counts: Counter = Counter()

        for line in lines:
            if not line or not line.strip():
                continue

            parsed = self.parse_line(line)
            if parsed is None:
                malformed_entries += 1
                continue

            total_requests += 1
            visitors.add(parsed["ip"])
            total_bytes += int(parsed["bytes"])
            endpoint_counts[str(parsed["path"])] += 1

            if int(parsed["status"]) >= 400:
                error_count += 1

        if total_requests == 0:
            error_rate = 0.0
            top_endpoint = None
        else:
            error_rate = round((error_count / total_requests) * 100, 2)
            max_count = max(endpoint_counts.values())
            top_endpoint = sorted(
                path for path, count in endpoint_counts.items() if count == max_count
            )[0]

        return {
            "total_requests": total_requests,
            "unique_visitors": len(visitors),
            "error_rate": error_rate,
            "total_bytes": total_bytes,
            "top_endpoint": top_endpoint,
            "malformed_entries": malformed_entries,
        }
