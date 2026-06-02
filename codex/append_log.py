import datetime
import os

def append_telemetry_log(file_path, sector, throughput, latency):
    """Appends a timestamped system metric entry to the markdown file."""
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Format the log entry as a clean markdown table row or block
    log_entry = f"\n| {timestamp} | {sector:<12} | {throughput:<10} | {latency:<8} | AUTOMATED |\n"
    
    try:
        # Open in append mode ('a')
        with open(file_path, "a", encoding="utf-8") as file:
            # Add table headers if it's a completely new log section
            if os.path.getsize(file_path) == 0:
                file.write("| Timestamp | Sector | Throughput | Latency | Status |\n")
                file.write("|---|---|---|---|---|\n")
            
            file.write(log_entry)
        print(f"[SUCCESS] Metrics recorded for {sector} at {timestamp}.")
    except FileNotFoundError:
        print(f"[ERROR] Target file '{file_path}' not found.")

# Example usage:
if __name__ == "__main__":
    TARGET_FILE = "dwd-imperial-portfolio-ledger.md"
    append_telemetry_log(TARGET_FILE, "SCION-CORE", "8.8k XP/s", "08ms")
