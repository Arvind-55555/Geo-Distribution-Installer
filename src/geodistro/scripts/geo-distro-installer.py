import sys
import subprocess

def main():
    print("Running Python Installer script...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "."])

if __name__ == "__main__":
    main()
