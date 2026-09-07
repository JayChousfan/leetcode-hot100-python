"""运行 Hot 100 的 20 道简单题答案。"""

from pathlib import Path
import os
import subprocess
import sys


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    files = sorted((Path(__file__).parent / "solutions").glob("e*.py"))

    for path in files:
        print(f"▶ {path.name}", flush=True)
        subprocess.run([sys.executable, str(path)], check=True, env=env)

    print(f"🎉 全部 {len(files)} 道简单题测试通过")
