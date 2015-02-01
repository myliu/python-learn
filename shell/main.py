import os
import sys
import subprocess

def main():
    shellpath = os.path.join(os.path.dirname(__file__), 'shell.py')
    subprocess.call([sys.executable, shellpath])

if __name__ == '__main__':
    sys.exit(main())