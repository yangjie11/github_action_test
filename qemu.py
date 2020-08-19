import os
import sys


def main():
    os.system("sudo apt-get install qemu")
    os.system("sudo apt -y install scons")
    os.system("sudo apt -y install gcc-arm-none-eabi")
    path = "qemu-vexpress-a9"
    retval = os.getcwd()
    os.chdir(path)
    os.system("scons -j2")
    os.system("sudo chmod a+x qemu.sh")
    sys.exit(0)


if __name__ == "__main__":
    main()
