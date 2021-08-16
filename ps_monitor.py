# 监控安卓进程的变化

import os
import time
import frida
import subprocess
from datetime import datetime, timezone


def ps():
    body = subprocess.check_output(["adb", "shell", "ps", "-A"])
    results = []
    for line in body.decode().split("\n"):
        item = line.split()
        if len(item) == 0:
            continue
        if item[-1] == "ps":
            continue
        results.append(f"{item[0]}, {item[1]}, {item[-1]}")
    return results


def main():
    base = ps()
    while True:
        time.sleep(0.1)
        current = ps()
        lines_new = set(current) - set(base)
        lines_del = set(base) - set(current)
        if len(lines_new) + len(lines_del) > 0:
            print(time.asctime(), "----------------")
        for i, item in enumerate(lines_new):
            print(time.asctime(), "new", item)
        for i, item in enumerate(lines_del):
            print(time.asctime(), "del", item)
        base = current


if __name__ == '__main__':
    main()
