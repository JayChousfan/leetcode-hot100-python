"""检查 20 道简单题是否仍在等待填写。"""

from pathlib import Path
import subprocess
import sys


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    files = sorted(Path(__file__).parent.glob("e*.py"))
    count = 0

    for path in files:
        result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        if "NameError" in result.stderr:
            count += 1
            print(f"⏳ {path.name}: 等待填写")

    print(f"共 {count}/{len(files)} 道题等待填写")
