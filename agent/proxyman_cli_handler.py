from __future__ import annotations

import subprocess
import os
import datetime
import time


def capture_logs_with_proxyman(domains: list[str], output_dir: str = "~/Desktop/output") -> str | None:
    try:
        output_dir = os.path.expanduser(output_dir)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(output_dir, f"proxyman_logs_{timestamp}.txt")
        output_path = os.path.expanduser(output_path)  # ✅ expand in case user path present

        os.makedirs(output_dir, exist_ok=True)

        cmd = [
            "/Applications/Proxyman.app/Contents/MacOS/proxyman-cli",
            "export-log",
            "-m", "domains",
            "-o", output_path,
            "--format", "raw"
        ]

        for domain in domains:
            cmd.extend(["--domains", domain])

        print(f"[INFO] Exporting logs for: {domains}")
        subprocess.run(cmd, check=True)

        time.sleep(1)  # ✅ give FS some time to flush logs
        print(f"[DEBUG] Returning log file path: {output_path}")
        return output_path

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Proxyman CLI failed: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return None



def filter_logs(path: str, keyword: str) -> str:
    print(f"[DEBUG] Checking file path: {path}")

    if not os.path.exists(path):
        return f"❌ Log file not found at {path}"

    # ✅ If path is a directory, get first .txt or .log inside
    if os.path.isdir(path):
        candidates = [f for f in os.listdir(path) if f.endswith(".txt") or f.endswith(".log")]
        if not candidates:
            return "❌ No readable log files found in export directory."
        path = os.path.join(path, candidates[0])
        print(f"[DEBUG] Reading log from: {path}")

    result = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if keyword.lower() in line.lower():
                result.append(line)

    return "\n".join(result) if result else f"No logs found for '{keyword}'"