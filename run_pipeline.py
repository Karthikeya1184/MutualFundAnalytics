"""
Master Pipeline Runner
Bluestock Mutual Fund Analytics
"""

import subprocess
import sys

scripts = [
    "data_ingestion.py",
    "data_cleaning.py",
    "database_loader.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    subprocess.run([sys.executable, script])

print("\nPipeline Completed Successfully")