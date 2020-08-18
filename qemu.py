import os
import sys


def main():
    os.system("ls -al")
    os.system("cd qemu-vexpress-a9")
    os.system("scons -j2")
    os.system("qemu.sh")
    sys.exit(0)


if __name__ == "__main__":
    main()
