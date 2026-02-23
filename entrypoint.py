#!/usr/bin/env python3
import os
import subprocess


def main():
    workspace = os.environ.get("GITHUB_WORKSPACE", "/github/workspace")
    os.chdir(workspace)

    subprocess.run(
        ["git", "config", "--global", "--add", "safe.directory", workspace],
        check=True,
    )

    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    tag = result.stdout.strip()
    github_env = os.environ.get("GITHUB_ENV")
    if github_env:
        with open(github_env, "a", encoding="utf-8") as f:
            f.write(f"TAG={tag}\n")


if __name__ == "__main__":
    main()
