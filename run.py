import subprocess
import sys


def run(command):
    result = subprocess.run(command)
    if result.returncode != 0:
        sys.exit(result.returncode)


if __name__ == "__main__":
    run(["docker", "build", "-t", "lusada_marketday", "."])
    run(["docker", "run", "--rm", "-p", "8080:8080", "lusada_marketday"])