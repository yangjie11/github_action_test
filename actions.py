import os


def main():
    os.system("apt -y update && apt -y upgrade")
    os.chdir("/rt-thread/actions")
    os.system("pip install selenium")
    os.system("python rt-thread-club.py")


if __name__ == "__main__":
    main()
